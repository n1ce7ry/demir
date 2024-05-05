from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import RegistrationForm
from .models import Car, Tag
from rental.models import Proposal
import datetime


def home_page(request):
    return render(request, 'main/index.html')


def catalog(request):
    cars = Car.objects.all()
    tags = Tag.objects.all()
    today = datetime.date.today()
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    return render(request, 'main/catalog.html', context={
        'cars': cars,
        'tags': tags,
        'today': today.strftime("%Y-%m-%d"),
        'tomorrow': tomorrow.strftime("%Y-%m-%d"),
    })


def about(request):
    return render(request, 'main/about.html')


def contacts(request):
    return render(request, 'main/contacts.html')


def profile(request):
    proposals = Proposal.objects.filter(user=request.user.id)
    return render(request, 'main/profile.html', context={'proposals': proposals})


def registration(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = form.cleaned_data['login']
            user.first_name = form.cleaned_data['fio'].split(' ')[1]
            user.last_name = form.cleaned_data['fio'].split(' ')[0]
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect("login")
        else:
            return render(
                request,
                "main/registration.html",
                {
                    "form": form,
                },
            )
    else:
        form = RegistrationForm()
        return render(
            request,
            "main/registration.html",
            {
                "form": form,
            },
        )


def user_logout(request):
    logout(request)
    return redirect('home_page')