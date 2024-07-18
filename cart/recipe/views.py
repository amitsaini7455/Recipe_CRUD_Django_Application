from django.shortcuts import render, redirect
from .models import Recipe 
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required


@login_required
def recipes(request):  
    if request.method == 'POST':
        data = request.POST

        recipe_image = request.FILES.get('recipe_image')
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')

        Recipe.objects.create(  
            recipe_image=recipe_image,
            recipe_name=recipe_name,
            recipe_description=recipe_description,
        )
        return redirect('/')

    queryset = Recipe.objects.all() 

    if request.GET.get('search'):
        queryset = queryset.filter(
            recipe_name__icontains=request.GET.get('search'))

    context = {'recipes': queryset}  
    return render(request, 'recipes.html', context) 

@login_required
def delete_recipe(request, id):  
    queryset = Recipe.objects.get(id=id)  
    queryset.delete()
    return redirect('/')

@login_required
def update_recipe(request, id):  
    queryset = Recipe.objects.get(id=id)  

    if request.method == 'POST':
        data = request.POST

        recipe_image = request.FILES.get('recipe_image')
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')

        queryset.recipe_name = recipe_name  
        queryset.recipe_description = recipe_description  

        if recipe_image:
            queryset.recipe_image = recipe_image 

        queryset.save()
        return redirect('/')

    context = {'recipe': queryset}  
    return render(request, 'update_recipe.html', context)  

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after saving the form
            messages.success(request, 'Registration successful.')
            return redirect('/')  # Redirect to the home page
        else:
            messages.error(request, 'Unsuccessful registration. Invalid information.')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f'You are now logged in as {username}.')
                return redirect('/')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, 'You have successfully logged out.')
    return redirect('/login')
