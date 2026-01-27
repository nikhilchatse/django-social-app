from django.shortcuts import render,redirect,get_list_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib import messages
from posts.models import posts
from django.http import HttpResponseForbidden
# Create your views here.
@login_required(login_url="login")
def user_profile(request):
    profile= request.user.profile
    post=posts.objects.filter(user=request.user)
    
    return render(request,"profile.html",{'profile':profile,'post':post})

def home(request):
    post=posts.objects.all().order_by("-created_at")


    # search_result=request.GET.get("search")
    # if search_result:
    #     result=posts.objects.filter(captions__icontains=search_result)
    # else:
    #     result=posts.objects.none()
    return render(request,"index.html",{'post':post})

@login_required(login_url="login")
def edit_profile(request, id):
    edit_data = Profile.objects.get(id=id)

    if request.method == 'POST':
        edit_data.name = request.POST.get("name")
        edit_data.email = request.POST.get("email")
        edit_data.contact = request.POST.get("contact")
        edit_data.bio = request.POST.get("bio")

        if "image" in request.FILES:
            edit_data.profile_img = request.FILES["image"]

        edit_data.save()   
        

        return redirect("profile")

    return render(request, "edit.html", {'edit': edit_data})


@login_required(login_url="login")
def delete_post(request,id):
    postdel=posts.objects.filter(id=id)
    postdel.delete()
    return redirect("profile")