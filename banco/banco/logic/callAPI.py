from traitlets import This
from twilio.rest import Client


class ManageApi:

    phone =''
    
    def send_message( phonenumber):  # Ensure self parameter for instance method
        account_sid = 'ACbdf30ee3a2080be25b4501d736941cea'
        auth_token = 'ae8136b74199309631d7564bd1d589b0'
        client = Client(account_sid, auth_token)
        ManageApi.phone = phonenumber

        verification = client.verify.v2.services('VA3ebb825e5495dcab90a077038c7ecf9f').verifications.create(
            to=phonenumber, channel="sms"
        )

    def verify_otp( phonenumber, otp):  # Ensure self parameter for instance method
        account_sid = 'ACbdf30ee3a2080be25b4501d736941cea'
        auth_token = 'ae8136b74199309631d7564bd1d589b0'
        client = Client(account_sid, auth_token)
        otp_check = client.verify.v2.services('VA3ebb825e5495dcab90a077038c7ecf9f').verification_checks.create(
            to=phonenumber, code=otp  # Use self to access instance attribute
        )
        if otp_check.status.lower() == 'approved':
            return True
        else:
            return False