from django.db import models

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    image = models.URLField(default='https://www.talk-recruitment.co.uk/userfiles/TalkRecruitment/WebContent/mood%20lighting.jpg?created=20-09-08-12-19-42"')
    price = models.IntegerField(default=0)

class FAQ(models.Model):
    question = models.CharField(max_length=150)
    answer = models.CharField(max_length=250)
    