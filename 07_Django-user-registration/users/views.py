from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login
from .forms import UserRegisterForm

# Create your views here.
def register(request):
    # Logged in user can't register a new account
    if request.user.is_authenticated:
        return redirect("/")

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
        else:
            for error in list(form.errors.values()):
                print(request, error)

    else:
        form = UserRegisterForm()

    return render(
        request = request,
        template_name = "register.html",
        context={"form":form}
        )
