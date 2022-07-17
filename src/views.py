from audioop import reverse
import genericpath
from src import settings
from django.contrib.auth import authenticate
from django.http.response import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import redirect, render, HttpResponse
from accounts.models import CustomUser
from django.views import generic
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout

from src.forms import CustomSignupForm

def index(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    return render(request, 'index.html')

# class LoginView(TemplateView):

#   template_name = 'registration/login.html'

#   def post(self, request, **kwargs):

#     username = request.POST.get('username', False)
#     password = request.POST.get('password', False)
#     user = authenticate(username=username, password=password)
#     if user is not None and user.is_active:
#         login(request, user)
#         return HttpResponseRedirect( settings.LOGIN_REDIRECT_URL )

#     return render(request, self.template_name)


def loginUser(request):
    print(request.method)
    if request.method == 'POST':
        print(request.POST)
        username = request.POST.get('username', False) 
        password = request.POST.get('password', False)
        user = authenticate(username=username, password=password)
        login(request, user)
        return HttpResponseRedirect(reverse_lazy('index'))
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
