from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from .forms import FeedbackForm
from .forms import RegistForm
from 
# Create your views here.
def main(request):
    return render(request, "acc/main.html")

def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user:
            login(request,user)
            return redirect("acc:main")
        else:
            return HttpResponse("<script>alert('Login Fail'); history.go(-1);</script>")
    return render(request, "acc/login.html")

def regist(request):
    if request.method == "POST":
        form =  RegistForm(request.POST)

        print(form['email'])
        # print(form.clean())
    form = RegistForm()
    context = {
        'form': form,
    }
    return render(request, "acc/regist.html", context)

class RegistView(FormView):
