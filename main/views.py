from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import RegistrationForm
from .models import Car, Tag


def home_page(request):
    return render(request, 'main/index.html')


def catalog(request):
    cars = Car.objects.all()
    tags = Tag.objects.all()
    return render(request, 'main/catalog.html', context={'cars': cars, 'tags': tags})


def about(request):
    return render(request, 'main/about.html')


def contacts(request):
    return render(request, 'main/contacts.html')


def profile(request):
    return render(request, 'main/profile.html')


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
                    "error": form.errors,
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