from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import logout


def home_page(request):
    return render(request, 'main/index.html')


def catalog(request):
    return render(request, 'main/catalog.html')


def about(request):
    return render(request, 'main/about.html')


def contacts(request):
    return render(request, 'main/contacts.html')


def registration(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = request.POST.get("login")
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