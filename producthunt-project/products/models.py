from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
    icon = models.ImageField(upload_to='images/')
    url = models.TextField()
    votes_total = models.IntegerField(default=1)
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)

    # Displays the name of the object in the admin page
    def __str__(self):
        return self.title


    def summary(self):
        return self.body[:100] + '...'


    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')


# Vote only once model that is called vote and has 2 foreign keys - product and user
# https://www.udemy.com/course/the-ultimate-beginners-guide-to-django-django-2-python-web-dev-website/learn/lecture/16349436#questions