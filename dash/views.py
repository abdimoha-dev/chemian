from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from dashboard.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from .models import Title, About,Service, Doctor, Doctor, P_Appointment,Online_appointments, Service_image, Testimonial

# def login(request):
#     return render(request,'login.html')
    
def index(request):
    main_title = Title.objects.latest('id')
    main_about = About.objects.latest('id')
    services = Service.objects.all()[:3]
    doctors = Doctor.objects.all()[:4]
    service_image = Service_image.objects.latest('id')
    testimonial = Testimonial.objects.all()
    consultations = Online_appointments.objects.all()
    for doctor in doctors:
        print(doctor.doctor_photo)
    
    context = {
            'main_title': main_title,
            'main_about':main_about,
            'services': services,
            'service_image':service_image,
            'doctors' : doctors,
            'testimonial' :testimonial,
            'consultations' : consultations
    }
    return render(request,'index.html', context)

def book_consultation(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        title = request.POST.get('title')
        details = request.POST.get('details')
        try:
            image  = request.FILES['image']
            appt = Online_appointments(full_name=full_name,email=email,title=title,details=details, image= image)
            appt.save()
            
        
    # if request.method == 'POST':
            subject = "welcome to emails"
            message = "Testing This Email"
            recepient = email
            send_mail(subject,
                        message, 
                        'chemianhealth@gmail.com',
                        [recepient],
                        fail_silently= False)
        
            return index(request)
        except Exception:
            appt = Online_appointments(full_name=full_name,email=email,title=title,details=details)
            appt.save()
            return index(request)
            
    else:
        return index(request)
        
@login_required(login_url='/accounts/login/')      
def admin_page(request):
    current_user = request.user
    doctors = Doctor.objects.all()
    appointments = P_Appointment.objects.all()
    consultations = Online_appointments.objects.all()
    context = {
        'doctors' : doctors,
        'current_user' : current_user,
        'appointments' : appointments,
        'consultations' :consultations
    }
    return render(request,'admin_index.html', context)

@login_required(login_url='/accounts/login/') 
def update(request):
    current_user = request.user
    context = {
        'current_user' : current_user
    }
    return render(request,'updates.html', context)

def add_main(request):
    if request.method == 'POST':
        # try:
        main_title = request.POST.get('main_title')
        main_body = request.POST.get('main_body')
        try:
            main_image = request.FILES['main_image']
            main_title = Title(main_title =main_title, main_body = main_body, main_image = main_image)
            main_title.save()   
        except Exception:
            main_title = Title(main_title =main_title, main_body = main_body)
            main_title.save()

        return render(request, 'updates.html')   

    else:
        return render(request, 'updates.html')  
        

def add_about(request):
    if request.method == 'POST':
        about_title = request.POST.get('about_title')
        about_body = request.POST.get('about_body')
        
        main_about = About(about_title = about_title, about_body =about_body)
        main_about.save()
        return render(request, 'updates.html')
    else:
        return render(request, 'updates.html')  
    
def add_services(request):
    if request.method == 'POST':
        service_title = request.POST.get('service_title')
        print(service_title)
        service_description = request.POST.get('service_description')
        
        services = Service(service_title = service_title, service_description= service_description) 
        services.save()
        
        return render(request, 'updates.html')
    
    else:
        return render(request, 'updates.html') 
   
def add_service_image(request):
    if request.method == 'POST':
        try:
            service_image =  request.FILES['service_image']
            svs = Service_image(service_image =service_image)
            svs.save()
            return render(request, 'updates.html')
        except Exception:
            return render(request, 'updates.html')
    
    else:
        return render(request, 'updates.html')
        
        
        
def doctors(request):
    if request.method == 'POST':
        doctor_name = request.POST.get('doctor_name')
        doctor_specialization = request.POST.get('doctor_specialization')
        doctor_details = request.POST.get('doctor_details')
        # doctor_photo = request.POST.get('doctor_photo')
        
        dr = Doctor(doctor_name=doctor_name, doctor_details=doctor_details, doctor_specialization=doctor_specialization, doctor_photo=request.FILES['doctor_photo'])
        dr.save()
        
        return render(request, 'updates.html')
    
    else:
        return render(request, 'updates.html')
    
# Booking physical appointment  
def physical_app(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        date = request.POST.get('date')
        time = request.POST.get('time')
        message =  request.POST.get('message')
        d = date.split("/")
        new_date = d[2]+ "-"+d[1]+"-"+d[0]
        apt = P_Appointment(full_name=full_name,email=email,date=new_date,time=time,message=message)
        apt.save()
        return index(request)
    else:
        return index(request)
    
    
def testimonial(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        title = request.POST.get('title')
        testimonial = request.POST.get('testimonial')
        photo = request.FILES['photo']
        
        tst = Testimonial(name=name, title=title, testimonial= testimonial, photo=photo)
        tst.save()
        
        return render(request, 'updates.html')
    else:
        return render(request, 'updates.html')
    
def pull_doctors(request):
    doctors = Doctor.objects.all()
    
    context = {
        'doctors' : doctors
    }
    
    return render('admin_index.html', context)
    
        