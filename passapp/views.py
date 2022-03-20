from django.shortcuts import render
import random, string

# Create your views here.

def passwordgen(request):
    opt = list(range(8,15))
    return render(request, 'passapp/index.html',{'opt':opt})

def yourpass(request):
    # lstop = list(map(chr,range(33,127))) Included everything
    length = int(request.GET.get('length'))
    low = list(string.ascii_lowercase)
    if request.GET.get('uppercase'):
        low.extend(list(string.ascii_uppercase))
    if request.GET.get('numbers'):
        low.extend(list(string.digits))
    if request.GET.get('special'):
        low.extend(list(string.punctuation))

    random.shuffle(low)
    password = random.sample(low,length)
    return render(request, 'passapp/password.html',{'password':''.join(password)})    

def about(request):
    return render(request, 'passapp/about.html')