from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns =[

path("", views.index, name="index"),

path("collector-login", LoginView.as_view(template_name="MedicalDonation/Collector-login.html"), name="Collectorlogin"),

path("acceptor-login", LoginView.as_view(template_name="MedicalDonation/Acceptor-login.html"), name="Acceptorlogin"),

path("donor-login", LoginView.as_view(template_name="MedicalDonation/Donor-login.html"), name="Donorlogin"),

path("logout", LogoutView.as_view, name="logout"),

path("collector", views.collectors, name= "Collector_view"),

path("donor", views.donors, name= "Donor_view"),

path("acceptor", views.acceptors, name= "Acceptor_view"),

path("medicines", views.medicines, name= "Medicine_view"),

path("job",views.jobs, name="job_view"),

path("acceptor-home", views.acceptor_dash, name="acceptorhome"),

path("collector-home", views.collector_dash, name="collectorhome"),

path("donor-home", views.donor_dash, name="donorhome"),


path("add-collector", views.collector_add, name="Add_Collector"),

path("add-donor", views.donor_add, name="add_donor"),

path("add-acceptor", views.acceptor_add, name="add_acceptor"),

path("medicine-add", views.medicine_add, name="add_medicine"),

path("create_Collector", views.create_Collector),

path("create_Doner", views.create_Doner),

path("create_Acceptor", views.create_Acceptor),

path("create_Medicine", views.create_Medicine),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
