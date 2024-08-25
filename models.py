from mongoengine import EmbeddedDocument, Document, CASCADE
from mongoengine.fields import EmbeddedDocumentField, ListField, StringField, ReferenceField


class Tag(EmbeddedDocument):
    name = StringField()

class Author(Document):
    fullname = StringField()
    born_date = StringField()
    born_location = StringField()
    description = StringField()

class Quote(Document):
    tags = ListField(EmbeddedDocumentField(Tag))
    author = ReferenceField(Author, reverse_delete_rule=CASCADE)
    quote = StringField()

