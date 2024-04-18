from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from .forms import SignUpForm, UserLoginForm


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import WebUser, LanguageSkill, Rating
from .serializers import WebUserSerializer
from rest_framework.exceptions import ValidationError

class UserSignUpView(View):
    def get(self, request):
        form = SignUpForm()
        return render(request, 'AccountApp/signup.html', {'form': form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully signed up! You can now log in.')
            return redirect('AccountApp:ViewLogin')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}")
            return render(request, 'AccountApp/signup.html', {'form': form})

class UserLoginView(View):
    def get(self, request):
        form = UserLoginForm()
        return render(request, 'AccountApp/login.html', {'form': form})

    def post(self, request):
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('HomeApp:ViewHome')
            else:
                form.add_error(None, "Invalid username or password.")
        return render(request, 'AccountApp/login.html', {'form': form})

class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('AccountApp:ViewLogin')


def ViewFilterUser(request):
    return render(request, 'AccountApp/filter.html')


# Rest API View
# To Filter Users Based on the Language Skills and Rating
class UserSearchAPIView(APIView):
    def get(self, request):
        # Get query parameters from request
        language_skill = request.query_params.get('language_skill')
        min_rating = request.query_params.get('min_rating')

        if not language_skill or not min_rating:
            raise ValidationError("Language skill and minimum rating are required.")

        # Fetch users based on language skill and minimum rating
        get_user_objs = Rating.objects.filter(language=language_skill, stars__gte=min_rating)

        # Extract the user objects from the ratings
        users = [rating.rated_user for rating in get_user_objs]

        return render(request, 'AccountApp/filter.html', {'users': users})
