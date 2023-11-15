from django.shortcuts import render,redirect
from django.contrib import messages
from myuser_app.models import MyUser

def email_change_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        u = request.user
        us = MyUser.objects.filter(username = u.username,email_active = True).first()
        if us:
            print('E postanı Değiştir')
            request.usdata = True

        else:
            print('bişeyok')

        response = get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    return middleware