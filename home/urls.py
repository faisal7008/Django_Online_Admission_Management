from django.contrib import admin
from django.urls import path
from home import views
from django.conf import settings
from django.conf.urls.static import static 
from home.views import UpdatePostView

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('sign_in/', views.sign_in, name='sign_in'),
    path('sign_out/', views.sign_out, name='sign_out'),
    path('register_1/', views.register_1, name='register_1'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('payment/', views.payment, name='payment'),
    path('notifications/', views.notifications, name='notifications'),
    path('dashboard/personal_details/', views.personal_details, name='personal_details'),
    path('dashboard/educational_details/', views.educational_details, name='educational_details'),
    path('dashboard/fee_payment/', views.fee_payment, name='fee_payment'),
    path('dashboard/status/', views.status, name='status'),
    path('contacts/', views.contacts, name='contacts'),
    path('allusers/', views.allusers, name='allusers'),
    path('approved_users/', views.approved_users, name='approved_users'),
    path('rejected_users/', views.rejected_users, name='rejected_users'),
    path('pending_users/', views.pending_users, name='pending_users'),
    path('handle_admin/', views.handle_admin, name='handle_admin'),
    path('change_password/', views.change_password, name='change_password'),
    path('application_form/', views.application_form, name='application_form'),
    path('application_status/', views.application_status, name='application_status'),
    path("student_application/<int:myid>/", views.student_application, name="student_application"),
    #path("student_status/<int:pk>/", UpdatePostView.as_view, name="student_status"),
    path("student_status/<int:myid>/", views.student_status, name="student_status"),
    path('change_password/', views.change_password, name='change_password'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)       # For storing files