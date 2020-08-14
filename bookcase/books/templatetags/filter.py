from django import template

register = template.Library()


@register.filter(name='userbasket')
def userbasket(object, user):
    return object.filter(user_id=user)
