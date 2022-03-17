from django.shortcuts import render
from django.http import HttpResponse
from .models import Users
from .CustomAuth import CustomAuthentication
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def Login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    if request.method == 'POST':
        auth = CustomAuthentication()
        user = auth.authenticate(request=request, username=username, password=password)
        if user is not None:
            return HttpResponse(user)
        else:
            return HttpResponse("user doesn't exist")
