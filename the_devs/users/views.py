from .models  import Profile
from django.shortcuts import render,get_object_or_404
from django.http  import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import logout as auth_logout
from .models import Contact
from django.core.mail import send_mail
from ratelimit import limits
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        print(username,email)
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return HttpResponseRedirect(reverse('users:register'))
            elif len(password) <8:
                messages.info(request,'ATLEAST 8 CHARACTER PASSWORD NEEDED')
                return HttpResponseRedirect(reverse('users:register'))
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return HttpResponseRedirect(reverse('users:register'))
            else:
                entry=User.objects.create_user(username=username,email=email,password=password)
                entry.save()
                messages.success(request,'Account Created!')
                return HttpResponseRedirect(reverse('users:login'))
        else:
            messages.info(request,'Password and confirm password didn"t match')
            return HttpResponseRedirect(reverse('users:register'))
    return render(request,'users/signup.html')

FIFTEEN_MINUTES=900
@limits(calls=15, period=FIFTEEN_MINUTES)
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
        send_mail(data['subject'],message, '',['ubunga255@gmail.com'] )
        messages.success(request,'Response Sent!,Thanks for contacting.')
        return HttpResponseRedirect(reverse('index:index'))
    return render(request,'users/contact.html')

def logout(request):
    auth_logout(request)
    messages.success(request,'Logout Successful')
    return HttpResponseRedirect(reverse('index:index'))

def about(request):
    return render(request,'users/about.html')

@login_required
def profile(request,user_id):
    #profile=Profile.objects.get(id=user_id)
    profile=get_object_or_404(Profile,id=user_id)
    return render(request,'users/profile.html',{'profile':profile})

@login_required
def profile_update(request,user_id):
    profile_edit=get_object_or_404(Profile,id=user_id)
    if request.method == 'POST':
        about=request.POST.get('about')
        image=request.POST.get('image')
        profile_edit.about=about
        profile_edit.image=image
        profile_edit.save()
        messages.success(request,'Profile updated Successfully')
        return HttpResponseRedirect(reverse('users:profile',args=[profile_edit.id]))
    return render(request,'users/profile-update.html',{'profile_edit':profile_edit})