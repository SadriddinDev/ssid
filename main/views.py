from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
from django.template import loader
import time

def home(request):
    html_message = loader.render_to_string(
        'email.html',
        {
            'user_name': "Sadriddin",
            'subject': 'Thank you from',

        }
    )
    t1 = time.time()
    send_mail(
        'Subject here',
        'Here is the message.',
        'sadriddindev@gmail.com',
        ['sadgiy1999@gmail.com'],
        html_message=html_message,
        fail_silently=False,
    )
    t2 = time.time()
    print(t2 - t1)

    return HttpResponse(request.META['REMOTE_ADDR']+ "   time: " + str(t2 - t1))
