from django.contrib.auth.models import User
from django.test import Client
from django.urls import reverse
from profiles.models import Profile
import pytest
from pytest_django.asserts import assertTemplateUsed


class TestLettingsViews:
    client = Client()

    @pytest.mark.django_db
    def test_indexView(self):
        """
        First assert tests if there are issues rendering template by checking 200 status code,
        Second assert checks if our view is returning right template
        """

        response = self.client.get(reverse('profiles_index'))

        assert response.status_code == 200
        assertTemplateUsed(response, 'profiles/index.html')

    @pytest.mark.django_db
    def test_profileView(self):
        """
        First assert tests if there are issues rendering template by checking 200 status code,
        Second assert checks if our view is returning right template
        """

        # Create an adress object in the test db
        user = User.objects.create(
            username="bobmorane",
            password="bob123",
            first_name="Bob",
            last_name="Morane",
            email="bob.morane@mail.fr"
        )
        # Create a letting object in the test db
        profile = Profile.objects.create(user=user,
                                         favorite_city=1)
        response = self.client.get(reverse('profile', args=[profile.user.username]))

        assert response.status_code == 200
        assertTemplateUsed(response, 'profiles/profile.html')
