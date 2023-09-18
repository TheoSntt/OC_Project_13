"""
Defines the test class for the lettings app views
"""
from django.test import Client
from django.urls import reverse
from lettings.models import Letting, Address
import pytest
from pytest_django.asserts import assertTemplateUsed


class TestLettingsViews:
    """
    Test class for the lettings app views
    """
    client = Client()

    def create_letting(self):
        """
        Helper function that creates a Letting, for use in tests that needs
        for a letting to exist.
        The function creates a Address first, for Letting is linked to Address.
        """
        # Create an adress object
        address = Address.objects.create(
            number=11,
            street="Rue des Peupliers",
            city="Nogent-le-Rotrou",
            state="Texas-sur-Ecole",
            zip_code="91540",
            country_iso_code=123)
        # Create a letting object
        Letting.objects.create(
            title="Une tente 2 places dans un jardin",
            address=address)

    @pytest.mark.django_db
    def test_indexView(self):
        """
        Test the lettings app index view.
        First assert tests if there are issues rendering template by checking 200 status code,
        Second assert checks if our view is returning right template
        """

        response = self.client.get(reverse('lettings_index'))

        assert response.status_code == 200
        assertTemplateUsed(response, 'lettings/index.html')

    @pytest.mark.django_db
    def test_LettingView(self):
        """
        Test the lettings app letting view.
        First assert tests if there are issues rendering template by checking 200 status code,
        Second assert checks if our view is returning the right template
        """

        self.create_letting()
        response = self.client.get(reverse('letting', args=[1]))

        assert response.status_code == 200
        assertTemplateUsed(response, 'lettings/letting.html')

    @pytest.mark.django_db
    def test_LettingView_404(self):
        """
        Test the lettings app letting view 404 error.
        First assert tests if the status code is 404 when a non existing letting is queried,
        Second assert checks if our view is returning the right template.
        """

        # self.create_letting()
        response = self.client.get(reverse('letting', args=[1]))

        assert response.status_code == 404
        assertTemplateUsed(response, '404.html')
