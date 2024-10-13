"""
Tests for models.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


def create_user(email='user@example.com', password='test123'):
    """Create and return a new user."""
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):
    """Test models."""

    def test_create_user_successful(self):
        """Test Creating a user"""
        email = 'test@exmaple.com'
        password = 'testpass123'
        user = create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_normalized(self):
        """Test email is normalized for new users."""
        sample_emails=[
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['test2@Example.com', 'test2@example.com'],
            ['test3@EXAMPLE.COM', 'test3@example.com'],
            ['test4@example.com', 'test4@example.com'],
        ]
        for input_email, expected_email in sample_emails:
            user = create_user(input_email, 'test123')
            self.assertEqual(user.email, expected_email)
