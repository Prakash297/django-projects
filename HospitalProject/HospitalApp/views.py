from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from HospitalApp.models import Profile,Doctor,Appointment
from django.contrib.auth.hashers import make_password
from faker import Faker

def landing(request):
    return render(request,'HospitalApp/landing.html')

@login_required(login_url='/userlogin')    #lets say after we run the server if we type 127.0.0.1:8000/appointment then it will take me to that page with out asking user name and password so it is a security concern so to prevent this we add this line, but before that we have to import login_required. after adding this line if some one directly want to access appoinment with login then it will ask for the userlogin
def appointment(request):
    if request.method=='POST':
        user=request.session.get('name1')   #previously in userhome view function we have store the user name in session management as key 'name1' so here we are fetching that username
        patient=request.POST['patientname']    #here patientname is 'name' associated with html input, here in return we will get the value of that html input i.e nothing but end-user input data
        age=request.POST['age']
        gender=request.POST['gender']
        mob=request.POST['mobile']
        city=request.POST['city']
        problem=request.POST['problem']
        fakegen=Faker()
        a=fakegen.random_int(min=65,max=90)
        b=fakegen.random_int(min=65,max=90)
        c=fakegen.random_int(min=65,max=90)
        d=fakegen.random_int(min=100,max=999)
        ref_no=chr(a)+chr(b)+chr(c)+str(d)
        Appointment.objects.create(username=user,ref_no=ref_no,patient_name=patient,age=age,gender=gender,mobile=mob,city=city,problem=problem,status='review')
        return redirect('/userhome')
    return render(request,'HospitalApp/appointmentform.html')

@login_required(login_url='/userlogin')
def manage(request):
    uname=request.session.get('name1')
    applist=Appointment.objects.filter(username__exact=uname,status__iexact='review')
    return render(request,'HospitalApp/manage.html',{'applist1':applist})

@login_required(login_url='/userlogin')
def delete(request,ref):
    record=Appointment.objects.get(ref_no=ref)
    record.delete()
    return redirect('/manage')

@login_required(login_url='/userlogin')
def remove(request,ref):
    app=Appointment.objects.get(ref_no=ref)
    app.delete()
    return redirect('/adminhome')

@login_required(login_url='/userlogin')
def edit(request,ref):       #while the request will come to edit function the with that request a value will also come which we will gona store in ref
    record=Appointment.objects.get(ref_no=ref)
    if request.method=='POST':
        record.patient_name=request.POST.get('patientname')
        record.age=request.POST.get('age')
        record.gender=request.POST.get('gender')
        record.mobile=request.POST.get('mobile')
        record.city=request.POST.get('city')
        record.problem=request.POST.get('problem')
        record.save()
        return redirect('/userhome')
    my_dict={'pname':record.patient_name,'age':record.age,'gender':record.gender,'mobile':int(record.mobile),'city':record.city,'problem':record.problem}
    return render(request,'HospitalApp/edit.html',context=my_dict)


@login_required(login_url='/adminlogin')
def adminhome(request):
    applist=Appointment.objects.filter(status__iexact='review')
    return render(request,'HospitalApp/ahome.html',{'applist2':applist})

@login_required(login_url='/adminlogin')
def accept(request,ref):
    app=Appointment.objects.get(ref_no=ref)
    app.status='accept'
    app.save()
    return redirect('/adminhome')

@login_required(login_url='/adminlogin')
def acceptedapp(request):
    acceptapp=Appointment.objects.filter(status__iexact='accept')
    return render(request,'HospitalApp/acceptedapp.html',{'acceptapp1':acceptapp})

@login_required(login_url='/adminlogin')
def decline(request,ref):
    app=Appointment.objects.get(ref_no=ref)
    app.status='decline'
    app.save()
    return redirect('/adminhome')

@login_required(login_url='/adminlogin')
def declinedapp(request):
    declineapp=Appointment.objects.filter(status__iexact='decline')
    return render(request,'HospitalApp/declinedapp.html',{'declineapp1':declineapp})


@login_required(login_url='/userlogin')
def status(request):
    uname=request.session.get('name1')
    applist=Appointment.objects.filter(username=uname)
    return render(request,'HospitalApp/status.html',{'applist3':applist})
    


@login_required(login_url='/userlogin')
def userhome(request):
    doc=Doctor.objects.all()
    uname=request.session.get('name1')     #here we are saving username in session management for further use
    return render(request,'HospitalApp/phome.html',{'uname1':uname,'doc1':doc})


def userlogin(request):
    if request.method == 'POST':
        username1 = request.POST['username']
        password1 = request.POST['password']
        user1 = authenticate(request, username=username1, password=password1) #here if username1 and password found in user table then that row will will be return otherwise None will be return
        if user1 is not None:
            profile1=Profile.objects.get(user=user1)    #instead of this you can write this     profile1=Profile.objects.get(user__username=username1),    here in this line we are fetching a profile object  according to the user1
            #here in the above line you can't write     user=username1     because user field in profile table is one to one connection with User table so you have to give a User object to the user field of profile table to get a record in profile table
            if user1 is not None and profile1.bio=='patient':
                
            
                login(request, user1)
                request.session['name1']=username1  #if you write this line before 'login(request,user)' then when a user will signup and then login for first time then in phome.html 'hello NONE' will be shown instead of 'hello username1'     
                return redirect('/userhome') 
            else:
                return render(request,'HospitalApp/userlogin.html')
        else:
            return render(request,'HospitalApp/userlogin.html')
    return render(request,'HospitalAPP/userlogin.html')
    


    


def adminlogin(request):
    if request.method == 'POST':
        username1 = request.POST['username']
        password1 = request.POST['password']
    
        user1 = authenticate(request, username=username1, password=password1)
        if user1 is not None:
            profile1=Profile.objects.get(user=user1)    #instead of this you can write this     profile1=Profile.objects.get(user__username=username1)
            if user1 is not None and profile1.bio=='admin':
                login(request, user1)
                return redirect('/adminhome') 
            else:
                return render(request,'HospitalApp/adminlogin.html')
        else:
            return render(request,'HospitalApp/adminlogin.html')

    return render(request, 'HospitalApp/adminlogin.html')




def signup(request):
    val=request.GET.get('name1')   #in both userlogin.html and adminlogin.html in there sign up anchor tag we have gave name as 'name1'   and by this line we can fetch the value associated with that name, we are doing this because we have to know that the request for signup is coming from which login page   userlogin or adminlogin
    if request.method=='POST':
        fname=request.POST.get('f_name')
        lname=request.POST.get('l_name')
        username=request.POST.get('u_name')
        mail=request.POST.get('mail_name')
        password=request.POST.get('pass_name')
        # Hash the password using Django's make_password function, for this you have to import make_password from django.contrib.auth.hashers
        hash_pass = make_password(password)
        new_user=User.objects.create(first_name=fname,last_name=lname,email=mail,username=username,password=hash_pass)
    
        btnval=request.POST.get('name1')  #in signup button in signup.html we have et name as 'name1' now we are fetching the value associated with that button
    
        if btnval=='usersignup':
            profile1=Profile.objects.create(user=new_user,bio='patient')

        elif btnval=='adminsignup':
            profile1=Profile.objects.create(user=new_user,bio='admin')
        return redirect('/')
    
    return render(request,'HospitalApp/signup.html',{'val1':val})   #now here we are sending the 'val' to the signup.html and assignig this as value in 'signup' button of signup.html

def  log_out(request):
    logout(request)
    return redirect('/')
# Create your views here.
