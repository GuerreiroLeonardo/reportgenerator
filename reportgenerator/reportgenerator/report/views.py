from django.shortcuts import render
from .forms import Consult

def consult(request):
    context = {}
    if request.method == 'POST':
        form = Consult(request.POST)
        if form.is_valid():
