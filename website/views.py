from django.shortcuts import render

from django.shortcuts import render
from django.contrib import messages
from datetime import datetime

from .models import Lead, Event, Cause,EventCategory,Contact




def website_home(request):
    causes = Cause.objects.all()[:5]
    events = Event.objects.all()[:5]
    context = {
        'causes': causes,
        'events': events
               }
    if request.method == "POST":
        data = request.POST
        email = data['email'].strip()
        if (not email) or (not '@' in email):
            messages.error(request, 'Please enter a valid email address')
            return render(request, 'sadakat/index.html', context=context)
        try:
            Lead.objects.create(
                email = data['email'],
            )
            messages.success(request, 'Thank you for your interest. We will update you once we are done.')
            return render(request, 'sadakat/index.html', context=context)
        except:
            messages.info(request, 'You are already registered. We will update you once we are done.')
            return render(request, 'sadakat/index.html', context=context)         

    return render(request, 'sadakat/index.html', context=context)



def about(request):
    return render(request, 'sadakat/about.html', {})


def blog(request):
    return render(request, 'sadakat/blog.html', {})


def causes(request):
    causes = Cause.objects.all()
    context = {'causes': causes}
    return render(request, 'sadakat/causes.html', context)


def cause_details(request, pk):
    cause = Cause.objects.get(id=pk)
    context = {'cause': cause}
    return render(request, 'sadakat/cause_details.html', context)


def event_details(request, pk):
    event = Event.objects.get(id=pk)
    context = {'event': event}
    return render(request, 'sadakat/event_details.html', context)


def contact(request):
    context = {}
    template_name = 'sadakat/contact.html',

    if request.method == "POST":
        data = request.POST
        Contact.objects.create(
            name = data['name'],
            email = data['email'],
            phone = data['phone'],
            address = data['address'],
            note = data['address']
        )
        messages.success(request, 'Your message has been sent! Thank You')
        return render(request, template_name, context=context)
    return render(request, template_name, context=context)


def donate(request):
    return render(request, 'sadakat/donate.html', {})


def error(request):
    return render(request, 'sadakat/error.html', {})


def events(request):
    current_date = datetime.now()
    upcoming_events = Event.objects.filter(start_date__gt=current_date)
    current_events = Event.objects.filter(start_date__lte=current_date)

    context = {
        'upcoming_events': upcoming_events,
        'current_events': current_events
    }
    return render(request, 'sadakat/event.html', context)


def volunteer(request):
    return render(request, 'sadakat/volunteer.html', {})

