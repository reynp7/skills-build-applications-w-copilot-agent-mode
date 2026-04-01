from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team')
        self.user = User.objects.create(name='Test User', email='test@example.com', team=self.team)
        self.workout = Workout.objects.create(name='Pushups', description='Do 20 pushups')
        self.activity = Activity.objects.create(user=self.user, type='run', duration=30, date='2023-01-01')
        self.leaderboard = Leaderboard.objects.create(team=self.team, points=100)

    def test_user_str(self):
        self.assertEqual(str(self.user), 'test@example.com')
    def test_team_str(self):
        self.assertEqual(str(self.team), 'Test Team')
    def test_activity_str(self):
        self.assertIn('test@example.com', str(self.activity))
    def test_workout_str(self):
        self.assertEqual(str(self.workout), 'Pushups')
    def test_leaderboard_str(self):
        self.assertIn('Test Team', str(self.leaderboard))
