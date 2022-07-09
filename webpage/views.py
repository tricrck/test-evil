from django.shortcuts import redirect, render, HttpResponseRedirect
from django.conf import settings
from .forms import requestForm
from django.core.mail import send_mail
from webpage.forms import requestForm, PositionForm, Projectform

# Create your views here.
def home(request):
    return render(request, 'index.html')
def aboutus(request):
    return render(request, 'aboutus.html')
def career(request):
    return render(request, 'career.html')
def contactus(request):
    return render(request, 'contactus.html')
def portfolio(request):
    return render(request, 'portfolio.html')
def services(request):
    return render(request, 'services.html')

def contact_project(request):
    form_class = Projectform
    # if request is not post, initialize an empty form
    form = form_class(request.POST or None)
    if request.method == 'POST':
        name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        company_name = request.POST.get('company_name')
        where_did_you_find_us = request.POST.get('where_did_you_find_us')
        budget = request.POST.get('budget')
        website_url = request.POST.get('website_url')
        message = request.POST.get('description')
        file = request.POST.get('file')

        form = Projectform(request.POST)
        if form.is_valid():
            form.save()

        recipient_list = [settings.EMAIL_HOST_USER,]
        subject = 'Nerdware Project contact from ' + str(name) 
        message = message + "\n" + "\n" + "Our budget is " + str(budget)
        email_from = email

        send_mail(subject, message, email_from, recipient_list, fail_silently=False)
        return render(request, 'contactus.html', {'name': name})
    else: 
        return render(request, 'contactus.html', {})

def contact_position(request):
    form_class = PositionForm
    # if request is not post, initialize an empty form
    form = form_class(request.POST or None)
    if request.method == 'POST':
        name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        company_name = request.POST.get('company_name')
        where_did_you_find_us = request.POST.get('where_did_you_find_us')
        applyfor = request.POST.get('applyfor')
        website_url = request.POST.get('website_url')
        message = request.POST.get('description')
        file = request.POST.get('file')

        form = PositionForm(request.POST)
        if form.is_valid():
            form.save()
        
        recipient_list = [settings.EMAIL_HOST_USER,]
        subject = 'Nerdware Project contact from ' + str(name) 
        message = message
        email_from = email

        send_mail(subject, message, email_from, recipient_list, fail_silently=False)
        return render(request, 'contactus.html', {'name': name})
    else: 
        return render(request, 'contactus.html', {})

def contact_say(request):
    form_class = requestForm
    # if request is not post, initialize an empty form
    form = form_class(request.POST or None)
    if request.method == 'POST':
        name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        company = request.POST.get('company_name')
        message = request.POST.get('description')
        recipient_list = [settings.EMAIL_HOST_USER,]
        subject = 'Nerdware Call Back Request from ' + str(name) 
        message = message + "\n" + "\n" + "From The Company " + str(company) + "\n" + "\n" + "My email is " + str(email) + "\n" + "\n" + "My phone number is " + str(phone)
        email_from = email

        send_mail(subject, message, email_from, recipient_list, fail_silently=False)
        return render(request, 'contactus.html', {'name': name})
    else: 
        return render(request, 'contactus.html', {})
def cloudkids(request):
    return render(request, 'Cloud-Kids-Mashinani.html')