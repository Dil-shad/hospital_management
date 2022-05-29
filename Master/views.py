
from multiprocessing import context
from django.contrib.auth.models import User, auth
import os
from django.conf import settings
from datetime import date, datetime
from django.shortcuts import redirect, render
from django.contrib import messages
from requests import post
from .models import *
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
import datetime
from datetime import timedelta
from .forms import *
# Create your views here.

#---------------INDEX----------------#


def index(request):

    var = DoctorModel.objects.all()
    l1 = []
    n = 0

    for x in var:
        var1 = User.objects.filter(id=x.user.id, is_active=True)
        for m in var1:
            xx = DoctorModel.objects.filter(user=m.id)
            for y in xx:
                n = n+1
                l1.append(y)

        context = {
            'obj': l1
        }

    return render(request, 'index.html', context)


def booking_panel_view(request):

    var = DoctorModel.objects.all()
    l1 = []
    for x in var:
        var1 = User.objects.filter(id=x.user.id, is_active=True)
        for m in var1:
            xx = DoctorModel.objects.filter(user=m.id)
            for y in xx:
                l1.append(y)

    context = {
        'docs': l1
    }

    return render(request, 'booking_panel.html', context)


@login_required(login_url='loginView')
def booking_appoinment(request, pk):

    try:
        today = datetime.datetime.today()
        enddate = today+timedelta(days=2)

        s1 = today.strftime("%Y-%m-%d")
        s2 = enddate.strftime("%Y-%m-%d")
        # print('------------------------'+str(s1))

        # print('------------------------'+str(s2))
        var = DoctorModel.objects.get(id=pk)
        fe = PayModel.objects.get(user=var.user.id)

        context = {
            'doc': var,
            'dt': s1,
            'maxdt': s2,
            'usr': request.user,
            'pmdl': fe
        }
        return render(request, 'confirm_booking.html', context)
    except:
        today = datetime.datetime.today()
        enddate = today+timedelta(days=3)
        s1 = today.strftime("%Y-%m-%d")
        s2 = enddate.strftime("%Y-%m-%d")
        # print('------------'+str(enddate))

        var = DoctorModel.objects.get(id=pk)
        context = {
            'doc': var,
            'maxdt': s2,
            'dt': s1,
            'usr': request.user,
        }
        return render(request, 'confirm_booking.html', context)


def appoinment_mdl_save(request, pk):

    var = DoctorModel.objects.get(id=pk)
    docter_id = var.id
    patient_id = request.user
    if request.method == 'POST':
        dt = request.POST['bdate']
        md = AppoinmentModel.objects.filter(visiter=request.user, date=dt)
        md.delete()
        if len(dt) != 0:
            mdl = AppoinmentModel(
                doc=docter_id,
                visiter=patient_id,
                date=dt
            )
            mdl.save()
            # ==========================todo +default img view
            messages.info(request, 'we will sent your token soon..!')
            ''' subject = 'MAIL INCOMING'
    message = 'Dear '+name + \
        '\nYour Account is Approved.\nYou can login now.\nUsername:'+uname + '\nDate:'+dt
    recipient = g.email
    try:
        send_mail(subject, message, settings.EMAIL_HOST_USER, [recipient])
        print('mail_send')
        g.save()
        return redirect('admin_dashboard')
    except:
        raise ConnectionError
        print('-----someting wrong---------------------Check INTERNET-----------------')'''

        else:
            messages.info(request, 'pick a valid date')
            return redirect('booking_appoinment', pk=var.id)

    return redirect('booking_appoinment', pk=var.id)


#-----------UserAuth-----------------#


def docter_reg_view(request):
    var = Docter_dep.objects.all()
    return render(request, 'doc_signup.html', {'dep': var})


def docter_reg(request):
    try:
        if request.method == 'POST':
            fname = request.POST['first_name']
            lname = request.POST['last_name']
            uname = request.POST['username']
            email = request.POST['email']
            pwd = request.POST['password']
            cpwd = request.POST['cpassword']
            #--------------------------------------#
            qualification = request.POST['qualification']
            dep = request.POST['department']
            fdep = Docter_dep.objects.get(id=dep)
            addr = request.POST['addr']
            mobile = request.POST['ph']
            if request.FILES.get('file') is not None:
                image = request.FILES['file']
            else:
                image = "/static/image/default.png"

            if pwd == cpwd:
                if User.objects.filter(username=uname).exists():
                    messages.info(request, 'username already exists...!!')
                    return redirect('docter_reg')
                # elif User.objects.filter(email=email).exists():
                #     messages.info(request, 'email already registerd..!!')
                #     return redirect('docter_reg')
                else:
                    user = User.objects.create_user(
                        first_name=fname,
                        last_name=lname,
                        username=uname,
                        password=pwd,
                        email=email,
                        is_active=False,
                    )
                    user.save()
                    u = User.objects.get(id=user.id)  # for fkey
                    ex = DoctorModel(
                        user=u,
                        qualification=qualification,
                        address=addr,
                        mobile=mobile,
                        department=fdep,
                        image=image,
                    )

                    ex.save()
                    return redirect('docter_reg_view')
            else:
                messages.info(request, 'paswd doesnt match..!!')
                return redirect('docter_reg')
        # return redirect('docter_reg_view')
    except:
        messages.info(request, 'Please Fill The form')
        return redirect('docter_reg_view')


