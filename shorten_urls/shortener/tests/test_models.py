from django.test import TestCase

from shortener.models import Url
from shortener.utils import get_short_id


class UrlModelTest(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.url_to_shorten = 'https://docs.djangoproject.com/en/4.0/topics/db/queries/#making-queries'
        cls.Url = Url.objects.create(
            http_url=cls.url_to_shorten,
            short_id=get_short_id()
        )

    def test_fields_verbose_name(self):
        field_verboses = {
            'http_url': 'Ссылка для сокращения'
        }

        for field, verbose_name in field_verboses.items():
            with self.subTest(field=field):
                self.assertEqual(self.Url._meta.get_field(field).verbose_name, verbose_name)

    def test_model_str_has_overload(self):
        self.assertEqual(str(self.Url), self.url_to_shorten)