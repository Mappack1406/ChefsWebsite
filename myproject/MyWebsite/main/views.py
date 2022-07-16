from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect

from .models import Contact_db
from .forms import Contact_form

def home(request):
    return render(request, 'main/index.html')

def contact(request):
    if request.method == 'POST':
            form = Contact_form(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Erfolgreich gesendet!')
                return redirect('home')
    else:
        form = Contact_form()
        context = {
            'form':form
        }
        return render(request, 'main/contact.html', context)