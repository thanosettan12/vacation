from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def login(request):
    if request.method == 'POST':
        un = request.POST['username']
        pw = request.POST['password']
        user=auth.authenticate(username=un,password=pw)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')


    else:
        return render(request, 'login2.html')

def logout(request):
    auth.logout(request)
    return redirect('/')


def register(request):
    if request.method == 'POST':
        un = request.POST['username']
        fn = request.POST['first_name']
        ln = request.POST['last_name']
        em = request.POST['email']
        pw = request.POST['password1']
        cpw = request.POST['password2']


        if pw==cpw:
            if User.objects.filter(username=un):
                messages.info(request,"username taken")
                return redirect('register')
            elif User.objects.filter(email=em):
                messages.info(request,'email taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=un, password=pw, first_name=fn, last_name=ln, email=em)
                user.save();
                print("user created")
                return redirect('login')

        else:
            print("password not matching ")
            return redirect('register')
        return redirect('register')

    else:
        return render(request, 'example.html')

