from django.urls import path,include
from . import views

urlpatterns =[

path("", views.index, name="index"),
path('account/', include('django.contrib.auth.urls')),

path("collector", views.collectors, name= "Collector_view"),

path("donor", views.donors, name= "Donor_view"),

path("acceptor", views.acceptors, name= "Acceptor_view"),

path("medicines", views.medicines, name= "Medicine_view"),

path("add-collector", views.collector_add, name="Add_Collector"),

path("add-donor", views.donor_add, name="add_donor"),

path("add-acceptor", views.acceptor_add, name="add_acceptor"),

path("medicine-add", views.medicine_add, name="add_medicine"),

path("create_Collector", views.create_Collector),

path("create_Doner", views.create_Doner),

path("create_Acceptor", views.create_Acceptor),

path("create_Medicine", views.create_Medicine),

path("login", views.login)



]
