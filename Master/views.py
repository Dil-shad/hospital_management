from django.contrib.auth.models import User, auth
from multiprocessing import context
from django.shortcuts import redirect, render
from django.contrib import messages
from .models import *
# Create your views here.

#---------------INDEX----------------#


def index(request):
    return render(request, 'index.html')


def phome(request):
    return render(request, 'p_home.html')

#-----------UserAuth-----------------#


def docter_reg(request):
    if request.method == 'POST':
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        uname = request.POST['username']
        email = request.POST['email']
        pwd = request.POST['password']
        cpwd = request.POST['cpassword']
        #--------------------------------------#
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
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email already registerd..!!')
                return redirect('docter_reg')
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
                    address=addr,
                    mobile=mobile,
                    department=fdep,
                    image=image,
                )

                ex.save()
                return redirect('/')
        else:
            messages.info(request, 'paswd doesnt match..!!')
            return redirect('docter_reg')

    var = Docter_dep.objects.all()
    return render(request, 'doc_signup.html', {'dep': var})


def Patient_reg(request):
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
                return redirect('Patient_reg')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email already registerd..!!')
                return redirect('Patient_reg')
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

    return render(request, 'p_signup.html')


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
                        return redirect('phome')

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


#-----------UserAuth-----------------#

#--------------admin-------------------#


def admin_dashboard(request):

    Docter_req = User.objects.filter(is_active=False)
    b = Docter_req.count()
    # print(b)
    context = {
        'doc_req': Docter_req,
        'count': b
    }
    return render(request, 'dash_admin.html', context)


def approve_doc(request, pk):
    g = User.objects.get(id=pk)
    print(g)
    g.is_active = True
    print('ACTIVATED')
    g.save()

    return redirect('admin_dashboard')
#_----------doCTER-----------#


def DocterDashView(request):
    return render(request, 'dash_docter.html')
