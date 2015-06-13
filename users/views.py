# coding: utf-8
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.core.urlresolvers import reverse
from users.forms import UserCreateForm
from django.shortcuts import HttpResponseRedirect, Http404
from django.contrib.auth import authenticate, login
from users.models import User


def register(request, autologin=True):
    form = UserCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        if autologin:
            username = form.cleaned_data['login']
            password = form.cleaned_data['password2']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.add_message(request, messages.SUCCESS, 'Поздравляем! С регистрацией!')
            return HttpResponseRedirect(
                reverse('users:profile')
            )
        else:
            return HttpResponseRedirect(
                reverse('index')
            )
    return render(request, 'users/register.html', {'form': form})


def profile(request):
    user = User.objects.get(id=request.user.id)
    context = {
        'profile': user,
    }
    return render(request, 'users/profile.html', context)


def any_profile(request, id):
    profile = get_object_or_404(User, id=id)
    context = {
        'profile': profile,
    }
    return render(request, 'users/profile.html', context)
