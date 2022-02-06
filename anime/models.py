from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.template.defaultfilters import slugify
from django.dispatch import receiver
from django.db.models.signals import pre_save
# Create your models here.
class AN(models.Model):
    name=models.CharField(max_length=100)
    details=models.TextField()
    jonra=models.CharField(max_length=100,default="")
    slug=models.SlugField(default='',null=True,blank=True)
    poster=models.TextField()
    viewsNum=models.PositiveIntegerField(default=0)
    movie=models.FileField(default='')
    def __str__(self):
        return self.name
    
class Comment(models.Model):
    content=models.TextField()
    user=models.ForeignKey(User , on_delete=models.DO_NOTHING)
    anime=models.ForeignKey(AN , on_delete=models.DO_NOTHING)
    time=models.DateTimeField(default=now)

  
class Favourite(models.Model):
    anime=models.ManyToManyField(AN)
    user=models.ForeignKey(User , on_delete=models.DO_NOTHING)
@receiver(pre_save , sender=AN)
def animeSlug(sender , instance , **kwargs):
    instance.slug=slugify(instance.name)
@receiver(pre_save , sender=User)
def animeSlug(sender , instance , **kwargs):
    if Favourite.objects.filter(user=instance).exists():
        pass
    else:
        fv=Favourite.objects.create(user=instance)
    
