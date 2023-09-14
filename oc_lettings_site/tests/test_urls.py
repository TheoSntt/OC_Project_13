"""
Defines the test class for the website home page url
"""
from django.test import Client
from django.urls import reverse, resolve


class TestBaseURLs:
    """
    Test class for the website home page url
    """
    client = Client()

    def test_index_url(self):
        """
        Test the index url.
        First assert that the right url path is returned.
        Second assert that the path calls the right view.
        """
        path = reverse('index')
        assert path == "/"
        assert resolve(path).view_name == "index"
