from django.shortcuts import render

from .models import Meetup

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
        return render(request, 'meetups/detail.html', {
            'meetup_available': True,
            'meetup': meetup_detail,
        })
    except Exception as e:
        return render(request, 'meetups/detail.html', {
            'meetup_available': False
        })
