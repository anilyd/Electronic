from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Service, Industry, Contact
from .forms import ContactForm

def home(request):
    services = Service.objects.all()
    industries = Industry.objects.all()
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('home')
    else:
        form = ContactForm()
    
    context = {
        'services': services,
        'industries': industries,
        'form': form
    }
    return render(request, 'main/home.html', context)

def service_detail(request, pk):
    service = Service.objects.get(pk=pk)
    return render(request, 'main/service_detail.html', {'service': service})

def industry_detail(request, pk):
    industry = Industry.objects.get(pk=pk)
    return render(request, 'main/industry_detail.html', {'industry': industry})

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'main/contact.html', {'form': form})