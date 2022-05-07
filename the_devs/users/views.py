from django.shortcuts import render
from django.http  import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import logout as auth_logout
from .models import Contact
from django.core.mail import send_mail


def register(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        print(username,email)
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                print('hmm')
                messages.info(request,'Username Taken')
                return HttpResponseRedirect(reverse('users:register'))
            elif len(password) <8:
                print('hmm')
                messages.info(request,'ATLEAST 8 CHARACTER PASSWORD NEEDED')
                return HttpResponseRedirect(reverse('users:register'))
            elif User.objects.filter(email=email).exists():
                print('hmm')
                messages.info(request,'Email Taken')
                return HttpResponseRedirect(reverse('users:register'))
            else:
                print('nice')
                entry=User.objects.create_user(username=username,email=email,password=password)
                entry.save()
                messages.success(request,'Account Created!')
                return HttpResponseRedirect(reverse('users:login'))
        else:
            messages.info(request,'Password and confirm password didn"t match')
            return HttpResponseRedirect(reverse('users:register'))
    return render(request,'users/signup.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject=request.POST.get('subject')
        message = request.POST.get('message')
        entry=Contact(name=name,email=email,subject=subject,message=message)
        entry.save()
        data={
            'name':name,
            'email':email,
            'subject':subject,
            'message':message
        }
        message='''
        New message : {}
        from : {}
        '''.format(data['message'],data['email'])
        send_mail(data['subject'],message, '',['aryanjainak@gmail.com'] )
        messages.success(request,'Response Sent!,Thanks for contacting.')
        return HttpResponseRedirect(reverse('index:index'))
    return render(request,'users/contact.html')

def logout(request):
    auth_logout(request)
    messages.success(request,'Logout Successful')
    return HttpResponseRedirect(reverse('index:index'))

def about(request):
    return render(request,'users/about.html')