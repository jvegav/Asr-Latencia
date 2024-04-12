from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import UserForm
from .logic.user_logic import create_user, get_users

# Create your views here.


def users_list(request):
    users = get_users()
    context = {
        'users_list': users
    }
    return render(request, 'User/users.html', context)

def user_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            create_user(form)
            messages.add_message(request, messages.SUCCESS, 'Successfully created user')
            return HttpResponseRedirect(reverse('userCreate'))
        else:
            print(form.errors)
    else:
        form = UserForm()

    context = {
        'form': form,
    }
    return render(request, 'User/userCreate.html', context)