import datetime
from django.shortcuts import render
from .models import Scheme, Genders
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.db.models import Q
from googletrans import Translator
# Create your views here.
from django.utils import timezone
from gTTS.cache import remove_cache
from gtts import gTTS
from django.contrib import messages


def valid_age(age):
    if age in range(1, 19):
        return ("0-18")
    if age in range(19-51):
        return ("18-50")
    else:
        return ("50-125")


def all_schemes_view(request):
    remove_cache()
    all_schemes = Scheme.objects.all().order_by('catagories__catagory')
    context = {"schemes": all_schemes}
    # print(timezone.now())
    return render(request, "all_schemes.html", context)


@login_required(login_url="login")
def user_schemes_view(request):
    current_user = request.user
    if current_user.username == "admin":
        print("hi")
        messages.error(request, "admin can not have a profile")
        return redirect("home")
    # eligible_schemes = Scheme.objects.filter(Q(education='any'|education__contains=current_user.education_class),
    #                                         Q(caste_data="any" | caste_data__contains=current_user.cast_class))
    eligible_schemes = Scheme.objects.filter(
        (Q(genders__gender="any") | Q(genders__gender=current_user.profile.gender)),
        (Q(incomes__income="any") | Q(
            incomes__income=current_user.profile.income_class)),
        (Q(marital_status="any") | Q(marital_status=current_user.profile.marital_status)),
        (Q(age="any") | Q(age=valid_age(current_user.profile.age))),
        (Q(castes__caste="any") | Q(castes__caste=current_user.profile.cast_class)),
        (Q(educations__education="any") | Q(
            educations__education=current_user.profile.education_class))
    )
    context = {"schemes": eligible_schemes, "user": current_user}
    return render(request, "user_schemes.html", context)


def dynamic_scheme_view(request, id):
    remove_cache()
    # translator= Translator(to_lang="Hindi")
    tr = Translator()
    obj = Scheme.objects.get(id=id)
    if (obj.last_date < datetime.date.today()):
        my_string = "expired"
        print(my_string)
    else:
        my_string = "valid"

    # translating to hindi via google_translate library
    hi_data = tr.translate(obj.scheme_info, dest='hi').text
    # translation = translator.translate(obj.scheme_info)
    # print(translation)
    context = {
        "scheme": obj,
        "hi_data": hi_data,
        "validity": my_string,
    }
    return render(request, "dynamic_scheme_new.html", context)


def catagory_scheme_view(request, cat):
    cat_schemes = Scheme.objects.filter(catagories__catagory=cat)
    context = {"schemes": cat_schemes}
    return render(request, "user_schemes.html", context)
