from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from schedule_app.models import Employee, Availability, Schedule
import json

class TestViews(TestCase):

    def setUp(self):
        # Create a test user
        self.test_user = User.objects.create_user(username='testuser', password='testpassword')

    def test_project_list_GET(self):
        client = Client()

        # Authenticate the test user
        client.login(username='testuser', password='testpassword')

        # Make the request after authentication
        response = client.get(reverse('weeks'), follow = True)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'schedule_app/week_list.html')