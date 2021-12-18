from django.contrib.messages.api import error
from django.shortcuts import redirect, render
from django.template import context
from .models import CustomUser, Helpline
from random import choice
from django.http import HttpResponse
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request, './home.html')


def registration(request):
    if request.method == ('POST'):
        validation = request.POST.get('Email')
        check_pass1 = request.POST.get('Password1')
        confirm_password = request.POST.get("Password2")
        if CustomUser.objects.filter(Email=validation) !=0:
            messages.error(request, 'A user with this email already exist!')
            return render(request, './registration_form.html')
        elif check_pass1 != confirm_password:
            messages.error(request, 'Password must be the same')
            return render(request, './registration_form.html')
        else:
            registration_input = CustomUser.objects.create(
            First_Name = request.POST.get('First Name'),
            Last_Name = request.POST.get('Last Name'),
            Country = request.POST.get('Country'),
            Email = request.POST.get('Email'),
            Phone_Number = request.POST.get('Phone Number'),
            Password1 = request.POST.get('Password1'),
            Confirm_Password = request.POST.get('Password2'),
        )  
            registration_input.save()
            request.session['id'] = registration_input.Email
            context = {
                "registration_input" : registration_input
            }
            return redirect('login')
            
    if request.method == ('GET'):
        return render(request, './registration_form.html')

def forget_pass(request):
    if request.method =='GET':
        return render(request, './forget_pass.html')

    else:
        email_check = request.POST.get('email')
        request.session['email_id'] = email_check
        check_email = CustomUser.objects.filter(Email=email_check)
        if check_email:
            return redirect("forget_password")
        else:
            messages.error(request, 'No user matches that password!')
            return render(request, './forget_pass.html')

def forget_password(request):
    if request.method =='GET':
        return render(request, "./forget_password.html")
    else:
        password_validation = CustomUser.objects.get(Email=request.session.get('email_id'))
        password = request.POST.get('Password')
        confirm_password = request.POST.get('confirm password')
        password_validation.Password1 = password
        password_validation.Confirm_Password = confirm_password
        password_validation.save()
        context = {
            'pasword_validation': password_validation
        }
        return render(request, "./login.html", context)

def login(request):
    if request.method=='GET':
      return render(request, './login.html')
    else:
        email = request.POST['Email']
        password = request.POST['Password']
        user = CustomUser.objects.get(Email= email)
        if user.Confirm_Password == password:
            request.session['user_id'] = email
            return redirect("helpline") 
        else:
            context = {"error": "Incorrect password"}
            return render(request, './login.html', context)

def helpline(request):
        if request.method =='GET':
            valid_user = CustomUser.objects.get(Email=request.session.get('user_id'))
            centers_in_country = Helpline.objects.filter(Country=valid_user.Country)
            if len(centers_in_country) == 0:
                return render(request, "./contact_Us.html")
            else:
                custom = choice(centers_in_country)
                customer_care = {
                    "country": custom.Country,
                    "branch": custom.Branch_name,
                    "phone": custom.Phone_number
                }
                return render(request, "./get_helpline.html", context=customer_care)   