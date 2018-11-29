
from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import *
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User,Group
from django.contrib.auth import login,logout,authenticate
from django.core.files.images import ImageFile
from django.core.files.storage import FileSystemStorage
from datetime import timedelta,datetime


def index(request):
    context= {

    }
    return render(request,"MedicalDonation/homepage.html",context)


def acceptors(request):
    context = {
    "acceptors": Acceptor.objects.all()

    }

    return render(request, "MedicalDonation/acceptor.html",context)


def collectors(request):
    context = {
    "collectors": Collector.objects.all()
    }

    return render(request, "MedicalDonation/collector.html",context)
def donors(request):
    context = {
    "donors": Doner.objects.all()
    }

    return render(request, "MedicalDonation/donor.html",context)

def medicines(request):
    context = {
    "medicines": medicine.objects.all()
    }

    return render(request, "MedicalDonation/medicines.html",context)

def jobs_assigned(request):
    context = {
    "jobs": job.objects.filter(date__gte=datetime.now(tz=None))
    }

    return render(request, "MedicalDonation/job.html",context)

def jobs_completed(request):
    context = {
    "jobs": job.objects.filter(date__lt=datetime.now(tz=None))
    }

    return render(request, "MedicalDonation/job.html",context)


def collector_add(request):
    context = {
    "collectors": Collector.objects.all()
    }

    return render(request, "MedicalDonation/collector-add.html",context)



def donor_add(request):
    context = {
    "donors": Doner.objects.all()
        }

    return render(request, "MedicalDonation/donor1.html",context)


def acceptor_add(request):
    context ={
    "acceptor" : Acceptor.objects.all()
    }
    return render(request, "MedicalDonation/acceptor-add.html",context)
@login_required(redirect_field_name="donor-login")
def medicine_add(request):
    context ={
    "medicines" : medicine.objects.all()
    }
    return render(request, "MedicalDonation/medicine-add.html",context)


def create_Collector(request):
    if request.POST:
            coll = Collector(name=request.POST['name'], address= (request.POST['address']+ request.POST['address3'] + request.POST['address4']), pinCode=request.POST['pincode'], Phone_no=request.POST['phone_no'],BirthDate=request.POST['birth'], UID=request.POST['uid'], email=request.POST['email'],username=request.POST['username'], image=request.FILES['image'],Driving_License_image=request.FILES['Driving_License_image'],qualification=request.POST['qualification'],Driving_License=request.POST['Driving_license'])
            username=request.POST['username']
            image=request.FILES['image']
            Driving_License_image=request.FILES['Driving_License_image']
            fs = FileSystemStorage()
            filename = fs.save(username, image)
            uploaded_file_url = fs.url(filename)
            fs = FileSystemStorage()
            filename = fs.save(username, Driving_License_image)
            uploaded_file_url = fs.url(filename)
            coll.save()
            password=request.POST['password']
            user = User.objects.create_user(username=request.POST['username'],email=request.POST['email'],password=request.POST['password'])
            user.last_name = ' '
            group = Group.objects.get(name="Collector")
            group.user_set.add(user)
            user.save()
            return render(request,"MedicalDonation/homepage.html",context)
    return HttpResponseRedirect(reverse("Add_Collector"))


def create_Doner(request):
    if request.POST:
            don = Doner(name=request.POST['name'], address= (request.POST['address1'] + request.POST['address3']), pinCode=request.POST['pinCode'], Phone_no=request.POST['Phone_no'],BirthDate=request.POST['birth'], UID=request.POST['uid'], email=request.POST['email'],username=request.POST['username'],  image=request.FILES['image'] )
            don.save()
            username=request.POST['username']
            password=request.POST['password']
            image=request.FILES['image']
            fs = FileSystemStorage()
            filename = fs.save(username, image)
            uploaded_file_url = fs.url(filename)
            user = User.objects.create_user(username=request.POST['username'],email=request.POST['email'],password=request.POST['password'])
            user.last_name = ' '
            group = Group.objects.get(name="Donor")
            group.user_set.add(user)
            user.save()
            return render(request,"MedicalDonation/homepage.html",{})
    return HttpResponseRedirect(reverse("add_donor"))



def create_Acceptor(request):
    if request.POST:
            accep = Acceptor(name=request.POST['name'],proprietor=request.POST['proprietor'], license_no=request.POST['license_no'],Phone_no=request.POST['Phone_no'],start_time=request.POST['start_time'],end_time=request.POST['end_time'], address= (request.POST['address1']+ request.POST['address3'] + request.POST['address4']),pincode=request.POST['pinCode'],UID=request.POST['UID'],email=request.POST['email'],username=request.POST['username'],image=request.FILES['License_image'])
            accep.save()
            username=request.POST['username']
            image=request.FILES['License_image']
            password=request.POST['password']
            fs = FileSystemStorage()
            filename = fs.save(username, image)
            uploaded_file_url = fs.url(filename)
            user = User.objects.create_user(username=request.POST['username'],email=request.POST['email'],password=request.POST['password'])
            group = Group.objects.get(name="Acceptor")
            group.user_set.add(user)
            user.save()
            return render(request,"MedicalDonation/homepage.html",{})
    return HttpResponseRedirect(reverse("add_acceptor"))


def create_Medicine(request):
    if request.POST:
        med = medicine(name=request.POST['name'],mfgdate=request.POST['manufacturing_date'],expdate=request.POST['expiry_date'],manufacturer=request.POST['manufacturer'],tradename=request.POST['trade_name'],composition=request.POST['chemical_composition'],uses=request.POST['uses'],quantity=request.POST['quantity'],sideeffect=request.POST['side_effects'],saltcomposition=request.POST['salt_composition'],dosage=request.POST['dosage'])
        med.save()
        return render(request,"MedicalDonation/homepage.html",{})
    return HttpResponseRedirect(reverse("add_medicine"))


def login(request):
    context = {
    "collectors": Collector.objects.all()
    }
    return render(request, "MedicalDonation/login.html",context)
@login_required
def acceptor_dash(request,username):
    context ={
    "acceptor" : Acceptor.objects.filter(username=username),
    "collector":Collector.objects.all()
    }
    return render(request, "MedicalDonation/acceptor_home.html",context)

@login_required
def collector_dash(request,username):
    context ={
    "acceptor" : Acceptor.objects.all(),
    "donor" : Doner.objects.all(),
    "collector":Collector.objects.filter(username=username)
    }
    return render(request, "MedicalDonation/collector_home.html",context)

def donor_dash(request,username):
    context ={
    "donor" : Acceptor.objects.filter(username=username),
    "collector":Collector.objects.all()
    }
    return render(request, "MedicalDonation/donor_home.html",context)

def acceptor_login(request):
     username = request.POST['username']
     password = request.POST['password']
     user = authenticate(request, username=username, password=password)
     if user is not None:
         login(request, user)
         #acceptor_dash(request,username)
     else:
        return render(request, "MedicalDonation/failure.html",{})
