#from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
#from django.contrib.auth.hashers import check_password
#from store.models.customer import Customer
#from django.contrib.auth import login, authenticate
from django.contrib import messages
#from django.views import View
from . import userregform, loginform
#from user_auth.forms import AddItemForm
from user_auth.models import User

#from django.contrib.auth.forms import UserRegisterForm




def home(request):
    return render(request, 'user_auth/home.html')

def register(request):
    form = userregform.UserRegisterForm
    if request.method == 'POST':
        form = userregform.UserRegisterForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
    #        form.save()
            username = form.cleaned_data.get('username')
            if username is not None:
                return redirect('/login')
    #        password = form.cleaned_data.get('password1')
    #        user = authenticate(request, username=username, password=password)



    #        messages.success(request, f'Your account has been created. You can log in now!')
    #        user.set_password(password)
    #        user.save()

#            return redirect('login')
#    else:
#        form = 	userregform.UserRegisterForm()

    context = {'form': form}
    return render(request, 'user_auth/userreg.html', context)

def login(request):
    #username = User.objects.get(pk=1)
    #name = User.objects.all().values()
    qs = list(User.objects.values_list('username'))
    #password1 = list(User.objects.values_list('password1'))
    #list_user = list()
    #list_user.append(username)
    #password1 = User.objects.get('password1')
    #password1=User._meta.get_field('password1')

    #print(''.join(password1))
    #print(password1)
    form = loginform.LoginForm
    message = ''
    if request.method == 'POST':
        form = loginform.LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            qu = list(User.objects.values_list('username'))
            qp = list(User.objects.values_list('password1'))
            print("%%%%%%%%")
            for q in qu:
                usernamedb=''.join(q)
                print(usernamedb)
            for p in qp:
                passworddb=''.join(p)
                print(passworddb)

        #       username=form.cleaned_data['username'],
        #       password=form.cleaned_data['password1'],
            #username=request.POST['username'],
            #password=request.POST['password']
            #username=usernamedb
        #    password=passworddb

            #user = authenticate(username=username, password=password)
    #        )
            if (username == usernamedb and password == passworddb):
                print("%%%%%%%%############")
            #    login(request,user)
                message = f'Hello {username}! You have been logged in'

            #    messages.info( f"You are now logged in as {user.username}")
                return redirect('/products',message)
            else:
                #message = 'Login failed!'
                #messages.error(request, "Invalid username or password.")
                message="please check username and password"

    return render(
       request, 'user_auth/login.html', context={'form': form, 'message': message})
    #request, 'user_auth/login.html', context={'form': form})


def logout(request):
    #logout(request)
    return render(request, 'user_auth/logout.html')

#########    return render(request,'user_auth/displayitems.html')
