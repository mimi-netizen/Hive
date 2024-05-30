from django.shortcuts import redirect, render
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request=request, data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
              
            else:
                pass
    elif request.method == 'GET':
        login_form = AuthenticationForm()
        
    return render(request, 'views/login.html', {'login_form': login_form})
