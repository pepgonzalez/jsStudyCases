from twilio.rest import TwilioRestClient

account_sid = "AC6502c0a8bd91af0a76093a66aab7a6d6" # Your Account SID from www.twilio.com/console
auth_token  = "30a8f8a3cd70c3b98e256e1827dec383"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Hello from Python",
    to="+528110801874",    # Replace with your phone number
    from_="+528141642132") # Replace with your Twilio number

print(message.sid)
