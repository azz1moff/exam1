from django.db.models import Model, CharField, ImageField, EmailField, IntegerField, TextField, ForeignKey, CASCADE


class Job(Model):
    name = CharField(max_length=255)


class Profile(Model):
    full_name = CharField(max_length=255)
    age = IntegerField()
    job = ForeignKey('apps.Job', CASCADE)
    description = TextField
    image = ImageField(upload_to='profile/')
    phone = CharField(max_length=255)
    address = CharField(max_length=255)
    email = EmailField()
