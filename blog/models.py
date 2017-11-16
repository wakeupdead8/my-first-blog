from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title



class Subscriber(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=128, blank=True, null=True, default=None)
    phone = models.CharField(max_length=32, blank=True, null=True, default=None)
    message = models.TextField(blank=True, null=True, default=None)

    def __str__(self):
        return "User %s %s" % (self.name, self.email,)

    class Meta:
        verbose_name = 'MySubscriber'
        verbose_name_plural = 'A lot of Subscribers'