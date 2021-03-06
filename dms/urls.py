from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name="login"),
    path('registration/', views.registration, name='registration'),
    path('aadhar/', views.aadhar, name="aadhar"),
    path('pan/', views.pan, name="pan"),
    path('licence/', views.licence, name="licence"),
    path('ration/', views.ration, name="ration"),
    path('voterid/', views.voterid, name="voterid"),
    path('aadhar1/', views.aadhar1, name="aadhar1"),
    path('voterid1/', views.voterid1, name="voterid1"),
    path('pan1/', views.pan1, name="pan1"),
    path('licence1/', views.licence1, name="licence1"),
    path('ration1/', views.ration1, name="ration1"),
    path('logout/', views.logout, name="logout"),
    path('display_aadhar/', views.display_aadhar, name="display_aadhar"),
    path('display_pancard/', views.display_pancard, name="display_pancard"),
    path('display_voterid/', views.display_voterid, name="display_voterid"),
    path('display_ration/', views.display_ration, name="display_ration"),
    path('display_licence/', views.display_licence, name="display_licence"),
    path('adminLogin/', views.adminLogin, name="adminLogin"),
    path('adminSignup/', views.adminSignup, name="adminSignup"),
    path('admin_panel/dashboard', views.dashboard, name="dashboard"),
    path('admin_panel/dashboard/change/<int:user>',
         views.doc_verification, name="doc_verification"),
    path('admin_panel/dashboard/change/aorr', views.aorr, name="aorr"),
    path('aadhar/status/', views.aadhar_query_status, name="aadhar_status"),
]
