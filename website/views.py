from django.shortcuts import render

from django.shortcuts import render
from django.contrib import messages

from .models import Lead




def website_home(request):
    if request.method == "POST":
        data = request.POST
        email = data['email'].strip()
        if (not email) or (not '@' in email):
            messages.error(request, 'Please enter a valid email address')
            return render(request, 'sadakat/index.html')
        try:
            Lead.objects.create(
                email = data['email'],
            )
            messages.success(request, 'Thank you for your interest. We will update you once we are done.')
            return render(request, 'sadakat/index.html')
        except:
            messages.info(request, 'You are already registered. We will update you once we are done.')
            return render(request, 'sadakat/index.html')

    return render(request, 'sadakat/index.html', {})



def about(request):
    return render(request, 'sadakat/about.html', {})



def blog(request):
    return render(request, 'sadakat/blog.html', {})



def causes(request):
    return render(request, 'sadakat/causes.html', {})


def contact(request):
    return render(request, 'sadakat/contact.html', {})


def donate(request):
    return render(request, 'sadakat/donate.html', {})


def error(request):
    return render(request, 'sadakat/error.html', {})




def event(request):
    return render(request, 'sadakat/event.html', {})



def volunteer(request):
    return render(request, 'sadakat/volunteer.html', {})




