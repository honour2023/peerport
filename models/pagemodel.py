from models.basemodels import *
from peewee import CharField, BooleanField, TextField, DateTimeField,IntegerField

from datetime import datetime

class SignUp(BaseModel):
    name = CharField(40)
    email = CharField(null=False)
    phone_num = CharField(null=True)
    date = DateTimeField(default=datetime.now())
    member_tag=CharField(null=False)

class Contact(BaseModel):
    name = CharField()
    email = CharField()
    phone_num = CharField()
    question = TextField()
    date = DateTimeField(default=datetime.now())