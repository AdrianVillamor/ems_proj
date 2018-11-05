from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, ListView

class HomePageView(TemplateView):
    template_name = "home.html"

class EventListView(ListView):
    model = Event
    template_name= "event_list.html"
    context_object_name ="event_list"