def patient_reg_view(request):
    return render(request, 'p_signup.html')


def patient_reg(request):

    try:
        if request.method == 'POST':
            fname = request.POST['first_name']
            lname = request.POST['last_name']
            uname = request.POST['username']
            email = request.POST['email']
            pwd = request.POST['password']
            cpwd = request.POST['cpassword']
            #-------------------------------#
            ph = request.POST['ph']
            age = request.POST['age']
            gender = request.POST['gen']
            addr = request.POST['addr']
            bloodgroup = request.POST['bgrp']
            case = request.POST['case']
            if request.FILES.get('file') is not None:
                image = request.FILES['file']
            else:
                image = "/static/image/default.png"

            if pwd == cpwd:
                if User.objects.filter(username=uname).exists():
                    messages.info(request, 'username already exists...!!')
                    return redirect('patient_reg_view')
                # elif User.objects.filter(email=email).exists():
                #     messages.info(request, 'email already registerd..!!')
                #     return redirect('patient_reg_view')
                else:
                    user = User.objects.create_user(
                        first_name=fname,
                        last_name=lname,
                        username=uname,
                        password=pwd,
                        email=email,

                    )
                    user.save()
                    u = User.objects.get(id=user.id)  # for fkey
                    x = PatientModel(
                        user=u,
                        phone=ph,
                        age=age,
                        gender=gender,
                        address=addr,
                        bloodgroup=bloodgroup,
                        case=case,
                        image=image,
                    )
                    x.save()
                    return redirect('loginView')
            else:
                messages.info(request, 're-check passwords')
                return redirect('patient_reg_view')
    except:
        messages.info(request, 'Enter all fields')
        return redirect('patient_reg_view')


def loginView(request):
    try:
        if request.method == 'POST':
            uname = request.POST['username']
            pwd = request.POST['password']
            user = auth.authenticate(username=uname, password=pwd)
            if user is not None:
                if user.is_superuser:
                    request.session['uid'] = user.id
                    auth.login(request, user)
                    return redirect('admin_dashboard')
                else:
                    x = PatientModel.objects.filter(user=user.id)
                    # print(len(x))
                    if len(x) > 0:
                        request.session['uid'] = user.id
                        auth.login(request, user)
                        return redirect('/')

                    else:
                        if not user.is_active:
                            messages.info(
                                request, 'account not activated')
                            return redirect('loginView')

                        else:
                            request.session['uid'] = user.id
                            auth.login(request, user)
                            return redirect('DocterDashView')

            else:
                messages.info(
                    request, 'Invalid Username or Password.')
                return redirect('loginView')

        return render(request, 'login.html')
    except:
        # messages.info(
        #     request, 'Invalid Username or Password. Try Again.IN')
        return render(request, 'login.html')


def logout(request):
    request.session['uid'] = ''
    auth.logout(request)
    return redirect('/')


#--------------UserAuth-----------------#

#--------------admin-------------------#


def admin_dashboard(request):

    var = DoctorModel.objects.all()
    l1 = []
    n = 0

    for x in var:
        var1 = User.objects.filter(id=x.user.id, is_active=True)
        for m in var1:
            xx = DoctorModel.objects.filter(user=m.id)
            for y in xx:
                n = n+1
                l1.append(y)

    # print(l1)
    # print(l1)
    # --------#
    Docter_req = User.objects.filter(is_active=False)
    b = Docter_req.count()
    # print(b)
    m1 = ContactModel.objects.all().count()
    context = {
        'doc_req': Docter_req,
        'count_req': b,
        'ACT_DOC': l1,
        'count': m1,
        'act_doc_count': n,

    }
    return render(request, 'dash_admin.html', context)


