from traitlets import This
from twilio.rest import Client


class ManageApi:

    phone =''
    
    def send_message( phonenumber):  # Ensure self parameter for instance method
        account_sid = 'AC1ecafd15aa3fc0a2974c61a972f1453f'
        auth_token = 'dd85c804f8e5c1b59df294c82f823c48'
        client = Client(account_sid, auth_token)
        ManageApi.phone = phonenumber

        verification = client.verify.v2.services('VA30a60815e20f6680b5056162b2fc1926').verifications.create(
            to=phonenumber, channel="sms"
        )

    def verify_otp( phonenumber, otp):  # Ensure self parameter for instance method
        account_sid = 'AC1ecafd15aa3fc0a2974c61a972f1453f'
        auth_token = 'dd85c804f8e5c1b59df294c82f823c48'
        client = Client(account_sid, auth_token)
        otp_check = client.verify.v2.services('VA30a60815e20f6680b5056162b2fc1926').verification_checks.create(
            to=phonenumber, code=otp  # Use self to access instance attribute
        )
        if otp_check.status.lower() == 'approved':
            return True
        else:
            return False