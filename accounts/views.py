from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Muvaffaqiyatli login qilindi')
                else:
                    return HttpResponse('sizning profilingiz activ emas')
            else:
                return HttpResponse('username or password incorrect')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def dashboardView(request):
    user = request.user
    context = {
        'user': user,
    }
    return render(request, 'accounts/user_profil.html', context)