from django import template
from .. import models
from django.shortcuts import get_list_or_404

register = template.Library()

@register.assignment_tag
def photos_sub_menu():
    sub_menus =get_list_or_404(models.Categorie)
    return sub_menus
