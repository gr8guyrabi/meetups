from django.shortcuts import render

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
