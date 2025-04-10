from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
import json

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        with open('octofit-tracker/backend/octofit_tracker/test_data.json') as f:
            data = json.load(f)

        # Populate users
        for user_data in data['users']:
            User.objects.get_or_create(email=user_data['email'], defaults={
                'name': user_data['name'],
                'age': user_data['age']
            })

        # Populate teams
        for team_data in data['teams']:
            Team.objects.get_or_create(name=team_data['name'], defaults={
                'description': team_data['description']
            })

        # Populate activities
        for activity_data in data['activities']:
            user = User.objects.get(email=activity_data['user_email'])
            Activity.objects.get_or_create(user=user, activity_type=activity_data['activity_type'], defaults={
                'duration': activity_data['duration'],
                'timestamp': activity_data['timestamp']
            })

        # Populate leaderboard
        for leaderboard_data in data['leaderboard']:
            user = User.objects.get(email=leaderboard_data['user_email'])
            Leaderboard.objects.get_or_create(user=user, defaults={
                'points': leaderboard_data['points'],
                'rank': leaderboard_data['rank']
            })

        # Populate workouts
        for workout_data in data['workouts']:
            Workout.objects.get_or_create(name=workout_data['name'], defaults={
                'description': workout_data['description'],
                'difficulty': workout_data['difficulty']
            })

        self.stdout.write(self.style.SUCCESS('Database populated with test data.'))