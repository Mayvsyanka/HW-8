from mongoengine import Document
from mongoengine.fields import StringField, BooleanField
from connection import connection

class Contacts (Document):

    fullname = StringField()
    email = StringField()
    message = BooleanField(default=False)

