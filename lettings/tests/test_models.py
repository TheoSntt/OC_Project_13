"""
Defines the test class for the lettings app models
"""
from django.test import Client
from lettings.models import Letting, Address
import pytest


class TestLettingModels:
    """
    Test class for the lettings app models
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
        letting = Letting.objects.create(
            title="Une tente 2 places dans un jardin",
            address=address)

        return {'address': address,
                'letting': letting}

    @pytest.mark.django_db
    def test_lettingModel(self):
        """
        Test the Letting model.
        Creates a Letting and then calls its str() method.
        """
        letting = self.create_letting()['letting']

        expected_value = "Une tente 2 places dans un jardin"
        assert str(letting) == expected_value

    @pytest.mark.django_db
    def test_adressModel(self):
        """
        Test the Address model.
        Creates a Address and then calls its str() method.
        """
        address = self.create_letting()['address']

        expected_value = "12 Rue des Peupliers"
        assert str(address) == expected_value
