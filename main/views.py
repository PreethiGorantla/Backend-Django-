from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import PatientForm
from .models import Patient
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets
from .serializers import PatientSerializer


# for authentication
def  register(request):
    print("REGISTER VIEW RUNNING")
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            messages.info(request,'username already exists')
            return redirect('register')
        user = User.objects.create_user(username=username,password=password)
        user.save()
        messages.success(request,'User created successfully')
        return redirect('login')
    return render(request,'register.html')

#user login
def user_login(request):
    print("LOGIN VIEW RUNNING")
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('patient_list')
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'login.html')
# logout
def user_logout(request):
    logout(request)
    return redirect('patient_list')
@login_required
def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'patient_list.html', {'patients': patients})
@login_required
def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm()

    return render(request, 'add_patient.html', {'form': form})

## update the patients
@login_required
def update_patient(request,pk):
     patient=get_object_or_404(Patient,pk=pk)
     if request.method == 'POST':
         form=PatientForm(request.POST,instance=patient)
         if form.is_valid():
             form.save()
             return redirect('patient_list')
         else:
             form=PatientForm(instance=patient)
     return render(request,'update.html',{'form':form})

# delete patient records
@login_required
def delete_patient(request,pk):
    patient=get_object_or_404(Patient,pk=pk)
    patient.delete()
    return redirect('patient_list')

# ModelViewSet Html views(for browser)...API views is for JSON
class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer