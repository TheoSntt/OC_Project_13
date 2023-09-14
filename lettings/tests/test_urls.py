"""
Defines the test class for the lettings app url routes
"""
from django.test import Client
from django.urls import reverse, resolve
import pytest
from lettings.models import Letting, Address


class TestLettingsURLs:
    """
    Test class for the lettings app url routes
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

    def test_index_url(self):
        """
        Test the index url.
        First assert that the right url path is returned.
        Second assert that the path calls the right view.
        """
        path = reverse('lettings_index')

        assert path == "/lettings/"
        assert resolve(path).view_name == "lettings_index"

    @pytest.mark.django_db
    def test_letting_url(self):
        """
        Test the letting url.
        First assert that the right url path is returned.
        Second assert that the path calls the right view.
        """
        self.create_letting()
        path = reverse('letting', args=[1])

        assert path == "/lettings/1/"
        assert resolve(path).view_name == "letting"
