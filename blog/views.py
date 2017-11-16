from django.shortcuts import render
from .forms import SubscriberForm


def index(request):
    return render(request, 'blog/index.html', {})

def about(request):
    return render(request, 'blog/about.html', {})

def post(request):
    return render(request, 'blog/post.html', {})

def contact(request):
    form = SubscriberForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        print (request.POST)
        print (form.cleaned_data)
        data = form.cleaned_data
        print (data["name"])

        new_form = form.save()

    return render(request, 'blog/contact.html', locals())

