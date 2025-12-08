from django.shortcuts import render, redirect
from .models import Donation, ContactMessage
from django.db.models import Sum

def donate_view(request):
    total = Donation.objects.aggregate(Sum('amount'))['amount__sum'] or 0
    donors = Donation.objects.count()
    latest = Donation.objects.order_by('-created').first()

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
        "latest_donation": latest.amount if latest else "No donations yet",
    }
    return render(request, "donate.html", context)
