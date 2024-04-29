from django.db.models import Model, CharField, ImageField, EmailField


# Create your models here.
class Contact(Model):
    full_name = CharField(max_length=255)
    image = ImageField(upload_to='contact/')
    phone = CharField(max_length=255)
    address = CharField(max_length=255)
    email = EmailField()
