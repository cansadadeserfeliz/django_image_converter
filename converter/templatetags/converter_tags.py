import re

from django import template
from django.utils.safestring import mark_safe
from django.conf import settings

from djcelery.admin import TASK_STATE_COLORS


register = template.Library()
task_file_pattern = re.compile('[\w\-]+\.jpg')


@register.filter
def colored_state(task):
    color = TASK_STATE_COLORS.get(task.state, 'black')
    state = '<b><span style="color: {0};">{1}</span></b>'.format(color, task.state)
    return mark_safe(state)


@register.filter
def get_task_url(task):
    result = task_file_pattern.search(task.result)
    if result:
        return '{0}{1}'.format(
            settings.MEDIA_URL,
            result.group()
        )
    return '#'
