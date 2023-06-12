from django.shortcuts import render

from django.views.generic.list import ListView
from .models import TestModel

class TestUserView(ListView):
    model = TestModel
    template_name = 'base.html'
    context_object_name = 'users'