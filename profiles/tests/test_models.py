from django.contrib.auth.models import User
from django.test import Client
from profiles.models import Profile
import pytest


class TestProfileModels:
    client = Client()

    def create_profile(self):
        """
        Helper function that creates a Profile, for use in tests that needs
        for a profile to exist.
        The function creates a User first, for Profile is linked to User.
        """
        user = User.objects.create(
            username="bobmorane",
            password="bob123",
            first_name="Bob",
            last_name="Morane",
            email="bob.morane@mail.fr"
        )
        profile = Profile.objects.create(
            user=user,
            favorite_city=1)

        return profile

    @pytest.mark.django_db
    def test_profileModel(self):
        """
        Test the Profile model
        Creates a Profile and then calls its str() method
        """
        profile = self.create_profile()

        expected_value = "bobmorane"
        assert str(profile) == expected_value
