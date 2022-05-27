
from unicodedata import name
from django.urls import path
from .views import *

urlpatterns = [

    path('', index, name='index'),
    path('booking_panel_view', booking_panel_view, name='booking_panel_view'),
    path('booking_appoinment/<int:pk>',booking_appoinment, name='booking_appoinment'),



    #------#
    path('docter_reg_view', docter_reg_view, name='docter_reg_view'),
    path('docter_reg', docter_reg, name='docter_reg'),
    path('loginView', loginView, name='loginView'),
    path('logout', logout, name='logout'),


    path('patient_reg_view', patient_reg_view, name='patient_reg_view'),
    path('patient_reg', patient_reg, name='patient_reg'),

    # ---------------#
    path('admin_dashboard', admin_dashboard, name='admin_dashboard'),
    path('approve_doc/<int:pk>', approve_doc, name='approve_doc'),
    path('removeDoc/<int:pk>', removeDoc, name='removeDoc'),
    path('doc_detail_view/<int:pk>',doc_detail_view,name='doc_detail_view'),
    path('PayModelUpdt/<int:pk>',PayModelUpdt,name='PayModelUpdt'),

    #------dOCTER---#
    path('DocterDashView', DocterDashView, name='DocterDashView'),

    #-----P---_#
    path('phome', phome, name='phome'),
]
