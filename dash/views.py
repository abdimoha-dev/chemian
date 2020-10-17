from django.shortcuts import render
from dashboard.settings import EMAIL_HOST_USER
from django.core.mail import send_mail

def index(request):
    return render(request,'index.html')

def mails(request):
    # if request.method == 'POST':
    subject = "welcome to emails"
    message = "Testing This Email"
    recepient = 'abdymohammed@gmail.com'
    send_mail(subject,
                message, 
                'chemianhealth@gmail.com',
                [recepient],
                fail_silently= False)
        
    return render(request,'index.html')
        