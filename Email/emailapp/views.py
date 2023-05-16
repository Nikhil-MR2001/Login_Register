from django.contrib import messages, auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
# def email(request):
#     send_mail("subject of our mail", "message", "Niikhiilmr@gmail.com", ['Niikhiilmr@gmail.com'], fail_silently=False)
#
#     return HttpResponse("Mail Sent")


from django.shortcuts import render


# def form(request):
#     if request.method == 'POST':
#         msg = request.POST.get('msg')
#         subject = request.POST.get('subject')
#         from_value = request.POST.get('from')
#
#         send_mail(subject, msg, from_value, ['appsarun34@gmail.com'], fail_silently=False)
#
#     return render(request, 'forms.html')
#     messages.success(request, "success")


def session(request):
    request.session['sname'] = "Nik"
    return HttpResponse("User Session set")


def getsession(request):
    sname = request.session['sname']
    return HttpResponse('welcome' + sname)


def register(request):
    if request.method == 'POST':
        uname = request.POST['username']
        email = request.POST['email']
        psswrd = request.POST['password']
        cpsswrd = request.POST['confirm-password']
        if psswrd == cpsswrd:
            if User.objects.filter(username=uname).exists():
                messages.info(request, 'username already taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email alredy taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=uname, email=email, password=psswrd)
                user.save()


        else:
            messages.info(request, 'password not matching')
            return redirect('register')
        return redirect('index')

    return render(request, 'register.html')




def login(request):
    if request.method == 'POST':
        username = request.POST['u1']
        password = request.POST['p1']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')

        else:
            messages.info(request, "invalid credential")
            return redirect('login')

    return render(request, "login.html")


def index(request):
    return render(request, 'index.html')