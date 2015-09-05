from django import template
from django.utils.safestring import mark_safe

from djcelery.admin import TASK_STATE_COLORS


register = template.Library()


@register.filter
def colored_state(task):
    color = TASK_STATE_COLORS.get(task.state, 'black')
    state = '<b><span style="color: {0};">{1}</span></b>'.format(color, task.state)
    return mark_safe(state)