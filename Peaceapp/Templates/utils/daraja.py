import requests
import base64
from datetime import datetime
from django.conf import settings

def get_access_token():
    """Get Daraja OAuth token"""
    url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
    response = requests.get(url, auth=(settings.DAR_CONSUMER_KEY, settings.DAR_CONSUMER_SECRET))
    token = response.json().get('access_token')
    return token

def lipa_na_mpesa_online(phone_number, amount, account_reference, transaction_desc):
    token = get_access_token()
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    password = base64.b64encode(f"{settings.DAR_SHORTCODE}{settings.DAR_PASSKEY}{timestamp}".encode()).decode()
    
    payload = {
        "BusinessShortCode": settings.DAR_SHORTCODE,
        "Password": password,
        "Timestamp": timestamp,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": amount,
        "PartyA": phone_number,  # Customer phone
        "PartyB": settings.DAR_SHORTCODE,
        "PhoneNumber": phone_number,
        "CallBackURL": settings.DAR_CALLBACK_URL,
        "AccountReference": account_reference,
        "TransactionDesc": transaction_desc
    }

    url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    return response.json()
