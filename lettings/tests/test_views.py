from django.test import Client
from django.urls import reverse
from lettings.models import Letting, Address
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

        response = self.client.get(reverse('lettings_index'))

        assert response.status_code == 200
        assertTemplateUsed(response, 'lettings/index.html')

    @pytest.mark.django_db
    def test_LettingView(self):
        """
        First assert tests if there are issues rendering template by checking 200 status code,
        Second assert checks if our view is returning right template
        """

        # Create an adress object in the test db
        address = Address.objects.create(number=11,
                                         street="Rue des Peupliers",
                                         city="Nogent-le-Rotrou",
                                         state="Texas-sur-Ecole",
                                         zip_code="91540",
                                         country_iso_code=123)
        # Create a letting object in the test db
        letting = Letting.objects.create(title="Une tente 2 places dans un jardin",
                                         address=address)
        response = self.client.get(reverse('letting', args=[letting.id]))

        assert response.status_code == 200
        assertTemplateUsed(response, 'lettings/letting.html')
