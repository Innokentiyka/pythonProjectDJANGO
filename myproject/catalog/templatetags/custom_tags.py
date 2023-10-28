from django import template

register = template.Library()

@register.simple_tag
def mediapath(value):
    return "/media/" + value