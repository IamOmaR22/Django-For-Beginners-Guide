from django.shortcuts import render
import random

def home(request):

    return render(request, 'generator/home.html')


def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):   # uppercase is the name from html input (checkbox name)
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
        
    if request.GET.get('special'):     # special is the name from html input (checkbox name)
        characters.extend(list('~!@#$%^&*().,[]{}|\/-_+'))
    
    if request.GET.get('numbers'):      # numbers is the name from html input (checkbox name)
        characters.extend(list('0123456789'))

    length = int(request.GET.get('length', 12))

    thepassword = ''

    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password':thepassword})



def about(request):

    return render(request, 'generator/about.html')