def approve_doc(request, pk):
    g = User.objects.get(id=pk)
    print(g.email)
    g.is_active = True
    # print('ACTIVATED')

    name = g.first_name
    uname = g.username
    dd = datetime.datetime.now()
    dt = (dd.strftime('%x'))

    #----#
    subject = 'MAIL INCOMING'
    message = 'Dear '+name + \
        '\nYour Account is Approved.\nYou can login now.\nUsername:'+uname + '\nDate:'+dt
    recipient = g.email
    try:
        send_mail(subject, message, settings.EMAIL_HOST_USER, [recipient])
        print('mail_send')
        g.save()
        return redirect('admin_dashboard')
    except:
        raise ConnectionError
        print('-----someting wrong---------------------Check INTERNET-----------------')


def removeDoc(request, pk):
    # print(pk)
    dell = DoctorModel.objects.get(id=pk)
    if dell.image is not None:
        if not dell.image == "/static/image/default.png":
            os.remove(dell.image.path)
        else:
            pass
    dell.user.delete()
    dell.delete()

    return redirect('admin_dashboard')


def doc_detail_view(request, pk):

    x = DoctorModel.objects.get(id=pk)
    try:
        y = PayModel.objects.get(user=x.user.id)
        context = {
            'ii': x,
            'jj': y
        }

        return render(request, 'doc_details.html', context)
    except:

        context = {
            'ii': x

        }
        return render(request, 'doc_details.html', context)


def PayModelUpdt(request, pk):
    if request.method == 'POST':
        print(pk)
        u = User.objects.get(id=pk)
        f = request.POST['fee']
        s = request.POST['salary']

        uid = u
        var = PayModel.objects.filter(user=u.id)
        var.delete()
        print('----------------'+str(var))
        mdl = PayModel(

            user=uid,
            fees=f,
            salary=s,

        )
        mdl.save()
        return redirect('admin_dashboard')


def department_fun(request):

    if request.method == 'POST':
        val = request.POST['depp']
        if len(val) >= 1:
            try:
                mdl = Docter_dep(
                    department=val
                )
                mdl.save()
                return redirect('department_fun')
            except:
                messages.info(request, 'Enter a valid department..!')
                return redirect('department_fun')
        else:
            messages.info(request, 'Enter a valid department..!')
            return redirect('department_fun')
    var = Docter_dep.objects.all()
    context = {
        'obj': var
    }
    return render(request, 'depart.html', context)
#----------doCTER-----------#


def DocterDashView(request):

    # val = request.user
    # print(val.id)
    mdl_doc = DoctorModel.objects.get(user=request.user.id)
    # print(mdl_doc.id)
    mdl = AppoinmentModel.objects.filter(doc=mdl_doc.id)
    l1 = []
    l2 = []

    for l in mdl:

        l1.append(l)
        pmdl = PatientModel.objects.filter(user=l.visiter.id)
        for x in pmdl:
            l2.append(x)
    zipped = zip(l1, l2)
    # print(l1,l2)

    context = {
        'doc': mdl_doc,
        'bookings': zipped,

    }

    return render(request, 'dash_docter.html', context)


def Doc_Remove_Patient(request, pk):
    # print(pk)
    vr = AppoinmentModel.objects.get(id=pk)
    vr.delete()
    return redirect('DocterDashView')


def doc_self_profile(request, pk):
    print(pk)

    #self_doc = request.user
    depp = Docter_dep.objects.all()
    var = DoctorModel.objects.get(user=pk)
    return render(request, 'doc_update_profile.html', {'obj': var, 'depp': depp})


def update_doc_profile(request, pk):
    print(pk)
    try:
        if request.method == 'POST':
            print('-=---------------------'+str(pk))
            mdl = DoctorModel.objects.get(id=pk)
            mdl.user.first_name = request.POST.get('fname')
            mdl.user.email = request.POST.get('mail')
            mdl.address = request.POST.get('addr')
            mdl.mobile = request.POST.get('mobile')
            mdl.qualification = request.POST.get('qualf')

            if request.POST.get('department') is not None:
                dep = request.POST.get('department')
                dep = Docter_dep.objects.get(id=dep)
                mdl.department = dep

            else:
                pass
            if request.FILES.get('file') is not None:
                mdl.image = request.FILES.get('file')
            else:
                pass
            mdl.user.save()

            mdl.department.save()
            mdl.save()
            return redirect('DocterDashView')

    except:
        pass


#-------------------------#
def ContactModelView(request):
    if request.method == 'POST':
        form = ContactModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    form = ContactModelForm()
    return render(request, 'Contactus.html', {'form': form})


def feedback_view_list_fun(request):

    m2 = ContactModel.objects.all()
    context = {

        'cobj': m2,
    }
    return render(request, 'feedbackview.html', context)


def delete_contact_fun(request, pk):
    print(pk)
    mdl = ContactModel.objects.get(id=pk)
    mdl.delete()

    return redirect('admin_dashboard')
