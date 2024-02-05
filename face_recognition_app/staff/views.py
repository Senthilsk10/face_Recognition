from django.shortcuts import render,redirect
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Session


class UserLogin(LoginView):
    success_url = reverse_lazy("home")
 

class Base_view(View):
    def get(self,request):
        template_name = 'welcome.html'
        return render(request,template_name)


def login_redirector(request,*args,**kwargs):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        return redirect('login')


def session_create_view(request,*args,**kwargs):
    if request.method == 'POST':
        sub = request.foem('subject')

        obj = Sessio.objects.create(subject = sub)
        obj.save()
        redirect_key = obj.key

        return redirect('')
        