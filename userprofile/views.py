from datetime import date
from schemes.models import Scheme
from urllib.request import Request
from django.shortcuts import render, redirect
from .forms import UserForm, ProfileForm, UpdateUserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib.auth import authenticate, login, logout
import sys
from django.db.models import Q
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from django.contrib.auth import get_user_model

from .tokens import account_activation_token
# caution: path[0] is reserved for script path (or '' in REPL)
sys.path.insert(1, '../schemes/')

# from verify_email.email_handler import send_verification_email # email verification


def activateEmail(request, user, to_email):
    messages.success(request, f'Dear <b>{user}</b>, please go to you email <b>{to_email}</b> inbox and click on \
        received activation link to confirm and complete the registration. <b>Note:</b> Check your spam folder.')


def activateEmail(request, user, to_email):
    mail_subject = 'Activate your user account.'
    message = render_to_string('template_activate_account.html', {
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        'protocol': 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        messages.success(
            request, 'go to {to_email} for verification. Note: Check spam folder')
    else:
        messages.error(
            request, f'Problem sending confirmation email to {to_email}, check if you typed it correctly.')


def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        messages.success(
            request, 'Thank you for your email confirmation. Now you can login your account.')
        return redirect('login')
    else:
        messages.error(request, 'Activation link is invalid!')

    return redirect('home')


def register_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)

        if form.is_valid() and profile_form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            activateEmail(request, user, form.cleaned_data.get('email'))
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('login')
    else:
        form = UserForm()
        profile_form = ProfileForm()

    context = {'form': form, 'profile_form': profile_form}
    return render(request, 'register.html', context)


def login_view(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('password')

        user = authenticate(username=username, password=pass1)
        print(user)
        if user is not None:
            print("hi")
            if user.is_active:
                login(request, user)
                context['user'] = user
                return redirect('home')
            else:
                messages.error(request, "Please check your email to verify")
                return redirect('login')

        else:

            messages.error(
                request, "Invalid credentials or email not verified")
            return redirect('login')
    return render(request, "login.html", context)


def home_view(request):
    context = {}
    context["new_schemes"] = Scheme.objects.order_by('-start_date')[:3]
    context["expiry_scheme"] = Scheme.objects.order_by(
        'last_date').filter(last_date__gte=date.today()).first()
    if request.method == 'POST':
        search_key = request.POST.get('search')
        searched_schemes = Scheme.objects.filter(
            Q(name__icontains=search_key) | Q(catagories__catagory__icontains=search_key) | Q(scheme_info__icontains=search_key))
        context['schemes'] = searched_schemes
        return render(request, 'user_schemes.html', context)
    return render(request, 'home.html', context)


def logout_view(request):
    logout(request)
    messages.success(request, "User logged out!")
    return redirect("home")


@login_required(login_url="login")
def profile_view(request):
    current_user = request.user
    context = {}
    context["user"] = current_user
    return render(request, "profile.html", context)


@login_required
def update_profile_view(request):
    if request.method == 'POST':
        print("hasih")
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(
            request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)

    return render(request, 'update_profile.html', {'user_form': user_form, 'profile_form': profile_form})


def about_us_view(request):
    context = {}
    return render(request, "aboutus.html", context)
