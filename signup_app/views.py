from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import All_user

# Create your views here.
def signup(request):
    if request.method=="POST":
        fname = request.POST.get("fname")
        email = request.POST.get("email")
        password = request.POST.get("pass")
        a_user = All_user(fname=fname,email=email,password=password)
        a_user.save()
        return redirect("home")
    return render(request,"signup_app/signup_index.html",{})

    

def print_users(request):
    return HttpResponse("User list page is under construction.")
    # a_users = All_user.objects.get(email='hasib@gmail.com')
    a_users = All_user.objects.all()
    
    data = "-->".join([us.fname + us.password for us in a_users])
    return HttpResponse(data)