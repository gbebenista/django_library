import uuid
from django.db import models
from taggit.managers import TaggableManager
from taggit.models import GenericUUIDTaggedItemBase, TaggedItemBase, Tag
from django.utils.translation import ugettext_lazy as _
from users.models import CustomUser


class UUIDTaggedItem(GenericUUIDTaggedItemBase, TaggedItemBase):
    tag = models.ForeignKey(Tag, related_name="uuid_tagged_items", on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")


class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    publisher = models.CharField(max_length=100)
    tags = TaggableManager(through=UUIDTaggedItem)


# class BookcaseCart(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
#     book = models.ManyToManyField(Book)
