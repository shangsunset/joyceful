from django import template
from random import randint

register = template.Library()

@register.assignment_tag()
def random_number():
    return randint(1, 2)




@register.assignment_tag()
def increment(val):
    val = val + 1
    return val


@register.assignment_tag()
def set_num_of_albums(num=0):
    return num
