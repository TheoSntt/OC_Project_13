from django.contrib.auth.models import User
from django.test import Client
from django.urls import reverse, resolve
import pytest
from profiles.models import Profile


class TestProfilesURLs:
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
        Profile.objects.create(
            user=user,
            favorite_city=1)

    def test_index_url(self):
        path = reverse('profiles_index')

        assert path == "/profiles/"
        assert resolve(path).view_name == "profiles_index"

    @pytest.mark.django_db
    def test_letting_url(self):
        self.create_profile()
        path = reverse('profile', args=[1])

        assert path == "/profiles/1/"
        assert resolve(path).view_name == "profile"
