from audioop import reverse
import genericpath
from django.contrib.auth import authenticate
from django.http.response import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import render, HttpResponse
from accounts.models import CustomUser
from django.views import generic

from src.forms import CustomSignupForm

def index(request):
    if request.user.is_authenticated:
        return redirect('/login')
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

class Signup(generic.CreateView):
    form_class = CustomSignupForm
    success_url = reverse_lazy("index")
    template_name = "signup.html"


def registration(request):
    errors = ''
    if request.method == 'POST':
        form = CustomSignupForm(request.POST)
        if form.is_valid():
            form.save()
            form = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],)
            return HttpResponseRedirect(reverse_lazy('index'))
        else :
            pass
            
    form = CustomSignupForm()
    return render(request,"signup.html", {'form':form, 'errors' : errors})

# if form.is_valid():
#                 user = form.save(commit=False)
    
#                 user.is_valid = False
#                 user.save()
#                 # Maybe redirect here
#             else:
#                 messages.info(request, 'invalid registration details')
