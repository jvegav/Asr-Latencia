from traitlets import This
from twilio.rest import Client


class ManageApi:

    phone =''
    
    def send_message(self, phonenumber):  # Ensure self parameter for instance method
        account_sid = 'AC75aecc0653315a05c12121973623ef5e'
        auth_token = '63a01eb1b86b82ca3a43189fdb8bd396'
        client = Client(account_sid, auth_token)
        ManageApi.phone = phonenumber

        verification = client.verify.v2.services('VA5cd775f75902274c8e28542444bfb7b0').verifications.create(
            to=phonenumber, channel="sms"
        )

    def verify_otp( phonenumber, otp):  # Ensure self parameter for instance method
        account_sid = 'AC75aecc0653315a05c12121973623ef5e'
        auth_token = '63a01eb1b86b82ca3a43189fdb8bd396'
        client = Client(account_sid, auth_token)
        otp_check = client.verify.v2.services('VA5cd775f75902274c8e28542444bfb7b0').verification_checks.create(
            to=phonenumber, code=otp  # Use self to access instance attribute
        )
        if otp_check.status.lower() == 'approved':
            return True
        else:
            return False