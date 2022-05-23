from django.test import TestCase, Client
from django.urls import reverse

from http import HTTPStatus

from shortener.models import Url


class UrlFormTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url_to_shorten = 'https://docs.djangoproject.com/en/4.0/topics/db/queries/#making-queries'
        
    def test_client_can_short_url(self):
        response = self.client.post(
            reverse('shortener:index'),
            data = {'http_url': self.url_to_shorten},
            follow=True
        )
        self.assertEqual(response.status_code, HTTPStatus.OK)
        url = Url.objects.first()
        self.assertEqual(url.http_url, self.url_to_shorten)
