from django.contrib.auth import authenticate
from django.http.response import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import render, HttpResponse

from src.forms import CustomSignupForm

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def registration(request):
    context = {}
    if request.method == 'POST':
        form = CustomSignupForm(request.POST)
        if form.is_valid():
            form.save()
            form = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],)
            return HttpResponseRedirect(reverse_lazy('index'))
        else :
            context['errors'] = form.errors
    form = CustomSignupForm()
    context["form"]= form #type: ignore
    return render(request,"signup.html", context=context)

