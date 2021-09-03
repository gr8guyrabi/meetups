from django.urls import path
from . import views

# map url to app view
urlpatterns = [  # urlpatterns <- has to be a list name
    # map domain_name.com/meetups/ to response from index function of views.py
    path('meetups/', views.index)
]
