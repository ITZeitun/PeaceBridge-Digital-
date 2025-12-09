from django.shortcuts import render, redirect
from .models import Donation, ContactMessage
from django.db.models import Sum
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages

# Homepage view
def index(request):
    return render(request, 'accounts/index.html')

# Registration view
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the new user
            login(request, user)  # Automatically log the user in
            messages.success(request, f'Welcome {user.username}! Your account was created.')
            return redirect('index')  # Redirect to homepage
    else:
        form = UserCreationForm()  # Empty form for GET request
    return render(request, 'accounts/register.html', {'form': form})

# Donation & contact view
def donate_view(request):
    total = Donation.objects.aggregate(Sum('amount'))['amount__sum'] or 0
    donors = Donation.objects.count()
    latest = Donation.objects.order_by('-created').first()
    latest_amount = latest.amount if latest else 0

    if request.method == "POST":
        # DONATION FORM
        if "phone" in request.POST:
            phone = request.POST.get("phone")
            amount = request.POST.get("amount")
            Donation.objects.create(phone=phone, amount=amount)
            return redirect('donate')

        # CONTACT FORM
        if "email" in request.POST:
            name = request.POST.get("name")
            email = request.POST.get("email")
            message = request.POST.get("message")
            ContactMessage.objects.create(name=name, email=email, message=message)
            return redirect('donate')

    context = {
        "total_donations": total,
        "donor_count": donors,
        "latest_donation": latest_amount,
    }
    return render(request, "donate.html", context)
