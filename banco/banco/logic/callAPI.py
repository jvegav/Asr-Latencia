from traitlets import This
from twilio.rest import Client


class ManageApi:

    phone =''
    
    def send_message( phonenumber):  # Ensure self parameter for instance method
        account_sid = 'AC75aecc0653315a05c12121973623ef5e'
        auth_token = 'b8e4beaf8e7e3ec8919bcf9a724518a7'
        client = Client(account_sid, auth_token)
        ManageApi.phone = phonenumber

        verification = client.verify.v2.services('VA3935003e5710342a24b804ea84c7b5f7').verifications.create(
            to=phonenumber, channel="sms"
        )

    def verify_otp( phonenumber, otp):  # Ensure self parameter for instance method
        account_sid = 'AC75aecc0653315a05c12121973623ef5e'
        auth_token = 'b8e4beaf8e7e3ec8919bcf9a724518a7'
        client = Client(account_sid, auth_token)
        otp_check = client.verify.v2.services('VA3935003e5710342a24b804ea84c7b5f7').verification_checks.create(
            to=phonenumber, code=otp  # Use self to access instance attribute
        )
        if otp_check.status.lower() == 'approved':
            return True
        else:
            return False