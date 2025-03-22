from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import LoginForm, SignUpForm, UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .models import Profile


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
                    success_url = reverse_lazy('profile')
                    return HttpResponseRedirect(success_url)
                else:
                    return HttpResponse('Profilingiz activ emas!')
            else:
                return HttpResponse('Bunday foydalanuvchi mavjud emas!')
    else:
        form = LoginForm()
        context = {
            'form': form,
        }
        return render(request, 'registration/login.html', context)


@login_required
def dashboardView(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    context = {
        'user': user,
        'profile': profile,
    }
    return render(request, 'accounts/user_profile.html', context)



class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'


def signUpView(request):
    if request.method =="POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
        context = {
            'form': form,
        }
        return render(request, 'accounts/signup.html', context)


def user_register(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password1'])
            new_user.save()
            Profile.objects.create(user=new_user)
            context = {
                'user_form': user_form,
            }
            return redirect('signup_done')
        else:
            return HttpResponse("Forma to'g'ri shakllantirilmagan")
    else:
        user_form = UserRegisterForm()
        context = {
            'user_form': user_form,
        }
        return render(request, template_name='accounts/register.html',context = context)

@login_required
def user_edit(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(data=request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(data=request.POST, instance=request.user.profile, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
        else:
            return HttpResponse("Forma to'g'ri shakllantirilmagan")
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
        context = {
            'user_form': user_form,
            'profile_form': profile_form,
        }
    return render(request, 'accounts/profile_edit.html',context)

# def user_login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return redirect('dashboard')
#                 else:
#                     return HttpResponse('Profiligiz aktiv emas.')
#             else:
#                 return HttpResponse('Bunday foydalanuvchi mavjud emas!')
#     else:
#         form = LoginForm()
#         context = {
#             'form': form,
#         }
#         return render(request, 'registration/login.html', context)
#
# def user_register(request):
#     if request.method == 'POST':
#         user_form = UserRegisterForm(request.POST)
#         if user_form.is_valid():
#             new_user = user_form.save(commit=False)
#             new_user.set_password(user_form.cleaned_data['password2'])
#             new_user.save()
#             return render(request, 'accounts/register_done.html', {'new_user': new_user})
#     else:
#         user_form = UserRegister
#         Form()
#         context = {
#             'user_form': user_form,
#         }
#         return render(request, 'accounts/register.html', context)