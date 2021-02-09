from django.db import models

# Create your models here.
class Band(models.Model):
    """A model of a rock band."""
    name = models.CharField(max_length=200)
    can_rock = models.BooleanField(default=True)
    image = models.URLField(default='https://dt7v1i9vyp3mf.cloudfront.net/styles/news_large/s3/imagelibrary/Q/QA_2-0812-iEt6DpElf7a6Bfqjbzsp_.4z1MoTRa0n.jpg')
    description = models.CharField(max_length=500,default='')
    def __str__(self):
        return f'{self.name}'

class Member(models.Model):
    """A model of a rock band member."""
    name = models.CharField("Member's name", max_length=200)
    instrument = models.CharField(choices=(
            ('g', "Guitar"),
            ('b', "Bass"),
            ('d', "Drums"),
        ),
        max_length=1
    )
    band = models.ForeignKey("Band",on_delete=models.DO_NOTHING)
    def __str__(self):
        return f'{self.name},{self.instrument}'
