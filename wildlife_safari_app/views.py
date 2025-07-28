from .models import Place
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django_daraja.mpesa.core import MpesaClient
from .forms import TouristForm
from .models import Message, Tourist  # Import both models

# Home page
def home_view(request):
    return render(request, 'home.html')

# About page
def about_view(request):
    return render(request, 'about.html')

# Contact page (now saves to database)
def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message_text = request.POST.get('message')
        
        # Save to database
        Message.objects.create(
            name=name,
            email=email,
            message=message_text
        )
        
        messages.success(request, f"Thank you {name}! Your message has been sent.")
        return redirect('contact')  # Redirect to prevent form resubmission
        
    return render(request, 'contact.html')

# Tourist registration with MPESA STK push
def register_view(request):
    if request.method == 'POST':
        form = TouristForm(request.POST)
        if form.is_valid():
            # Save tourist information
            tourist = form.save()
            
            # Process payment
            phone_number = form.cleaned_data.get('phone')
            amount = 1  # for sandbox testing

            account_reference = "WildlifeSafari"
            transaction_desc = "Tour Booking Payment"
            callback_url = "https://f55f416eeb72.ngrok-free.app/api/callback/"

            cl = MpesaClient()
            response = cl.stk_push(
                phone_number,
                amount,
                account_reference,
                transaction_desc,
                callback_url
            )
            print("STK Push response:", response)
            return redirect('payment_success')
    else:
        form = TouristForm()
    return render(request, 'register.html', {'form': form})

# Payment success page
def payment_success_view(request):
    return render(request, 'payment_success.html')

# MPESA Callback handler
@csrf_exempt
def mpesa_callback(request):
    if request.method == 'POST':
        print("MPESA Callback received:")
        print(request.body)  # raw JSON payload from Safaricom
        return JsonResponse({"status": "success"})
    return JsonResponse({"error": "Invalid request"}, status=400)
def places_view(request):
    places = Place.objects.all()
    return render(request, 'places_to_visit.html', {'places': places})
