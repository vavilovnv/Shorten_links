from django.test import TestCase, Client

from http import HTTPStatus


class UrlsTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()    

    def test_index_url_access(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_index_url_has_correct_template(self):
        response = self.client.get('/')
        self.assertTemplateNotUsed(response, 'shortener/index.html')