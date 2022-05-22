from string import ascii_lowercase
from random import choice
from hashlib import sha1

from django.conf import settings


def get_short_id():
    code = ''.join(
        [choice(ascii_lowercase) for _ in range(settings.SHORTEN_URL_LENGHT)]    
    )
    return sha1(code.encode()).hexdigest()[:settings.SHORTEN_URL_LENGHT]
