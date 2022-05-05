from django.core.mail import EmailMessage
from shelve import Shelf
from django.shortcuts import render, redirect
from django.contrib import messages

from . models import Information
from .forms import RegisterForm
from my_app import models
# Create your views here.
def index(request):
    shelf = Information.objects.all()
    return render(request, 'polls/index.html', {'shelf': shelf})
def additionalpage(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            data.pop("password")
            models.Information.objects.create(**data)
            messages.success(request, 'Your account has been created. You can log in now!')    
            return redirect('/admin')
    else:
        form = RegisterForm()

    context = {'form': form}
    return render(request, 'polls/addpage.html', context)

def send_message(request):
    email = EmailMessage(
        'Hello',
        'Text',
        '200103520@stu.sdu.edu.kz',
        ['200103520@stu.sdu.edu.kz'],
        headers={'Message-ID': 'foo'},
    )
    email.attach_file('/Users/nazymgultajrova/Downloads/image.jpg')
    email.send(fail_silently=False)
    return render(request, 'polls/addpage.html')
