from django.shortcuts import render
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def signup(request):
  template_data = {}
  template_data['title'] = 'Iniciar sesión'
  if request.method == 'GET':
    template_data['form'] = CustomUserCreationForm()
    return render(request, 'usuarios/signup.html', {'template_data': template_data})
  elif request.method == 'POST':
    form = CustomUserCreationForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('/usuarios/signup.html')
    else:
      template_data['form'] = form
      return render(request, 'usuarios/signup.html', {'template_data': template_data})

def login(request):
    template_data = {}
    template_data['title'] = 'Login'
    if request.method == 'GET':
        return render(request, 'usuarios/login.html', {'template_data': template_data})
    elif request.method == 'POST':
        user = authenticate(request, username = request.POST['username'], password = request.POST['password'])
        if user is None:
            template_data['error'] = 'The username or password is incorrect'
            return render(request, 'usuarios/login.html', {'template_data': template_data})
        else:
            auth_login(request, user)
            return render(request, 'usuarios/login.html', {'template_data': template_data})

@login_required
def logout(request):
  auth_logout(request)
  return render(request, 'usuarios/login.html')