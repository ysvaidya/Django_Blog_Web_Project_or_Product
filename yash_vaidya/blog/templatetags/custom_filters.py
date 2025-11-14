# your_app/templatetags/custom_filters.py
from django import template
from django.template.defaultfilters import stringfilter
import re

register = template.Library()

@register.filter
@stringfilter
def truncate_smart(value, word_count=30):
    """
    Truncate after complete sentences near the word limit
    """
    words = value.split()
    
    if len(words) <= word_count:
        return value
    
    # Take first X words
    truncated = ' '.join(words[:word_count])
    
    # Find the last sentence end (. ! ?) in the truncated text
    sentence_end = max(
        truncated.rfind('.'),
        truncated.rfind('!'),
        truncated.rfind('?')
    )
    
    # If we found a sentence end and it's not too early, use it
    if sentence_end > len(truncated) * 0.6:  # At least 60% through
        return truncated[:sentence_end + 1] + '..'
    
    # Otherwise, find the last space and truncate there
    last_space = truncated.rfind(' ')
    if last_space > 0:
        return truncated[:last_space] + '...'
    
    return truncated + '...'

# You can add more filters here
@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)