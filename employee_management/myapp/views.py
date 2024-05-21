from django.shortcuts import render
from.models import Employee,User
from django.shortcuts import render, redirect, get_object_or_404
from.forms import EmployeeForm,UserForm,UserProfileForm,UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.urls import reverse
from django.contrib.auth import logout as auth_logout
from django.http import JsonResponse
from django.views import View

# Create your views here.

@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def profile_view(request):
    employees = Employee.objects.all()
    return render(request, 'employee/employee_list.html', {'employees': employees})

@login_required
def employee_detail(request, id):
    employee = get_object_or_404(Employee, id=id)
    return render(request, 'employee/employee_detail.html', {'employee': employee})
@login_required
def employee_add(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'employee/employee_form.html', {'form': form})
@login_required
def employee_edit(request, id):
    employee = get_object_or_404(Employee, id=id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employee/employee_form.html', {'form': form})

@login_required
def employee_delete(request, id):
    employee = get_object_or_404(Employee, id=id)
    employee.delete()
    return redirect('employee_list')




@login_required
def user_list(request):
    users = User.objects.all()
    return render(request, 'user/user_list.html', {'users': users})
    
@login_required
def add_user(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('user_list')
    else:
        user_form = UserForm()
    return render(request, 'user/user_form.html', {'user_form': user_form})

@login_required
def user_detail(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(request, 'user/user_detail.html', {'user': user})


@login_required
def edit_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        if user_form.is_valid():
            user_form.save()
            return redirect('user_list')
    else:
        user_form = UserForm(instance=user)
    return render(request, 'user/user_form.html', {'user_form': user_form})





@login_required
def edit_profile(request):
    user = request.user
    user_profile, created = UserProfile.objects.get_or_create(user=user)
    
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        profile_form = UserProfileForm(request.POST, instance=user_profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('edit_profile')  # Redirect to a profile page or another page
    else:
        user_form = UserForm(instance=user)
        profile_form = UserProfileForm(instance=user_profile)
    
    return render(request, 'user/edit_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })



@login_required
def logout_view(request):
    logout(request)
    return redirect('login')
