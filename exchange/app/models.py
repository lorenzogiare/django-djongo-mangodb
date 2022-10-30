from email.policy import default
from django.db import models
from djongo.models.fields import ObjectIdField, EmbeddedField
from django.contrib.auth.models import User



class Profile (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    _id = ObjectIdField()
    ips = EmbeddedField()  
    subprofiles = EmbeddedField()  

    def __str__(self):
        return self.user.username

class Order(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)
    price = models.FloatField()
    quantity = models.FloatField()
