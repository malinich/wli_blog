import datetime

from marshmallow import validate
from umongo import Document, fields, EmbeddedDocument

from app import MetaBaseTemplate


class Comment(EmbeddedDocument, metaclass=MetaBaseTemplate):
    user = fields.UUIDField(required=True)
    text = fields.StringField(validate=validate.Length(min=3), required=True)
    created = fields.DateTimeField(missing=datetime.datetime.now)


class Areal(EmbeddedDocument, metaclass=MetaBaseTemplate):
    country = fields.StringField(required=True)
    cities = fields.ListField(fields.StringField, missing=list)
    geo = fields.ListField(fields.DictField)


class Blog(Document, metaclass=MetaBaseTemplate):
    __collection__ = 'blog'

    title = fields.StringField(validate=validate.Length(max=128), required=True)
    text = fields.StringField(validate=validate.Length(min=128), required=True)
    user = fields.UUIDField(required=True)
    created = fields.DateTimeField(missing=datetime.datetime.now)
    comments = fields.ListField(fields.EmbeddedField(Comment), missing=list)
    areal = fields.EmbeddedField(Areal, missing=dict)

    class Meta:
        pass
