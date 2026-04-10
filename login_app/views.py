from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from signup_app.models import All_user

def login(request):
    user_id = request.session.get("user_id")
    if user_id:
        return HttpResponse("You are already logged in.")
    if request.method == 'POST':
        email = request.POST.get('loginEmail')
        password = request.POST.get('loginPassword')
        try:
            user = All_user.objects.get(email=email, password=password)
            if user:
                request.session["user_id"] = user.id
                request.session["user_email"] = user.email
                
                return redirect("home")
        except All_user.DoesNotExist:
            return HttpResponse("Invalid email or password.")
    return render(request,'login_app/login_page.html',{})


def logout(request):
    request.session.flush()
    return redirect("login")