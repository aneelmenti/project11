from django.shortcuts import render
from django.views import View
from .forms import RegForm,LoginForm
from .models import Reg
from django.http import HttpResponse
# Create your views here.
class Home(View):
    def get(self,request):
        return render(request,'home.html')
class RegInput(View):
    def get(self,request):
        r_f=RegForm()
        con_dict={'regform':r_f}
        return render(request,'reginput.html',context=con_dict)
class LoginInput(View):
    def get(self,request):
        l_f=LoginForm()
        con_dict={'loginform':l_f}
        return render(request,'logininput.html',context=con_dict)
class RegView(View):
    def post(self,request):
        rf=RegForm(request.POST)
        if rf.is_valid():
            r=Reg(firstname=rf.cleaned_data["firstname"],
                  lastname=rf.cleaned_data["lastname"],
                  username=rf.cleaned_data['username'],
                  password=rf.cleaned_data['password'],
                  cpassword=rf.cleaned_data['cpassword'],
                  mobno=rf.cleaned_data['mobno'],
                  emailid=rf.cleaned_data['emailid'])
            r.save()
            return HttpResponse("reg successfull")
class LoginView(View):
    def post(self,request):
        lf=LoginForm(request.POST)
        if lf.is_valid():
            user_name=lf.cleaned_data["username"]
            pass_word=lf.cleaned_data["password"]
            r=Reg.objects.get(username=user_name,password=pass_word)
            if r:
                return HttpResponse("login success")
            else:
                return HttpResponse("login failed")


