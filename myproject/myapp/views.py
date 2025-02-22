from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse

def index(request):
    return render(request, 'index.html')

def portfolio_details(request):
    return render(request, 'portfolio-details.html')

def service_details(request):
    return render(request, 'service-details.html')

def starter_page(request):
    return render(request, 'starter-page.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        send_mail(
            f'New message from {name}',
            f'Email: {email}\n\nMessage: {message}',
            settings.EMAIL_HOST_USER,
            [settings.EMAIL_HOST_USER],  # Send to yourself
            fail_silently=False,
        )
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})