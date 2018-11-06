from django.shortcuts import render

from django.views.generic import CreateView

from .forms import ParticipantCreationForm

class SignUpView(CreateView):
    form_class = ParticipantCreationForm
    template_name = "signup.html"
