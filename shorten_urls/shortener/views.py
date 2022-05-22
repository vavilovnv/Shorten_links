from os import path
from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings

from .models import Url
from .forms import UrlForm

from .utils import get_short_id


def index(request):
    template = path.join('shortener', 'index.html')
    # template = path.join('shortener/index.html')
    if not request.method == 'POST':
        form = UrlForm()
        return render(request, template, {'form': form})
    form = UrlForm(request.POST)
    if not form.is_valid():
        return render(request, template, {'form': form})
    short_url = form.save(commit=False)
    short_url.short_id = get_short_id()
    short_url.save()
    return render(
        request,
        template,
        {
            'form': form,
            'shorted_url': f'{settings.SITE_URL}{short_url.short_id}'
        }
    )


def shorted_url_redirect(request, slug):
    url_object = get_object_or_404(Url, short_id=slug)
    url_object.counts_of_visits += 1
    url_object.save()
    return redirect(url_object.http_url)
