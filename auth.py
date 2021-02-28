from django.shortcuts import render, redirect
from django.http import HttpResponse
import urllib
import json
from random import randint
from kavenegar import KavenegarAPI

from .forms import *

class Signup(View):
    def get(self, request):
        form = SignupForm()
        return render(request, '.html', {'form': form})

    def post(self, request):
        form = SignupForm(request.POST)
        if form.is_valid():
        user.ConfirmedOtp = False
        user.save()
        login(request, user)
        #Generate OTP for request.user
        OTP = randint(100000,999999)
        c = ActivatedCode.objects.create(user=user,
                                         code= OTP
                                         )
        c.save()
        print('code sended to :' + str(user.PhoneNumber) + '- & Code is:'+str(c))
        #usign kaveh negar to send data
        # kavenegar.com
        try:
          api = KavenegarAPI(
          )
          params = {
              'sender': '',
              'receptor': str(user.PhoneNumber),
              'message': str(c.code),
          }
          response = api.sms_send(params)
          print(response)
          print('SENDED CODE : ' + str(c.code))
        except Exception as e:
          print(e)
  
    return redirect('app:view')
  return render(
                   request,
                  'signup.html',
                  {'form':form}
                  )

