from django.shortcuts import render

from .models import Meetup

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
        if request.method == 'GET':
            registration_form = RegistrationForm()
        else:
            registration_form = RegistrationForm(request.POST)
            if registration_form.is_valid():
                participant = registration_form.save()
                meetup_detail.participants.add(participant)

        return render(request, 'meetups/detail.html', {
            'meetup_available': True,
            'meetup': meetup_detail,
            'registration_form': registration_form,
        })
    except Exception as e:
        return render(request, 'meetups/detail.html', {
            'meetup_available': False
        })
