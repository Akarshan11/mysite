from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=30)
    f_name = models.CharField(max_length=50)
    dob = models.DateField(max_length=8)
    mob = models.CharField(max_length=12)
    email = models.EmailField(max_length=70)
    address = models.CharField(max_length=100)
    pic = models.FileField()


    def get_absolute_url(self):
      return reverse("{% url 'tution:home' %}")

