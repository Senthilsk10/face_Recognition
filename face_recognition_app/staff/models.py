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

    def save(self, *args, **kwargs):
        # Generate and set the unique key only if it doesn't exist
        if not self.key:
            self.key = secrets.token_urlsafe(24)
        super().save(*args, **kwargs)

class Record(models.Model):
    session = models.ForeignKey('Session',on_delete=models.CASCADE)
    rollno=models.BigIntegerField(blank=True,null=True)
    timestamp = models.DateTimeField(auto_now_add=True)