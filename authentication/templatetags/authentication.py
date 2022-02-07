from django import template
from django.conf import settings
from allauth.utils import get_form_class
from crispy_forms.utils import render_crispy_form
from django.template.context_processors import csrf
from django.template.loader import render_to_string

register = template.Library()

@register.simple_tag(takes_context=True)
def authentication_form(context,key):
    """Renders a named authentication form by the given key. Possible values are those listed in settings"""
    form = get_form_class(settings.ACCOUNT_FORMS, key, False)
    if not form:
        raise KeyError(f'Could not find form using the lookup key: {key}. Possible values are {list(settings.ACCOUNT_FORMS.keys())}')
    return render_crispy_form(form, context=csrf(context['request']))


@register.simple_tag
def auth_link(type, link_text):
    template = f'authentication/links/{type}.html'
    return render_to_string(template, {'link_text': link_text})