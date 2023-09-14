from django.test import Client
from django.urls import reverse
import pytest
from pytest_django.asserts import assertTemplateUsed


class TestBaseViews:
    client = Client()

    @pytest.mark.django_db
    def test_indexView(self):
        """
        Test the main app index view.
        First assert tests if there are issues rendering template by checking 200 status code,
        Second assert checks if our view is returning right template
        """

        response = self.client.get(reverse('index'))

        assert response.status_code == 200
        assertTemplateUsed(response, 'index.html')
