
from unicodedata import name
from django.urls import path
from .views import *

urlpatterns = [

    path('', index, name='index'),
    path('booking_panel_view', booking_panel_view, name='booking_panel_view'),
    path('booking_appoinment/<int:pk>',booking_appoinment, name='booking_appoinment'),
    path('appoinment_mdl_save/<int:pk>',appoinment_mdl_save, name='appoinment_mdl_save'),
    path('ContactModelView', ContactModelView, name='ContactModelView'),#createview
    path('feedback_view_list_fun', feedback_view_list_fun,name='feedback_view_list_fun'),#list
    path('delete_contact_fun/<int:pk>',delete_contact_fun, name='delete_contact_fun'),#del



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
    path('doc_detail_view/<int:pk>', doc_detail_view, name='doc_detail_view'),
    path('PayModelUpdt/<int:pk>', PayModelUpdt, name='PayModelUpdt'),
    
     path('department_fun',department_fun,name='department_fun'),

    #------dOCTER---#
    path('DocterDashView', DocterDashView, name='DocterDashView'),
    path('Doc_Remove_Patient/<int:pk>',
         Doc_Remove_Patient, name='Doc_Remove_Patient'),
    path('doc_self_profile/<int:pk>', doc_self_profile, name='doc_self_profile'),
    path('update_doc_profile/<int:pk>',
         update_doc_profile, name='update_doc_profile'),

    #-----P---_#

]
