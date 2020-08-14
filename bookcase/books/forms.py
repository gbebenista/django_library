from crispy_forms.bootstrap import PrependedText, AppendedText
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit
from django.forms import ModelForm
from books.models import Book


class CreateBookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['author', 'title', 'publisher', 'tags', ]

    def __init__(self, *args, **kwargs):
        super(CreateBookForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.helper.layout = Layout(Field('author', placeholder="Author"),
                                    Field('title', placeholder="Title"),
                                    Field('publisher', placeholder="Publisher"),
                                    Field('tags', placeholder="Tags"),
                                    Submit('submit', 'Add book', css_class='btn btn-info'),)


class UpdateBookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['author', 'title', 'publisher', 'tags', ]

    def __init__(self, *args, **kwargs):
        super(UpdateBookForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.helper.layout = Layout(Field('author', placeholder="Author"),
                                    Field('title', placeholder="Title"),
                                    Field('publisher', placeholder="Publisher"),
                                    Field('tags', placeholder="Tags"),
                                    Submit('submit', 'Edit book', css_class='btn btn-info'), )
