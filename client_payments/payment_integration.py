import requests

# Constants
PAYSTACK_API_BASE_URL = 'https://api.paystack.co'
PAYSTACK_SECRET_KEY = 'sk_live_82902ffc972a41a161dedabcf4a57e7c5b85e9cd'

# Function to create a Paystack transaction
def create_paystack_transaction(amount, email, callback_url):
    headers = {
        'Authorization': f'Bearer {PAYSTACK_SECRET_KEY}',
        'Content-Type': 'application/json',
    }
    payload = {
        'amount': amount * 100,  # Paystack expects the amount in kobo (multiply by 100)
        'email': email,
        'callback_url': callback_url,
    }
    response = requests.post(f'{PAYSTACK_API_BASE_URL}/transaction/initialize', json=payload, headers=headers)
    return response.json()

# Example usage
amount = 1000  # Amount in Naira
email = 'customer@example.com'
callback_url = 'https://yourwebsite.com/payment-callback'  # URL to handle Paystack callback

# Create Paystack transaction
paystack_response = create_paystack_transaction(amount, email, callback_url)
transaction_reference = paystack_response['data']['reference']
payment_url = paystack_response['data']['authorization_url']

# Redirect the user to the Paystack payment page
print(f'Please complete your payment <a href="{payment_url}">here</a>.')
