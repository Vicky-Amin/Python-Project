import doctest
from multiprocessing import context
import re
from telnetlib import DO
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import redirect
from .models import *
import random
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home (request):
    if "email" in request.session:
        uid = User.objects.get(email=request.session['email'])
        if uid.role == "doctor":
            did = Doctor.objects.get(user_id = uid)
            context = {
                "uid" : uid,
                "did" : did,
            }
            return render(request,"myapp/index.html",context)
        else:
            pid = Patient.objects.get(user_id = uid)
            #p_count = Doctor.objects.all().count()
            context={
                'uid' : uid,
                'pid' : pid,
                #'p_count':p_count,
            }
        return render(request, "myapp/p-index.html", context)
    else:
        return redirect("login")

@csrf_exempt
def login(request):
    if "email" in request.session:
        return redirect('home')
    else:
        if request.POST:
            email = request.POST ['email']
            password = request.POST['password']
            print("---> login",email)
            try:
                uid = User.objects.get (email = email)               
                if uid.password == password:
                    if uid.is_verify:
                        request.session["email"] = uid.email                    
                        if uid.role == 'doctor':
                            did = Doctor.objects.get(user_id = uid)
                            context = {
                                "uid" : uid,
                                "did" : did,
                            }
                            return render(request, "myapp\index.html",context)
                        else:
                            pid = Patient.objects.get(user_id = uid)
                            context = {
                                'uid' : uid,
                                'pid' : pid,
                            }
                            return render(request, "myapp/p-index.html", context)
                    else:
                        context={
                            'email' : uid.email
                        }
                        return render(request, "myapp\change_password.html",context)
                else:
                    context = {
                        "e_msg" : "Invalid Password"
                    }
                    return render(request,"myapp/login.html",context)
            except User.DoesNotExist:
                context = {
                    "e_msg" : "Email Address does not Exist "
                }
                return render(request,"myapp/login.html",context)
        else:
            return render(request,"myapp/login.html")

def logout (request):
    if "email" in request.session:
        del  request.session["email"]
        return render(request,"myapp/login.html")
    else:
        return render(request,"myapp/login.html")

def register(request):
    if "email" in request.session:
        return redirect("home")
    else:
        if request.POST:
            p_firstname = request.POST["firstname"]
            p_lastname = request.POST["lastname"]
            p_role = request.POST["role"]
            p_email = request.POST["email"]
            p_contact = request.POST["contact"]
            l1 = ["ade412", "eeda586", "5312edde", "de154e31", "1aede25"]
            password = random.choice(l1)+p_email[3:6]+p_contact[4:7]
            uid = User.objects.create(email=p_email, password=password, role=p_role)
            send_mail("AUTHENTICATION","password :"+str(password),"vicky.amin8686@gmail.com",[p_email])
            
            if p_role == "doctor":
                did = Doctor.objects.create(user_id = uid, firstname=p_firstname, lastname=p_lastname, phone=p_contact)
                if did:
                    print("Successfully Register")
                    context={
                        "s_msg" : "Successfully Register"
                    }
                    return render(request,"myapp/register.html", context)
                else:
                    return render(request,"myapp/register.html")
            else:
                pid = Patient.objects.create(user_id = uid, firstname=p_firstname, lastname=p_lastname, mobile=p_contact)
                if pid:
                    print("Successfully Register")
                    context={
                        "s_msg" : "Successfully Register"
                    }
                    return render(request,"myapp/register.html", context)
                else:
                    return render(request,"myapp/register.html")
        else:
            print("Page just loadded")
            return render(request,"myapp/register.html")

