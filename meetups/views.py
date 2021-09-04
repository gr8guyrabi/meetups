from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Every view is a function to be called.


def index(request):
    meetups = [
        {
            'title': 'A First Meetup',
            'location': 'Kathmandu',
            'slug': 'a-first-meetup'
        },
        {
            'title': 'A Second Meetup',
            'location': 'Pokhara',
            'slug': 'a-second-meetup'
        }
    ]
    return render(request, 'meetups/index.html', {
        'showMeetup': True,
        'meetups': meetups
    })


def detail(request, meetup_slug):
    meetupDetail = {
        'title': 'A First Meetup',
        'description': 'This is a first Meetup!!! '
    }

    return render(request, 'meetups/detail.html', {
        'meetup_title': meetupDetail['title'],
        'meetup_description': meetupDetail['description']
    })
