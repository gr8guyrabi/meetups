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
        meetupDetail = Meetup.objects.get(slug=meetup_slug)

        return render(request, 'meetups/detail.html', {
            'meetup_available': True,
            'meetup_title': meetupDetail.title,
            'meetup_description': meetupDetail.description
        })
    except Exception as e:
        return render(request, 'meetups/detail.html', {
            'meetup_available': False
        })
