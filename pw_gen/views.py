
from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home_pwd(request):
    return render(request,'pw_gen/home_pwd.html')



def password(request):

    characters=list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('?!"&/()'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))


    length=int(request.GET.get('length',12)) ## 12 is the default
    thepassword=''

    for x in range(length):
        thepassword +=random.choice(characters)

    return render(request,'pw_gen/password.html', {'password':thepassword})
