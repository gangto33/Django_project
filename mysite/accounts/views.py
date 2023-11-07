from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

def login(request):
    if request.user.is_authenticated:
        return redirect('/blog/')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)

        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('/blog/')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


def logout(request):
    auth_logout(request)
    return redirect('/blog/')

@login_required
def profile(request):
    return render(request, 'accounts/profile.html')

def signup(request):
    if request.method == 'POST':
        messages.info(request, "회원가입이 완료되었습니다!")
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts/login')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


def delete(request):
    request.user.delete()
    return redirect('/blog/')


@login_required
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/accounts/profile')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)


@login_required
def change_password(request):
    # <GET>
    if request.method != "POST":
        form = PasswordChangeForm(request.user)
        return render(request, 'accounts/change_password.html', {'form':form})

    # <POST>
    form = PasswordChangeForm(request.user, request.POST)
    if form.is_valid():
        user = form.save()
        update_session_auth_hash(request, user)
        messages.success(request, '비밀번호가 정상적으로 변경되었습니다.')
        return redirect('/accounts/profile')
    else:
        messages.error(request, '입력하신 정보가 유효하지 않습니다.')
    return redirect("/accounts/change_password")
