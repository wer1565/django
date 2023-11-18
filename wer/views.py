from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from wer.models import TestModel


def asd(request):
    return render(request, 'sasha.html', {'name': 'Александр'})
def das(request):
    return render(request, 'sasha2.html', {'name': 'Александр'})

def reverse(request):

    user_text = request.GET['usertext']
    user_text = user_text[::-1]

    return render(request,'reverse.html', {'usertext' :user_text})




@csrf_exempt
def reg(request):
        sasha = TestModel()
        if request.method == 'POST':
            sasha.email = request.POST['email']
            sasha.password = request.POST['password']
            sasha.save()
            return HttpResponse('Email' + ' ' + sasha.email + ' ' + "успешно зарегистрирован!")
        return render(request, 'forma.html')

def index(request):
    return render (request, 'index.html')


@csrf_exempt
def login(request):
    return render (request, 'login.html')


