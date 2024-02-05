from django.db import models
import secrets


subject_choices = [
    ("M3","discrete mathematics"),
    ("computer architecture and organisation","computer architecture and organisation"),
    ("operating system","operating system"),
    ("graphics and multimdeia","graphics and multimdeia"),
    ("computer networking","computer networking"),
    ("python","python"),

]
class Session(models.Model):
    date = models.DateField(auto_now_add=True)
    subject = models.CharField(max_length=45,choices=subject_choices,blank =True,null=True)
    key = models.CharField(max_length=12,default=secrets.token_urlsafe(12), editable=False, unique=True)


class Record(models.Model):
    rollno=models.BigIntegerField(blank=True,null=True)