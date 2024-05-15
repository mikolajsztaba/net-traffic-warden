from twilio.rest import Client

account_sid = ''
auth_token = ''

# Tworzymy klienta Twilio
client = Client(account_sid, auth_token)

def send_sms(to, body):
    try:
        message = client.messages.create(
            to=to,
            from_='+12673949161',
            body=body
        )
        print(message.sid)
    except Exception as e:
        print(str(e))


recipient_number = ''
message_body = ''

send_sms(recipient_number, message_body)