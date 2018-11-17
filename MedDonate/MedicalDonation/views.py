
from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
# Create your views here.
from .models import *
from django.contrib.auth.models import User,Group
from django.contrib.auth import login,logout,authenticate


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




def collector_add(request):
    context = {
    "collectors": Collector.objects.all()
    }

    return render(request, "MedicalDonation/add-collector.html",context)



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

def medicine_add(request):
    context ={
    "medicines" : medicine.objects.all()
    }
    return render(request, "MedicalDonation/medicine-add.html",context)


def create_Collector(request):
    if request.POST:
            coll = Collector(name=request.POST['name'], address= (request.POST['address1']+ request.POST['address2'] + request.POST['address3']), pinCode=request.POST['pincode'], Phone_no=request.POST['phone_no'],BirthDate=request.POST['birth'], UID=request.POST['uid'], email=request.POST['email'],username=request.POST['username'], password=request.POST['password'], image=request.POST['image'] )
            coll.save()
            user = User.objects.create_user(username=request.POST['username'],email=request.POST['email'],password=request.POST['password'])
            user.last_name = ' '
            group = Group.objects.get(name="Collector")
            group.user_set.add(user)
            user.save()
    return HttpResponseRedirect(reverse("Add_Collector"))


def create_Doner(request):
    if request.POST:
            don = Doner(name=request.POST['name'], address= (request.POST['address1']+ request.POST['address2'] + request.POST['address3']), pinCode=request.POST['pincode'], Phone_no=request.POST['phone_no'],BirthDate=request.POST['birth'], UID=request.POST['uid'], email=request.POST['email'],username=request.POST['username'], password=request.POST['password'], image=request.POST['image'] )
            don.save()
            user = User.objects.create_user(username=request.POST['username'],email=request.POST['email'],password=request.POST['password'])
            user.last_name = ' '
            group = Group.objects.get(name="Donor")
            group.user_set.add(user)
            user.save()
    return HttpResponseRedirect(reverse("add_donor"))


def login(request):
    user = request.POST['username']
    passw = request.POST['password']
    user = authenticate(request, username=user, password=passw)
    if user is not None:
        login(request, user)
        return render(request, "MedicalDonation/index.html",context)

    else:
        # Return an 'invalid login' error message.
        ...

def logout_view(request):
    logout(request)

def create_Acceptor(request):
    if request.POST:
            accep = Acceptor(name=request.POST['name'],proprietor=request.POST['proprietor'], license_no=request.POST['license_no'],Phone_no=request.POST['Phone_no'],start_time=request.POST['start_time'],end_time=request.POST['end_time'], address= (request.POST['address1']+ request.POST['address3'] + request.POST['address4']),pincode=request.POST['pinCode'],UID=request.POST['UID'],email=request.POST['email'],username=request.POST['username'],password=request.POST['password'],image=request.POST['License_image'])
            accep.save()
            user = User.objects.create_user(username=request.POST['username'],email=request.POST['email'],password=request.POST['password'])
            group = Group.objects.get(name="Acceptor")
            group.user_set.add(user)
            user.save()
    return HttpResponseRedirect(reverse("add_acceptor"))


def create_Medicine(request):
    if request.POST:
        med = medicine(name=request.POST['name'],mfgdate=request.POST['manufacturing_date'],expdate=request.POST['expiry_date'],manufacturer=request.POST['manufacturer'],tradename=request.POST['trade_name'],composition=request.POST['chemical_composition'],uses=request.POST['uses'],quantity=request.POST['quantity'],sideeffect=request.POST['side_effects'],saltcomposition=request.POST['salt_composition'],dosage=request.POST['dosage'])
        med.save()
    return HttpResponseRedirect(reverse("add_medicine"))
