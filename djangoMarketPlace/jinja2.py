from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse
from jinja2 import Environment
from core.templatetags.user_filters import add_class
from django.contrib.humanize.templatetags.humanize import apnumber, intcomma, intword, naturalday, naturaltime, ordinal


def environment(**options):
    env = Environment(**options)
    env.globals.update({
        'static': staticfiles_storage.url,
        'url': reverse,
    })
    env.filters.update({
        # my filters
        'addclass': add_class,
        # django filters
        'apnumber': apnumber,
        'intcomma': intcomma,
        'intword': intword,
        'naturalday': naturalday,
        'naturaltime': naturaltime,
        'ordinal': ordinal,
    })
    return env
