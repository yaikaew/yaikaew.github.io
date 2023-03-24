from django import template


register = template.Library()


@register.filter
def get_list(dict, day):
    return dict[day]

@register.filter
def count(user, sub_id):
    return user.filter(sub_id_id = sub_id).count()