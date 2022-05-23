from django.urls import reverse
from django.test import TestCase, Client

from http import HTTPStatus

from os import path

from shortener.models import Url
from shortener.utils import get_short_id


class UrlViewsTest(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.url_to_shorten = 'https://docs.djangoproject.com/en/4.0/topics/db/queries/#making-queries'
        cls.shorten_url = get_short_id()
        cls.Url = Url.objects.create(
            http_url=cls.url_to_shorten,
            short_id=cls.shorten_url
        )

    def setUp(self) -> None:
        self.client = Client()

    def test_correct_template_used_for_reverse(self):
        template = path.join('shortener', 'index.html')
        response = self.client.get(reverse('shortener:index'))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, template)

    def test_correct_template_has_correct_context(self):
        response = self.client.get(reverse('shortener:index'))
        self.assertIn('form', response.context)
        self.assertNotIn('shorted_url', response.context)

    def test_short_url_do_redirect(self):
        response = self.client.get(
            reverse('shortener:redirect_to', args=[self.shorten_url])
        )
        self.assertEqual(response.headers['Location'], self.url_to_shorten)
