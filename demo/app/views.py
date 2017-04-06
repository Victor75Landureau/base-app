from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm, WizardForm


def email(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            form.save()
            return redirect('/app/email')
    return render(request, "app/email.html", {'form': form})


def wizard(request):
    print("wizard")
    if request.method == 'POST':
        form = WizardForm(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('app'))
    else:
        form = WizardForm()

    return render(request, 'app/wizard.html', {'form': form})