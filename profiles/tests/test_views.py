"""
Defines the test class for the profiles app views
"""
from django.contrib.auth.models import User
from django.test import Client
from django.urls import reverse
from profiles.models import Profile
import pytest
from pytest_django.asserts import assertTemplateUsed


class TestProfilesViews:
    """
    Test class for the profiles app views
    """
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

    @pytest.mark.django_db
    def test_indexView(self):
        """
        Test the profiles app index view.
        First assert tests if there are issues rendering template by checking 200 status code,
        Second assert checks if our view is returning right template
        """

        response = self.client.get(reverse('profiles_index'))

        assert response.status_code == 200
        assertTemplateUsed(response, 'profiles/index.html')

    @pytest.mark.django_db
    def test_profileView(self):
        """
        Test the profiles app profile view.
        First assert tests if there are issues rendering template by checking 200 status code,
        Second assert checks if our view is returning the right template
        """
        self.create_profile()

        response = self.client.get(reverse('profile', args=["bobmorane"]))

        assert response.status_code == 200
        assertTemplateUsed(response, 'profiles/profile.html')

    @pytest.mark.django_db
    def test_profileView_404(self):
        """
        Test the profiles app profile view 404 error.
        First assert tests if the status code is 404 when a non existing profile is queried,
        Second assert checks if our view is returning the right template.
        """
        # self.create_profile()

        response = self.client.get(reverse('profile', args=["bobmorane"]))

        assert response.status_code == 404
        assertTemplateUsed(response, '404.html')
