from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponse
# Create your views here.
def home(request):
        template= loader.get_template('home.html')
        return HttpResponse(template.render())
def actualites(request):
    return render(request, 'actualites.html')
def about(request):
    return render(request, 'about.html')
def docutheque(request):
    return render(request, 'docutheque.html')
def world(request):
    return render(request, 'world.html')  

def bloc1(request):
    return render(request, 'bloc1.html')
def bloc2(request):
    return render(request, 'bloc2.html')  
def bloc3(request):
    return render(request, 'bloc3.html')  
def bloc4(request):
    return render(request, 'bloc4.html')
def bloc5(request):
    return render(request, 'bloc5.html')  
def bloc6(request):
    return render(request, 'bloc6.html')  

def solar(request):
    return render(request, 'solar.html')  
def wind(request):
    return render(request, 'wind.html')  
def fossile(request):
    return render(request, 'fossile.html')  
def renouvelable(request):
    return render(request, 'renouvelable.html')  
def petrole(request):
    return render(request, 'petrole.html')  
def nucleaire(request):
    return render(request, 'nucleaire.html') 
def hydraulique (request):
    return render(request, 'hydraulique.html')
def gaz (request):
    return render(request, 'gaz.html')
def charbon (request):
    return render(request, 'charbon.html')
def dashboard (request):
    return render(request, 'dashboard.html')
def consommation (request):
    return render(request, 'consommation.html')

def payment (request):
    return render(request, 'payment.html')
def confirmation (request):
    return render(request, 'confirmation.html')
def payment1 (request):
    return render(request, 'payment..html')
def confirmation1 (request):
    return render(request, 'confirmation..html')
def paiement(request):
    return render(request, 'paiement.html')
# views.py

from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt



def contact(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        contact_info = request.POST.get('contact')  # Renommé pour éviter la confusion avec 'contact' fonction
        company = request.POST.get('company')
        message = request.POST.get('message')

        send_mail(
            subject=f'Message from {full_name}',  # Sujet de l'email
            message=f'Company: {company}\nContact: {contact_info}\n\nMessage:\n{message}\n\nEmail: {email}\n\nFull_Name: {full_name}',
            from_email=settings.EMAIL_HOST_USER,  # Adresse email de l'expéditeur
            recipient_list=['salouaelhodifi@gmail.com','energytrackmorocco@gmail.com'],  # Liste des destinataires
            fail_silently=False,
        )
        return redirect('success')  # Rediriger vers une URL de succès après l'envoi du mail
    return render(request, 'home.html')  # Afficher la page d'accueil si la méthode n'est pas POST


def success(request):
    return render(request, 'contact_success.html')

def newslater (request):
    return render(request, 'newslater.html')

from django.shortcuts import render, redirect
from myapp import forms 
from django.contrib import messages


@csrf_exempt
def subscribe(request):
    if request.method == 'POST':
        form = forms.EMailForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Vous êtes maintenant abonné à la newsletter.")
            return redirect('newslater')  # Ou votre page de succès
        else:
            messages.error(request, "Une erreur est survenue. Veuillez réessayer.")
    else:
    
        form = forms.EMailForm()
    return render(request, 'newslater.html',{'form': form})  



