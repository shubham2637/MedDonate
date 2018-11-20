from django.db import models
from datetime import timedelta,datetime
from .encrption import *
# Create your models here.
class Doner(models.Model):
    name = models.CharField(max_length=64)
    address = models.CharField(max_length=128,unique=True)
    pinCode = models.IntegerField()
    Phone_no = models.IntegerField()
    BirthDate = models.DateField()
    UID = models.IntegerField(unique=True)
    email = models.EmailField(max_length=64)
    username = models.CharField(max_length=16,unique=True)
    #password = models.CharField(max_length=16)
    image = models.ImageField(upload_to='doner')


    def __str__(self):
        return (f"{self.name} {self.username} {self.Phone_no}")

class Collector(models.Model):
    #to store a Image file

    name = models.CharField(max_length=64)
    address = models.CharField(max_length=128)
    pinCode = models.IntegerField()
    Phone_no = models.IntegerField()
    BirthDate = models.DateField()
    UID = models.IntegerField(unique=True)
    email = models.EmailField(max_length=64)
    username = models.CharField(max_length=16,unique=True)
    #password = models.CharField(max_length=16)
    qualification = models.CharField(max_length=64)
    Driving_License = models.CharField(max_length=32)
    Driving_License_image = models.ImageField(upload_to='photos/collector/DL')
    image = models.ImageField(upload_to='collector/image')

    def __str__(self):
         return (f"{self.name} {self.username} {self.Phone_no}")

class Acceptor(models.Model):
    #to store a Image file
    name = models.CharField(max_length=64)
    proprietor = models.CharField(max_length=64)
    license_no = models.CharField(max_length=64)
    address = models.CharField(max_length=128)
    pincode = models.PositiveIntegerField()
    UID = models.IntegerField(unique=True)
    start_time = models.TimeField(auto_now=True)
    end_time = models.TimeField(auto_now=True)
    email = models.EmailField()
    username = models.CharField(max_length=64, unique=True)
    #password = models.CharField(max_length=16)
    Phone_no = models.IntegerField()
    image = models.ImageField(upload_to='acceptor')


    def __str__(self):
        return (f"{self.name} {self.username} {self.Phone_no}")

class vehicle(models.Model):
    type = models.CharField(max_length=32)
    name = models.CharField(max_length=32)
    RC_no =models.CharField(max_length=32)
    registration_no = models.CharField(max_length=16)
    last_servicing = models.DateField()
    fuel_type = models.CharField(max_length=32)
    insurence_no = models.CharField(max_length=32)
    owner_name = models.CharField(max_length=32)
    Date_purchase = models.DateField()
    owner_number = models.IntegerField()


    def __str__(self):
        return (f"{self.type} {self.name}")

class assigned_vehicle(models.Model):
    vehicle_id = models.ForeignKey(vehicle,blank=True,on_delete=models.CASCADE)
    collector_id = models.ForeignKey(Collector,blank=True,on_delete=models.CASCADE)
    vehicle_assigned_time = models.DateTimeField(auto_now=True)
    vehicle_return_time = models.DateTimeField(auto_now=True)
    destination = models.ForeignKey(Doner,to_field='address',blank=True,on_delete=models.CASCADE)
    distance = models.FloatField()

    def __str__(self):
        return(f"{self.vehicle_id} {self.collector_id}")

class medicine(models.Model):
    name = models.CharField(max_length=32)
    mfgdate = models.DateField(auto_now=True)
    expdate = models.DateField(auto_now=True)
    manufacturer = models.CharField(max_length=64)
    tradename = models.CharField(max_length=64)
    composition = models.CharField(max_length=64)
    uses = models.CharField(max_length=64)
    quantity = models.PositiveIntegerField()
    sideeffect = models.CharField(max_length=64)
    saltcomposition = models.CharField(max_length=64)
    dosage = models.CharField(max_length=64)

    def __str__(self):
        return (f"{self.name} {self.tradename}")


class medicine_ledger(models.Model):
    donor_id = models.ForeignKey(Doner,blank=True,on_delete=models.CASCADE)
    collector_id = models.ForeignKey(Collector,blank=True, on_delete=models.CASCADE)
    medicine_id = models.ForeignKey(medicine,blank=True, on_delete=models.CASCADE)
    acceptor_id = models.ForeignKey(Acceptor,blank=True, on_delete=models.CASCADE)
    indate = models.DateTimeField(default=datetime.now(tz=None))
    outdate = models.DateTimeField(default=datetime.now(tz=None))
    medicine_count = models.PositiveIntegerField(default=1)


    def __str__(self):
        return (f"{self.medicine_id} {self.medicine_count} {self.indate} {self.outdate}")


class job(models.Model):
    donor_id = models.ForeignKey(Doner,blank=True,on_delete=models.CASCADE)
    collector_id = models.ForeignKey(Collector,blank=True, on_delete=models.CASCADE)
    acceptor_id = models.ForeignKey(Acceptor,blank=True, on_delete=models.CASCADE)
    medicine_id = models.ForeignKey(medicine,blank=True, on_delete=models.CASCADE)
    vehicle_id = models.ForeignKey(vehicle,blank=True,on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now(tz=None))

    def __str__(self):
        return(f"{self.date} {self.donor_id} {self.collector_id} {self.acceptor_id} {self.medicine_id} {self.vehicle_id}")
