"""
Defines the test class for the website homepage view
"""
from django.test import Client
from django.urls import reverse
import pytest
from pytest_django.asserts import assertTemplateUsed


class TestBaseViews:
    """
    Test class for the website homepage view
    """
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

    @pytest.mark.django_db
    def test_404(self):
        """
        Test the response for a non existing URL.
        First assert tests if the status code is 404,
        Second assert checks if our app is rendering our custom 404.html template
        """

        response = self.client.get(reverse('index')+"wrong_url")

        assert response.status_code == 404
        assertTemplateUsed(response, '404.html')
