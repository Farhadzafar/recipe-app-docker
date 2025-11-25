"""
Docstring for app.core.tests.test_models
"""
from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):
    """Tests for core models."""

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful."""
        def test_create_user_with_email_successful(self):
            email = 'Test@example.com'
            password = 'Testpass123'
            user= get_user_model().objects.create_user(
                email=email,
                password=password
            )

            self.assertEqual(email = email)
            self.assertEqual(password = password)

    