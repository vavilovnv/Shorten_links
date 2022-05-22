from django.db import models


class Url(models.Model):
    short_id = models.SlugField(unique=True)
    http_url = models.URLField(
        max_length=255,
        verbose_name='Ссылка для сокращения'
    )
    pub_date = models.DateTimeField(auto_now_add=True)
    counts_of_visits = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f'{self.http_url}'
