from django.test import TestCase
from .models import User, Skill

class SkillTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create(first_name="John", last_name="Doe", email="john@example.com")
        self.skill = Skill.objects.create(name="Jardinage")
        self.user.skills.add(self.skill)

    def test_user_has_skill(self):
        self.assertIn(self.skill, self.user.skills.all())

    def test_skill_str(self):
        self.assertEqual(str(self.skill), "Jardinage")
