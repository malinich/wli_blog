import datetime

from marshmallow import validate
from umongo import Document, fields, EmbeddedDocument

from app import MetaBaseTemplate


class Comment(EmbeddedDocument, metaclass=MetaBaseTemplate):
    user = fields.UUIDField(required=True)
    text = fields.StringField(validate=validate.Length(min=3), required=True)

    created = fields.DateTimeField(missing=datetime.datetime.now)


class Blog(Document, metaclass=MetaBaseTemplate):
    __collection__ = 'blog'

    title = fields.StringField(validate=validate.Length(max=128), required=True)
    text = fields.StringField(validate=validate.Length(min=128), required=True)
    user = fields.UUIDField(required=True)
    geo = fields.ListField(fields.DictField)
    created = fields.DateTimeField(missing=datetime.datetime.now)
    comments = fields.ListField(fields.EmbeddedField(Comment), missing=list)

    class Meta:
        pass
