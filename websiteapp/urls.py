from django.urls import path
from websiteapp import views

urlpatterns = [
    path('login/',views.Login, name='Login'),
    path('register/',views.Register,name='Register'),
    path('',views.home, name='home'),
    path('company/',views.company,name="company"),
    path('service/',views.service,name="service"),
    path('contact/',views.contact,name="contact"),
    path('attendance_form/',views.attendance_form, name='attendance_form'),
    path('view_attendance/', views.view_attendance, name='view_attendance'),
    path('logout/', views.logout_view, name='logout'),
    
]  