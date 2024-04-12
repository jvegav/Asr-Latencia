from django.shortcuts import render

from .logic.publisher import publish_phone_number

from.logic.callAPI import ManageApi

from usuarios.models import Usuario


def index(request):
    return render(request, 'index.html')

def send_otp(request):
    return render(request, 'sendOtp.html')

def sendSuccess(request):
    if request.method == 'POST':
        lista_usuarios = Usuario.objects.get_queryset()
        esta = False
        phone = request.POST.get('phonenumber')

        for usuario in lista_usuarios:
            if usuario.phone == phone:
                esta= True
        
        if esta==True:
            publish_phone_number(phone)
            return render(request, 'verify.html')
        else:
            return render(request, 'verifyFailed.html')

        
def verify(request):
    return render(request, 'verify.html')

def verifySuccess(request):
    if request.method == 'POST':
        otp_code = request.POST.get('otp')
        phone = request.POST.get('phonenumber')

        result = ManageApi.verify_otp(phonenumber=phone,otp=otp_code)
        
        if result:
            return render(request, 'verifySuccess.html')

def verifyFailed(request):
    return render(request, 'verifyFailed.html')

        


