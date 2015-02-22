from django import template
from random import randint

register = template.Library()

@register.assignment_tag()
def random_number():
    return randint(1, 2)


@register.assignment_tag()
def count_big():
    return 0


@register.assignment_tag()
def count_small():
    return 0


@register.assignment_tag()
def increment(val):
    val = val + 1
    return val
