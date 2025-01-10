import requests
import os

# ExchangeRate-API details
api_key = os.getenv('API_KEY')
base_url = 'https://v6.exchangerate-api.com/v6'
endpoint = f'{base_url}/{api_key}/latest/USD'

# GroupMe bot details
groupme_bot_id = os.getenv('BOT_ID')
groupme_post_url = 'https://api.groupme.com/v3/bots/post'

def get_exchange_rate():
    response = requests.get(endpoint)
    data = response.json()
    if response.status_code == 200:
        usd_to_ils = data['conversion_rates']['ILS']
        return usd_to_ils
    else:
        print('Error fetching exchange rate:', data['error'])
        return None

def send_message_to_groupme(message):
    payload = {
        'bot_id': groupme_bot_id,
        'text': message
    }
    response = requests.post(groupme_post_url, json=payload)
    if response.status_code == 202:
        print('Message sent successfully!')
    else:
        print('Error sending message:', response.json())

if __name__ == "__main__":
    rate = get_exchange_rate()
    if rate:
        message = f'The current exchange rate from USD to ILS is: {rate:.2f}'
        send_message_to_groupme(message)
