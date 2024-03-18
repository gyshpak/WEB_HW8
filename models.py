from mongoengine import Document
from mongoengine.fields import (
    DateTimeField,
    ListField,
    StringField,
    ReferenceField,
    BooleanField,
)


class Author(Document):
    fullname = StringField()
    born_date = DateTimeField()
    born_location = StringField()
    description = StringField()


class Quote(Document):
    tags = ListField()
    authors = ReferenceField(Author)
    quotes = StringField()


# For 2 part
class Contact(Document):
    name = StringField(max_length=150)
    completed = BooleanField(default=False)
    email = StringField(max_length=150)
    
