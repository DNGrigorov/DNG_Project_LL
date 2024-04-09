from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import SignUpForm, UserLoginForm

def UserSignUpView(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('AccountApp:ViewLogin')
    else:
        form = SignUpForm()
    return render(request, 'AccountApp/signup.html', {'form':form})

def UserLoginView(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)

                return redirect('HomeApp:ViewHome')
            else:
                # Invalid login
                form.add_error(None, "Invalid username or password.")
    else:
        form = UserLoginForm()

    return render(request, 'AccountApp/login.html', {'form': form})