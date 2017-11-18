from django import forms
from .models import *


class SubscriberForm(forms.ModelForm):

    class Meta:
        model = Subscriber
        exclude = [""]

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)