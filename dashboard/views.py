from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from signup_app.models import All_user
from .models import User_post,Friend_List
# Create your views here.

def Homepage(request):
    user_id = request.session.get("user_id")
    if user_id == None:
        return redirect("login")
    all_posts = User_post.objects.all().order_by("-cretaed_at")
    all_friends = Friend_List.objects.filter(source_friend=request.session.get("user_email")).order_by("-cretaed_at")
    u_email = request.session.get("user_email")
    username = All_user.objects.get(email=u_email).fname
    return render(request,'dashboard/homepage.html',{"posts":all_posts,"username": username,"friends": all_friends})    

def StatusUpdate(request):
    user_email = request.session.get("user_email")
    
    if user_email == None:
        return redirect("login")
    if request.method == "POST":
        post_content = request.POST.get("post_content")
        User_post.objects.create(email=user_email,post_msg=post_content)
        return redirect("home")

def Unfriend(request,friend_email):
    user_email = request.session.get("user_email")
    
    if user_email == None:
        return redirect("login")
    Friend_List.objects.filter(source_friend=user_email,target_friend=friend_email).delete()
    return redirect("home")