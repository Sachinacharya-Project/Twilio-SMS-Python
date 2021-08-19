from credentials import credentials
from twilio.rest import Client

account_sid =   credentials.get('account_sid')
auth_token = credentials.get('auth_token')
client = Client(account_sid, auth_token)

messageIntake = input("Your Message: ")

client.api.account.messages.create(
    to="registered_receiver_number",
    from_=credentials.get('twilio_cell_number'),
    body=messageIntake)
    
input("Press [Enter] to Close")