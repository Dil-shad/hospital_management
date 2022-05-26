
from unicodedata import name
from django.urls import path
from .views import *

urlpatterns = [

    path('', index, name='index'),
    path('docter_reg', docter_reg, name='docter_reg'),
    path('loginView', loginView, name='loginView'),
    path('logout', logout, name='logout'),

    path('Patient_reg', Patient_reg, name='Patient_reg'),

    # ---------------#
    path('admin_dashboard', admin_dashboard, name='admin_dashboard'),
    path('approve_doc/<int:pk>',approve_doc,name='approve_doc'),

    #------dOCTER---#
    path('DocterDashView',DocterDashView, name='DocterDashView'),

    #-----P---_#
    path('phome',phome,name='phome'),
]
