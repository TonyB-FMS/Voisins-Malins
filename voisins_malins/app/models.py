from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import datetime


class Visitor(models.Model):
    """
    Modèle représentant un visiteur, un utilisateur non connecté qui peut consulter
    les compétences et les créneaux disponibles sans pouvoir ajouter ou gérer des compétences.
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    def view_skills(self):
        """
        Retourne la liste de toutes les compétences disponibles dans l'application.

        :return: QuerySet des compétences
        """
        return Skill.objects.all()

    def view_available_slots(self):
        """
        Retourne les créneaux horaires où des utilisateurs sont disponibles pour apporter leur aide.

        :return: QuerySet des créneaux horaires disponibles
        """
        return TimeSlot.objects.filter(is_available=True)

    def search_skills(self, query):
        """
        Recherche des compétences dont le nom contient la chaîne de caractères fournie.

        :param query: Chaîne de caractères à rechercher dans les compétences.
        :return: QuerySet des compétences correspondantes
        """
        return Skill.objects.filter(name__icontains=query)


class AuthenticatedUser(Visitor):
    """
    Modèle représentant un utilisateur authentifié, héritant de Visitor, avec des capacités
    supplémentaires comme ajouter des compétences, définir des créneaux de disponibilité et demander de l'aide.
    """
    password = models.CharField(max_length=128)
    skills = models.ManyToManyField('Skill', blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def add_skill(self, skill):
        """
        Ajoute une compétence à l'utilisateur.

        :param skill: L'instance de Skill que l'utilisateur possède
        """
        self.skills.add(skill)

    def set_availability(self, timeslot):
        """
        Définit un créneau horaire comme disponible, après validation que ce créneau est effectivement libre.

        :param timeslot: L'instance de TimeSlot à marquer comme disponible.
        :raises ValidationError: Si le créneau n'est pas disponible.
        """
        if not timeslot.is_available:
            raise ValidationError(_("Ce créneau horaire n'est pas disponible"))
        timeslot.is_available = True
        timeslot.save()

    def request_help(self, activity, skill):
        """
        Crée une demande d'aide pour une activité spécifique, en précisant la compétence requise.
        Vérifie que l'utilisateur possède la compétence avant de créer la tâche.

        :param activity: Nom de l'activité pour laquelle de l'aide est demandée.
        :param skill: Compétence requise pour l'activité.
        :raises ValidationError: Si l'utilisateur ne possède pas la compétence requise.
        """
        if skill not in self.skills.all():
            raise ValidationError(_("Vous ne possédez pas la compétence requise pour cette tâche"))

        Task.objects.create(name=activity, required_skill=skill, user=self)


class Skill(models.Model):
    """
    Modèle représentant une compétence que les utilisateurs peuvent échanger.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        """
        Retourne le nom de la compétence sous forme de chaîne.

        :return: Nom de la compétence
        """
        return self.name

    def clean(self):
        """
        Validation pour vérifier que le nom de la compétence n'est pas vide.

        :raises ValidationError: Si le nom de la compétence est vide ou constitué uniquement d'espaces.
        """
        if not self.name.strip():
            raise ValidationError(_("Le nom de la compétence ne peut pas être vide"))


class TimeSlot(models.Model):
    """
    Modèle représentant un créneau horaire durant lequel un utilisateur est disponible pour aider.
    """
    date = models.DateField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        """
        Retourne la date du créneau sous forme de chaîne.

        :return: La date du créneau
        """
        return str(self.date)

    def clean(self):
        """
        Validation pour vérifier qu'un créneau horaire ne peut pas être défini comme disponible si la date est dans le passé.

        :raises ValidationError: Si la date du créneau est dans le passé.
        """
        if self.date < datetime.date.today():
            raise ValidationError(_("La date du créneau horaire ne peut pas être dans le passé"))


class Task(models.Model):
    """
    Modèle représentant une tâche ou une demande d'aide pour une activité, en précisant la compétence requise.
    """
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    required_skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    user = models.ForeignKey(AuthenticatedUser, on_delete=models.CASCADE)

    def __str__(self):
        """
        Retourne le nom de la tâche sous forme de chaîne.

        :return: Nom de la tâche
        """
        return self.name

    def clean(self):
        """
        Validation pour vérifier qu'une tâche a une compétence requise associée.

        :raises ValidationError: Si aucune compétence n'est associée à la tâche.
        """
        if not self.required_skill:
            raise ValidationError(_("La tâche doit être associée à une compétence"))

    @classmethod
    def create_task(cls, name, description, skill, user):
        """
        Crée une tâche après validation que l'utilisateur et la compétence sont fournis.

        :param name: Nom de la tâche.
        :param description: Description de la tâche (optionnelle).
        :param skill: Compétence requise pour la tâche.
        :param user: L'utilisateur qui demande de l'aide.
        :return: L'instance de Task créée.
        :raises ValidationError: Si la compétence ou l'utilisateur est manquant.
        """
        if not skill or not user:
            raise ValidationError(_("La compétence et l'utilisateur sont nécessaires pour créer une tâche"))

        return cls.objects.create(name=name, description=description, required_skill=skill, user=user)
