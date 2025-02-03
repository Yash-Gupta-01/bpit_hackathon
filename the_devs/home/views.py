from django.shortcuts import render,get_object_or_404
from .models import Volunteer
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Q
from .models import district_choices

def index(request):
    return render(request,'index/index.html')


@login_required
def become_volunteer(request):
    districts = district_choices
    if request.method == 'POST':
        name = request.POST.get('name')
        phone_no = request.POST.get('phone_no')
        district = request.POST.get('district')
        volunteered_by = request.user
        if Volunteer.objects.filter(phone_no=phone_no).exists() or Volunteer.objects.filter(volunteered_by=volunteered_by).exists():
            messages.success(request, 'Data Need to be unique OR you already are a Volunteer in this account')
            return HttpResponseRedirect(reverse('index:become_volunteer'))
        entry = Volunteer(name=name, phone_no=phone_no, district=district, volunteered_by=volunteered_by)
        entry.save()
        messages.success(request, 'Thanks, now you are a volunteer')
        return HttpResponseRedirect(reverse('index:index'))
    return render(request, 'index/become-volunteer.html', {'districts': districts})

def volunteers(request):
    v_query = Volunteer.objects.filter(is_active=True)
    return render(request, 'index/volunteers.html', {'v_query': v_query})

@login_required
def update_volunteer(request):
    volunteer_update=Volunteer.objects.get(id=request.user.volunteer.id)
    volunteer_update = get_object_or_404(Volunteer, id=request.user.volunteer.id)  # Updated to use get_object_or_404
    # print(volunteer_update)  # Removed print statement
    if request.method == 'POST':
        phone_no=request.POST.get('phone_no')
        is_active=request.POST.get('is_active')
        print(is_active)
        """if Volunteer.objects.filter(phone_no=phone_no).exists():
            messages.success(request,'Phone no. taken')
            return HttpResponseRedirect(reverse('index:update_volunteer'))"""
        volunteer_update.phone_no=phone_no
        volunteer_update.is_active=is_active
        volunteer_update.save()
        messages.success(request,'Updated!')
        return HttpResponseRedirect(reverse('index:index'))
    return render(request,'index/update-volunteer.html',{'volunteer_update':volunteer_update})

def search(request):
    if request.method == "POST":
        searched=request.POST.get('searched')
        q1=Volunteer.objects.filter(Q(district__startswith=searched) | Q(district__icontains=searched)).filter(is_active=True)
        return render(request,'index/volunteer-searched.html',{'q1':q1,'searched':searched})
    #return render(request,'index/volunteers.html')
    return HttpResponseRedirect(reverse('index:volunteers'))