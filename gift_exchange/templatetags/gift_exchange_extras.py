from django import template
from django.template.defaultfilters import stringfilter
import datetime

register = template.Library()


@register.filter
def if_in_somewhere_is_something(query_set, user):
    for v_list in query_set:
        if v_list[1] == user:
            return bool(v_list[1] == user)


@register.filter
@stringfilter
def symbols_max(string: str):
    max_len = 80
    if string.__len__() > max_len:
        return str(string[0:max_len - 2] + '...')
    else:
        return string


@register.filter(expects_localtime=True)
def can_draw(date_time):
    v_date_time = datetime.datetime.strptime(str(date_time).split('+')[0], '%Y-%m-%d %H:%M:%S')
    current_time = datetime.datetime.strptime(str(datetime.datetime.now()).split('.')[0], '%Y-%m-%d %H:%M:%S')
    return v_date_time < current_time


@register.filter
def to_whom_id(query_set, user):
    for v_list in query_set:
        if v_list[-3] == user:
            return v_list[-1]
