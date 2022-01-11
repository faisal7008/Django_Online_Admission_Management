from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from home.models import Contact, Application
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth  import authenticate,  login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView
from django.core.mail import EmailMessage

from django.conf import settings
from django.core.mail import send_mail





def send_email(msg, mail_id):
    subject = 'CBIT ADMISSION STATUS'
    message = msg
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [str(mail_id)]
    send_mail( subject, message, email_from, recipient_list )

class UpdatePostView(UpdateView):
    model = Application
    template_name = 'student_status.html'
    fields = ('Application_Status', 'message',)

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def personal_details(request):
    if not request.user.is_authenticated:
        return redirect("/sign_in")
    try:    
        app = Application.objects.get(user=request.user)
        app_id = app.id
        id = 20210000 + app_id
        print(id)     
        return render(request, "personal_details.html",{'application':app,'id':id})
    except:
        return render(request, 'personal_details.html')

def educational_details(request):
    if not request.user.is_authenticated:
        return redirect("/sign_in")
    try:    
        app = Application.objects.get(user=request.user)
        app_id = app.id
        id = 20210000 + app_id
        print(id)     
        return render(request, "educational_details.html",{'application':app,'id':id})
    except:
        return render(request, 'educational_details.html')

def fee_payment(request):
    if not request.user.is_authenticated:
        return redirect("/sign_in")
    try:    
        app = Application.objects.get(user=request.user)
        app_id = app.id
        id = 20210000 + app_id
        print(id)     
        return render(request, "fee_payment.html",{'application':app,'id':id})
    except:
        return render(request, 'fee_payment.html')

def status(request):
    if not request.user.is_authenticated:
        return redirect("/sign_in")
    try:    
        app = Application.objects.get(user=request.user)
        app_id = app.id
        id = 20210000 + app_id
        print(id)     
        return render(request, "status.html",{'application':app,'id':id})
    except:
        return render(request, 'status.html')

def dashboard(request):
    if not request.user.is_authenticated:
        return redirect("/sign_in")
    return render(request, 'dashboard.html')

def payment(request):
    if not request.user.is_authenticated:
        return redirect("/sign_in")
    return render(request, 'payment.html')

def contacts(request):
    if not request.user.is_superuser:
        return redirect("/sign_in")
    #contacts = {'name':name,'email':email,'phone':phone,'desc':desc}
    contacts = Contact.objects.all()
    return render(request, 'contacts.html', {"contacts":contacts})

def allusers(request):
    if not request.user.is_superuser:
        return redirect("/sign_in")
    applications = Application.objects.all()
    return render(request, 'allusers.html', {"applications":applications})

def approved_users(request):
    if not request.user.is_superuser:
        return redirect("/sign_in")
    applications = Application.objects.filter(Application_Status='Approved')
    return render(request, 'approved_users.html', {"applications":applications})

def rejected_users(request):
    if not request.user.is_superuser:
        return redirect("/sign_in")
    applications = Application.objects.filter(Application_Status='Rejected')
    return render(request, 'rejected_users.html', {"applications":applications})

def pending_users(request):
    if not request.user.is_superuser:
        return redirect("/sign_in")
    applications = Application.objects.filter(Application_Status='Pending')
    return render(request, 'pending_users.html', {"applications":applications})

def notifications(request):
    if not request.user.is_authenticated:
        return redirect("/sign_in")
    try:
        application = Application.objects.get(user=request.user)
        if application.Application_Status == "Approved":
            messages.success(request, "Congrats! Your Application has been accepted.")
            return render(request, 'notifications.html')
        if application.Application_Status == "Rejected":
            messages.success(request, "Sorry! Your Application has been rejected.")
            return render(request, 'notifications.html')
        return render(request, 'notifications.html')
    except:
        return render(request, 'notifications.html')

def handle_admin(request):
    if not request.user.is_superuser:
        return redirect("/sign_in")
    users = User.objects.all().count
    approve = Application.objects.filter(Application_Status='Approved').count
    reject = Application.objects.filter(Application_Status='Rejected').count
    pending = Application.objects.filter(Application_Status='Pending').count
    return render(request, "handle_admin.html", {'approve':approve, 'reject':reject, 'pending':pending, 'users':users})

def student_application(request, myid):
    if not request.user.is_superuser:
        return redirect("/sign_in")
    id = 20210000 + myid
    application = Application.objects.filter(id=myid)
    #print(application.id)
    return render(request, "student_application.html", {'application':application[0],'id':id})

def student_status(request, myid):
    if not request.user.is_superuser:
        return redirect("/sign_in")
    application = Application.objects.get(id=myid)
    if request.method == "POST":
        status = request.POST.get('status')
        application.Application_Status = status
        application.save()
        print(myid, status, application.Application_Status)
        messages.success(request, "Application Status is successfully edited!!")
        if application.Application_Status != "Pending":
            if application.Application_Status == "Approved":
                msg = "Hello " + str(application.name).capitalize() + ",\n" + "Congratulations! Your Application has been accepted."
                mail_id = str(application.email)
                send_email(msg, mail_id)
            if application.Application_Status == "Rejected":
                msg = "Hello " + str(application.name).capitalize() + ",\n" + "Sorry! Your Application has been accepted."
                mail_id = str(application.email)
                send_email(msg, mail_id)

        return render(request, "student_status.html", {'id':20210000 + myid,'name':application.name})
    return render(request, "student_status.html",  {'id':20210000 + myid,'name':application.name})

