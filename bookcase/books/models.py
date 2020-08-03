import uuid
from django.db import models
from taggit.managers import TaggableManager
from taggit.models import GenericUUIDTaggedItemBase, TaggedItemBase, Tag
from django.utils.translation import ugettext_lazy
from users.models import CustomUser


class UUIDTaggedItem(GenericUUIDTaggedItemBase, TaggedItemBase):
    tag = models.ForeignKey(Tag, related_name="uuid_tagged_items", on_delete=models.CASCADE)

    class Meta:
        verbose_name = ugettext_lazy("Tag")
        verbose_name_plural = ugettext_lazy("Tags")


class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    publisher = models.CharField(max_length=100)
    tags = TaggableManager(through=UUIDTaggedItem)
    is_loaned = models.BooleanField(default=False)
    loaner_user = models.ForeignKey('users.CustomUser', models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title


class UserBasket(models.Model):
    basket_id = models.UUIDField(primary_key=True, default=uuid.uuid4(), unique=True)
    user_id = models.ForeignKey('users.CustomUser', models.SET_NULL, null=True)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.books
