from django.test import Client
from django.urls import reverse, resolve


class TestBaseURLs:
    client = Client()

    def test_index_url(self):
        path = reverse('index')
        assert path == "/"
        assert resolve(path).view_name == "index"
