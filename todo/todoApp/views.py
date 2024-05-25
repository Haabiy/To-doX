from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.template.loader import render_to_string



# import forms and models 
from . forms import CreateUserForm, LoginForm, usertodolist, UpdateUserForm, UpdateProfileForm
from . models import todo, Profile

# Authentication libs
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def test101(request):
    return HttpResponse('Hello world')

def homepage(request):
    return render(request, "todoApp/index.html")

def register(request):
    '''
    This view handles user registration.

    On GET request:
    - Initializes an instance of CreateUserForm.
    - Renders the registration page with the form.

    On POST request:
    - Binds the form with the POST data.
    - Validates the form data.
    - If form data is valid, saves the form data to create a new user, displays a success message, and redirects to the login page.
    - If form data is invalid, displays an error message.

    Returns:
    - Renders the registration page with the form instance.
    '''
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save() # Related to user profile-picture upload saving it in the Profiles db(admin/auth/user), as it is connected through ForeignKey
            
            # Sending welcome emails
            # Email parameters
            subject = 'Welcome to TodoX'
            message = 'Welcome to TodoX! We hope you enjoy using our app.'
            #html_message = render_to_string('todoApp/welcome.html', {'recipient_name': {user.username}})
            
            # Please follow the steps to set up sending email using gmail-2FA.pdf (found in 2FAGuide folder)
            #send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email])

            Profile.objects.create(user=user) 
            form.save() # And then, saving to the user db in http://127.0.0.1:8000/admin/auth/user/ for example if running locally
            messages.success(request, 'Successful user creation')
            return redirect('my_login')
        else:
            messages.error(request, 'Try again !')
    else:
        form = CreateUserForm()

    context = {"registration_form" : form}
        
    return render(request, "todoApp/register.html", context=context)

@login_required(login_url='my_login')
def dashboard(request):
    # Profile picture upload
    try:
        profile_picture = Profile.objects.get(user=request.user)
        context = {'ProfilePicture' : profile_picture}
    except Profile.DoesNotExist:
        # If the profile does not exist for the current user
        if request.user.is_superuser:
            # For admin user, create a default profile picture
            admin_user = User.objects.get(username=request.user)
            profile_picture = Profile.objects.create(user=admin_user)
            context = {'ProfilePicture' : profile_picture}
        else:
            # For non-admin users, handle the case gracefully
            context = {'ProfilePicture' : None}
    return render(request, "todoApp/dashboard.html", context=context)

def my_login(request):
    '''
    This view handles user login.

    On GET request:
    - Initializes an instance of LoginForm.
    - Renders the login page with the form.

    On POST request:
    - Gets the username and password from the request.POST data.
    - Authenticates the user.
    - If authentication is successful, logs the user in and redirects to the dashboard.
    - If authentication fails, stays on the login page with an error message.

    Returns:
    - Renders the login page with the form instance.
    '''
    form = LoginForm()
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')
    context = {'authentication_form':form}
    return render(request, "todoApp/my_login.html", context=context)

def my_logout(request):
    logout(request)

    return redirect('homepage')

'''@login_required(login_url='my_login')
def create(request):
    if request.method=='POST':
        form = usertodolist(request.POST)
        if form.is_valid:
            # no need anymore
            #form.save(commit=False)
            #form.user = request.user
            form.save()
            return redirect('dashboard')
    else:
        form = usertodolist()
    context = {'create_form' : form}
    return render(request, "todoApp/create.html", context)'''

@login_required(login_url='my_login')
def create(request):
    '''
    View function for creating a new task.

    On GET request:
    - Renders the create.html template with an empty form.

    On POST request:
    - Populates the form with POST data.
    - If the form is valid, assigns the current user to the 'user' field of the form instance.
    - Saves the form instance.
    - Redirects to the 'read' view.

    Returns:
    - Renders the create.html template with the form instance.
    '''
    if request.method == 'POST':
        form = usertodolist(request.POST)
        if form.is_valid():
            # Saves the form instance, now the 'user' field will be set to the current user
            form.instance.user = request.user
            form.save()
            return redirect('read')  
    else:
        # Render an empty form
        form = usertodolist()
    context = {'create_form': form}
    return render(request, "todoApp/create.html", context)

@login_required(login_url='my_login')
def read_all(request):
    '''
    View function for displaying all tasks of the logged-in user.

    Retrieves all tasks associated with the current user, ordered by date posted in descending order.

    Returns:
    - Renders the read.html template with the queryset of tasks associated with the current user.
    '''
    read_models = todo.objects.filter(user = request.user).order_by('-date_posted') 
    #read_models = todo.objects.all()
    context = {"read_models": read_models}
    print(read_models)
    return render(request, "todoApp/read.html", context=context)

@login_required(login_url='my_login')
def toupdate(request, pk):
    '''
    View function for updating a task.

    Retrieves the task with the given primary key and associated with the current user.
    On POST request:
    - Populates the form with POST data and the retrieved task instance.
    - If the form is valid, saves the form instance and redirects to the 'read' view.

    Returns:
    - Renders the update.html template with the form instance.
    '''
    try:
        mytask = get_object_or_404(todo, id=pk, user=request.user)
        if request.method == 'POST':
            form = usertodolist(request.POST, instance=mytask)
            if form.is_valid():
                form.save()
                return redirect('read') # Redirect to a success page or any other desired URL
        else:
            form = usertodolist(instance=mytask)  # Populate the form with existing data
        context = {"update_form" : form}
    except Exception:
        return redirect('read')
    return render(request, "todoApp/update.html", context = context)

@login_required(login_url='my_login')
def todelete(request, pk):
    '''
    View function for deleting a task.

    Retrieves the task with the given primary key.
    On POST request:
    - Deletes the task instance and redirects to the 'read' view.

    Returns:
    - Renders the delete.html template.
    '''
    delete_task = get_object_or_404(todo, id=pk)
    if request.method == 'POST':
        delete_task.delete()
        return redirect('read')
    return render(request, 'todoApp/delete.html')

# Update the username and email address
'''@login_required(login_url='my_login')
def profile_management(request):
    form = UpdateUserForm(instance=request.user)
    if request.method =='POST':
        form = UpdateUserForm(request.POST, instance=request.user) # for that specific user
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    
    context ={
        'update_userform': form
        } 
    return render(request, "todoApp/profile_management.html", context = context)'''

# updating the username + email address + allow users to upload their own profile picture
@login_required(login_url='my_login')
def profile_management(request):
    form = UpdateUserForm(instance=request.user)
    profile = Profile.objects.get(user=request.user) # related to the file upload
    form_2 = UpdateProfileForm(instance=request.user) # to allow user to upload their own profile picture
    if request.method =='POST':
        form = UpdateUserForm(request.POST, instance=request.user) # for that specific user
        form_2 = UpdateProfileForm(request.POST, request.FILES, instance=profile) # same if we use instance = request.user
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        if form_2.is_valid():
            form_2.save()
            return redirect('dashboard')
    
    context ={
        'update_userform': form, 
        'update_profileform': form_2
        } 
    return render(request, "todoApp/profile_management.html", context = context)

@login_required(login_url='my_login')
def delete_profile(request):
    if request.method=='POST':
        deleteUser = User.objects.get(username=request.user)
        deleteUser.delete()
        return redirect('homepage')
    return render(request, "todoApp/delete_account.html")

'''@login_required(login_url='my_login')
def delete_profile(request):
    pass'''




