from django.urls import path
from . import views

# map url to app view
urlpatterns = [  # urlpatterns <- has to be a list name
    # map domain_name.com/meetups/ to response from index function of views.py
    path('', views.index, name='all-meetups'),
    path('<slug:meetup_slug>/registration-success',
         views.registration_success, name='registration-success'),
    path('<slug:meetup_slug>', views.detail, name='meetup-detail'),
]
