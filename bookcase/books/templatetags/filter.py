from django import template
from books.models import UserBasket

register = template.Library()

@register.filter(name='userbasket')
def userbasket(object, user):
    return object.filter(user_id=user)
