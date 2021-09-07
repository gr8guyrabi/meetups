from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Meetup, Participant

from .forms import RegistrationForm

# Create your views here.

# Every view is a function to be called.


def index(request):
    meetups = Meetup.objects.all()
    return render(request, 'meetups/index.html', {
        'meetups': meetups
    })


def detail(request, meetup_slug):
    try:
        meetup_detail = Meetup.objects.get(slug=meetup_slug)
        user_email_exists = None
        if request.method == 'GET':
            registration_form = RegistrationForm()
        else:
            registration_form = RegistrationForm(request.POST)
            if registration_form.is_valid():
                user_email = registration_form.cleaned_data['email']
                participant, _ = Participant.objects.get_or_create(
                    email=user_email)  # variable, **was_created** =
                user_email_exists = meetup_detail.participants.filter(
                    email=user_email)
                if not(user_email_exists):
                    meetup_detail.participants.add(participant)
                    return redirect('registration-success', meetup_slug=meetup_slug)
        return render(request, 'meetups/detail.html', {
            'user_email_exists': user_email_exists,
            'meetup_available': True,
            'meetup': meetup_detail,
            'registration_form': registration_form,
        })
    except Exception as e:
        return render(request, 'meetups/detail.html', {
            'meetup_available': False
        })


def registration_success(request, meetup_slug):
    meetup = Meetup.objects.get(slug=meetup_slug)
    return render(request, 'meetups/registration_success.html', {'organizer_email': meetup.organizer_email})