def profile (request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == "doctor":
            did = Doctor.objects.get(user_id = uid)
            context = {
                'uid' : uid,
                'did' : did,
            }
            return render(request,"myapp/profile.html",context)
        else:           
            return render(request,"myapp/profile.html",context)
    else:        
        return redirect("login")

def p_profile (request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == "patient":
            pid = Patient.objects.get(user_id = uid)
            context = {
                'uid' : uid,
                'pid' : pid,
            }
            return render(request,"myapp/p-profile.html",context)
        else:           
            return render(request,"myapp/p-profile.html",context)
    else:        
        return redirect("login")

def doc_profile (request):
    try:
        if request.POST:
            uid = User.objects.get(email = request.session['email'])
            did = Doctor.objects.get(user_id = uid)
            did.firstname = request.POST['firstname']
            did.lastname = request.POST['lastname']
            did.qualification = request.POST['qualification']
            did.specification = request.POST['specification']
            did.availabal_time = request.POST['availabal_time']
            did.experiance = request.POST['experiance']
            did.clinic_name = request.POST['clinic_name']
            did.clinic_city = request.POST['clinic_city']
            did.clinic_address = request.POST['clinic_address']
            did.mobile = request.POST['mobile']
            print("----> mobile number",did.mobile)

            if "pic" in request.FILES:
                did.pic = request.FILES['pic']
                print('----> pic change',did.pic)
            did.save()
            context = {
                    'uid' : uid,
                    'did' : did,
                    "s_msg" : "Successfully Profile Updated",
                }
            return render(request,"myapp/profile.html",context)
        else:
            return redirect("login")
    except:
        return redirect("login")

def patients_profile (request):
    try:
        if request.POST:
            uid = User.objects.get(email = request.session['email'])
            pid = Patient.objects.get(user_id = uid)
            pid.firstname = request.POST['firstname']
            pid.lastname = request.POST['lastname']
            pid.age = request.POST['age']
            pid.gender = request.POST['gender']
            pid.birthdate = request.POST['birthdate']
            pid.bloodgroup = request.POST['bloodgroup']
            pid.height = request.POST['height']
            pid.mobile = request.POST['mobile']
            pid.weight = request.POST['weight']
            pid.patient_address = request.POST['patient_address']
            print("----> mobile number",pid.mobile)

            if "pic" in request.FILES:
                pid.pic = request.FILES['pic']
                print('----> pic change',pid.pic)
            pid.save()
            context = {
                    'uid' : uid,
                    'pid' : pid,
                    "s_msg" : "Successfully Profile Updated",                
                }
            return render(request,"myapp/p-profile.html",context)
        else:
            return redirect("login")
    except:
        return redirect("login")

def doc_pass_change (request):
    if "email" in request.session:
        uid = User.objects.get(email=request.session['email'])
        if uid.role == "doctor":
            did = Doctor.objects.get(user_id = uid)
            currentpassword = request.POST['currentpassword']
            newpassword = request.POST['newpassword']
            if uid.password==currentpassword:
                uid.password = newpassword
                uid.save()
                del request.session['email']
                context = {
                'uid' : uid,
                'did' : did,
                "s_msg" : "Successfully Password Reset",
                
            }
                return render(request,"myapp/login.html",context)
            else:
                e_msg = "Invalid Current password"
                context = {
                    'uid' : uid,
                    'did' : did,
                    "e_msg" : e_msg,

                }
            return render(request,"myapp/profile.html",context)
        else:
            if uid.role == "patient":
                pid = Patient.objects.get(user_id = uid)
                currentpassword = request.POST['currentpassword']
                newpassword = request.POST['newpassword']
                if uid.password==currentpassword:
                    uid.password = newpassword
                    uid.save()
                    del request.session['email']
                    context = {
                    'uid' : uid,
                    'pid' : pid,
                    "s_msg" : "Successfully Password Reset",
                    
                }
                    return render(request,"myapp/login.html",context)
                else:
                    e_msg = "Invalid Current password"
                    context = {
                        'uid' : uid,
                        'did' : did,
                        "e_msg" : e_msg,

                    }
                return render(request,"myapp/profile.html",context)

def all_doctors(request):
    if 'email' in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role=='doctor':
            did = Doctor.objects.get(user_id = uid)
            dall = Doctor.objects.filter().exclude(user_id=uid)
            context = {
                'did' : did,
                'dall' : dall,
                'uid' : uid,
            }
            return render(request,"myapp/all-doctors.html",context)
        else:
            pass

def view_doc(request,pk):
    if 'email' in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role=='doctor':
            did = Doctor.objects.get(user_id = uid)
            did_s = Doctor.objects.get(id=pk)
            context = {
                'did' : did,           
                'uid' : uid,
                'did_s': did_s,
            }
            return render(request,"myapp/doc-spe-profile.html",context)
        else:
           if uid.role=='patient':
            pid = Patient.objects.get(user_id = uid)
            pid_s = Doctor.objects.get(id=pk)
            context = {
                'pid' : pid,           
                'uid' : uid,
                'pid_s': pid_s,
            }
            return render(request,"myapp/doc-spe-profile.html",context)

def change_password(request):
    try:
        if request.POST:
            email = request.POST['email']
            oldpassword = request.POST['oldpassword']
            newpassword = request.POST['newpassword']
            confirmpassword = request.POST['confirmpassword']
            uid = User.objects.get(email=email)
            if uid.password == oldpassword and newpassword and confirmpassword:
                uid.password = newpassword
                uid.is_verify = True
                uid.is_active = True
                uid.save()
                context = {
                    's_msg' : "Successfully Password Reset"
                }
                return render(request,"myapp/login.html",context)
            else:
                context = {
                    'e_msg' : "Invalid Password"
                }
                return render(request,"myapp/login.html",context)
        else:
            return render(request,"myapp/login.html")
    except:
        return render(request,"myapp/login.html")


def p_all_doctors(request):
    if 'email' in request.session:
        uid = User.objects.get(email=request.session['email'])
        pid = Patient.objects.get(user_id=uid)
        dall = Doctor.objects.all()
        context = {
            'uid' : uid,
            'pid' : pid,
            'dall' : dall,
    }
    return render(request,'myapp/p-all-doctors.html',context)


def p_doc_spe_profile(request,pk):
    if 'email' in request.session:
            uid = User.objects.get(email=request.session['email'])
            pid = Patient.objects.get(user_id=uid)
            did_s = Doctor.objects.get(id = pk)
            context = {
                'uid' : uid,
                'pid' : pid,
                'did_s' : did_s,
        }
    return render(request,'myapp/p-doc-spe-profile.html',context)


def p_book_appointment(request,pk):
    if 'email' in request.session:
        uid = User.objects.get(email=request.session['email'])
        pid = Patient.objects.get(user_id=uid)
        did = Doctor.objects.get(id = pk)
        context = {
            'uid' : uid,
            'pid' : pid,
            'did' : did,
        }
    return render(request,'myapp/book-appointment.html',context)

def p_book_a (request):
    if request.POST:
        pid = request.POST['pid']
        did = request.POST['did']
        date = request.POST['date']
        time = request.POST['time']
        reason = request.POST['reason']
        case_status = request.POST['case_status']

        patient_id = Patient.objects.get(id = pid)
        doctor_id = Doctor.objects.get(id = did)
        paid = Appointment.objects.create(patient_id=patient_id, doctor_id=doctor_id, a_date = date, a_time = time, reason = reason, case_status = case_status)

        if paid:
            context = {
                'msg' : "Appointment request sent Successfully "
            }
            return render(request,'myapp/book-appointment.html',context)