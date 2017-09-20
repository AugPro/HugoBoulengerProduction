from django import template
from .. import models
from django.shortcuts import get_list_or_404

register = template.Library()

@register.assignment_tag
def format_socials():
    socials_list =get_list_or_404(models.Social)
    return socials_list
