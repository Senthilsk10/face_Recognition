from django.shortcuts import render,redirect
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views import View
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.models import User
from .models import Session,Record


class UserLogin(LoginView):
    success_url = reverse_lazy("home")
 

class Base_view(View):
    def get(self,request):
        sessions = Session.objects.all()
        template_name = 'welcome.html'
        return render(request,template_name,{"sessions":sessions})


def login_redirector(request,*args,**kwargs):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        return redirect('login')


def create_Session(request,*args,**kwargs):
    if request.method == "GET":
        return render(request,'sessionform.html')
    if request.method == 'POST':
        sub = request.POST.get('subject')

        obj = Session.objects.create(subject = sub)
        obj.save()
        redirect_key = obj.key
        print(obj.key)
        #return JsonResponse('ok',safe=False,status=200)
        return redirect('home')
        


def session_view(request,*args,**kwargs):
    key = kwargs.get('pk')

    session = Session.objects.get(key=key)
    result_data = Record.objects.filter(session=session)
    return render(request,'session.html',{'session':session,'result_data':result_data})