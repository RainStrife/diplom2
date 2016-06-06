# coding: utf-8
import json

from django import template
register = template.Library()


@register.filter('get_value_from_dict')
def get_value_from_dict(dict, key):
    """
    usage example {{ your_dict|get_value_from_dict:your_key }}
    """
    if key:
        return dict.get(key)
