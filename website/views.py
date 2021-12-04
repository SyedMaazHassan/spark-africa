from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import datetime
from .forms import *
from .models import *
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
import re

def website_home(request):
    causes = Cause.objects.all()[:5]
    events = Event.objects.all()[:5]
    volunteers = Volunteer.objects.filter(is_approved = True)[:5]
    context = {
        'causes': causes,
        'events': events,
        'volunteers': volunteers
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
    context = {
        'event': event,
        'is_registered': False
    }

    if request.user.is_authenticated:
        filter_query = EventRegistration.objects.filter(user = request.user, event = event)
        if filter_query.exists():
            context['is_registered'] = True


    return render(request, 'sadakat/event_details.html', context)


def contact(request):
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thanks for contacting us, we'll get back to you soon!")

    context = {'form': form}
    return render(request, 'sadakat/contact.html', context)


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
    form = VolunteerForm()

    if request.method == 'POST':
        form = VolunteerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Your volunteer request has been submitted!")
            return redirect("volunteer")

    context = {
        'form': form,
        'volunteers': Volunteer.objects.filter(is_approved = True)
    }
    return render(request, 'sadakat/volunteer.html', context)


def subscribe_to_newsletter(request):
    output = {'status': False}
    email = request.GET.get('email')
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
 
    if re.fullmatch(regex, email):
        filter_query = Subscribe.objects.filter(email = email)

        if filter_query.exists():
            output['message'] = "You have already subscribed!"
        else:
            Subscribe.objects.create(
                email=email
            )
            output['message'] = "You have successfully subscribed to our news letter!"

        output['status'] = True
    else:
        output['message'] = "Please enter a valid email address!"

    return JsonResponse(output)

@login_required
def register_to_event(request, pk):
    filter_query = Event.objects.filter(id = pk)
    if filter_query.exists():
        event = filter_query[0]

        filter_query_2 = EventRegistration.objects.filter(user = request.user, event = event)
        if filter_query_2.exists():
            messages.info(request, "You have already registered for this event!")
        else:
            EventRegistration.objects.create(
                user=request.user,
                event=event
            )
            messages.info(request, "Congratulations! you have been registered for this gret event!")
        return redirect("event_details", pk=pk)
    else:
        return redirect("website_home")