from django.shortcuts import render

# Create your views here.
from django.core.mail import send_mail
from django.http import HttpResponse

def send_email(request):
    subject = 'Hello, Django Email'
    message = 'This is a test email sent from Django.'
    from_email = 'srutee79@gmail.com'
    recipient_list = ['recipient@example.com']

    send_mail(subject, message, from_email, recipient_list)
    return HttpResponse('Email sent successfully.')