def change_password(request):
    if not request.user.is_authenticated:
        return redirect("/sign_in")
    if request.method=="POST": 
            #print(request.user.username, request.user.password)
            username = request.POST['username'] 
            #old_password = request.POST['password']
            new_password1 = request.POST['password1']
            new_password2 = request.POST['password2']

            if username != request.user.username:
                messages.error(request, "Username is Incorrect")
                return redirect('/change_password')
            
            if new_password1 != new_password2:
                messages.error(request, "Passwords do not match")
                return redirect('/change_password')

            if username == request.user.username:
                #print(request.user.username)        # gets username
                user = User.objects.get(username=username)
                user.set_password(new_password1)
                user.save()
                messages.info(request, 'Your Password has been changed succesfully!')
                return redirect('/sign_in')
            else:
                messages.success(request, 'Incorrect Username!')

    return render(request, 'change_password.html')

def application_form(request):
    if not request.user.is_authenticated:
        return redirect("/sign_in")
    if request.method == "POST":
        course = request.POST.get('course')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        name = first_name + ' ' + last_name
        gender = request.POST.get('gender')
        DOB = request.POST.get('DOB')
        student_profile = request.FILES['student_profile']
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        ssc_score = request.POST.get('ssc_score')
        ssc_memo = request.FILES['ssc_memo']
        ssc_tc = request.FILES['ssc_tc']
        inter_score = request.POST.get('inter_score')
        inter_memo = request.FILES['inter_memo']
        inter_tc = request.FILES['inter_tc']
        eamcet_score = request.POST.get('eamcet_score')
        eamcet_memo = request.FILES['eamcet_memo']
        jee_score = request.POST.get('jee_score')
        jee_memo = request.FILES['jee_memo'] 
        application = Application.objects.create(course=course, name=name, gender=gender, DOB=DOB, student_profile=student_profile, email=email, phone=phone, address=address, ssc_score=ssc_score, ssc_memo=ssc_memo, ssc_tc=ssc_tc, inter_score=inter_score, inter_memo=inter_memo, inter_tc=inter_tc, eamcet_score=eamcet_score, eamcet_memo=eamcet_memo, jee_score=jee_score, jee_memo=jee_memo)
        application.user = request.user
        application.save()
        messages.success(request, 'Your Application has been submitted Successfully!')
    try:    
        app = Application.objects.get(user=request.user)
        app_id = app.id
        id = 20210000 + app_id
        print(id)     
        return render(request, "application_form.html",{'id':id})
    except:
        return render(request, 'application_form.html')

def application_status(request):
    if not request.user.is_authenticated:
        return redirect("/sign_in")
    try:
        application = Application.objects.get(user=request.user)
        myid = application.id
        id = 20210000 + myid
        return render(request, 'application_status.html', {'application':application, 'application_id':id})
    except:
        return render(request, 'application_status.html')   

def register_1(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You are registered successfully!')
    return render(request, 'register_1.html', {'form':form})

def register(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
        if request.method=="POST":   
            username = request.POST['username']
            email = request.POST['email']
            first_name=request.POST['first_name']
            last_name=request.POST['last_name']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
        
            if User.objects.filter(email=email).exists():
                messages.error(request, "Email Already Registered!!")
                return redirect('/register')

            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exist!!")
                return redirect('/register')
        
            if len(username)>20:
                messages.error(request, "Username must be under 20 charcters!!")
                return redirect('/register')
            
            if not username.isalnum():
                messages.error(request, "Username must be Alpha-Numeric!!")
                return redirect('/register')

            if password1 != password2:
                messages.error(request, "Passwords do not match!!")
                return redirect('/register')
            try:
                user = User.objects.create_user(username, email, password1)
                user.first_name = first_name.capitalize()
                user.last_name = last_name.capitalize()
                user.save()
                return redirect('/sign_in')        # render(request, 'sign_in.html') 
            except:
                messages.error(request, "Please Enter neccessary details.")  
                return redirect('/register')
        return render(request, "register.html")

def sign_in(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
        if request.method=="POST":
            username = request.POST['username']
            password = request.POST['password']
            print(str(username), str(password))
            
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                #messages.success(request, "Successfully Logged In")
                return redirect("/")
            else:
                messages.error(request, "Invalid Credentials")
            #return render(request, 'college.html')   
        return render(request, "sign_in.html")

def sign_out(request):
    logout(request)
    #messages.success(request, "You've successfully logged out")
    return redirect("/sign_in")

def contact(request):
    if request.method == "POST":
        global name,email,phone,desc
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        # ssc_memo = request.FILES['ssc_memo']
        desc = request.POST.get('desc')
        # document = Contact.objects.create(name=name, course=course, gender=gender, DOB=DOB, email=email, phone=phone,ssc_memo=ssc_memo, desc=desc, date=datetime.today())           # Very Important
        # document.save()                                     
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
        # contacts = {'name':name,'email':email,'phone':phone,'desc':desc}
        # return render(request, 'contacts.html', contacts)
    return render(request, 'contact.html')