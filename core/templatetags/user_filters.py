from django import template
from django.core.handlers.wsgi import WSGIRequest

register = template.Library()


@register.filter
def add_class(field, css=''):
    if field and not isinstance(field, WSGIRequest):
        return field.as_widget(attrs={'class': css})
    return field
