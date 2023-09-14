from django.test import Client
from django.urls import reverse, resolve
import pytest
from lettings.models import Letting, Address


class TestLettingsURLs:
    client = Client()

    def create_letting(self):
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
        path = reverse('lettings_index')

        assert path == "/lettings/"
        assert resolve(path).view_name == "lettings_index"

    @pytest.mark.django_db
    def test_letting_url(self):
        self.create_letting()
        path = reverse('letting', args=[1])

        assert path == "/lettings/1/"
        assert resolve(path).view_name == "letting"
