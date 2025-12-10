from django.shortcuts import render, redirect
from django.contrib import messages
from .utils.daraja import lipa_na_mpesa_online

def donate(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        amount = request.POST.get("amount")
        phone = request.POST.get("phone")  # e.g., 2547XXXXXXXX

        account_ref = f"PeaceBridge-{name}"
        transaction_desc = "Donation"

        response = lipa_na_mpesa_online(phone, amount, account_ref, transaction_desc)

        if response.get("ResponseCode") == "0":
            messages.success(request, "STK Push sent! Complete payment on your phone.")
        else:
            messages.error(request, f"Error: {response.get('errorMessage')}")
        return redirect('donate')

    return render(request, "donate.html")
def register_view(request):
    if request.method == 'POST':
        form = userCreation(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})