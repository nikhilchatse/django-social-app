from django.shortcuts import render,redirect
from .models import posts
from django.contrib import messages
# Create your views here.


def create_post(request):
    if request.method=='POST':
        image=request.FILES.get('postimg')
        captions=request.POST.get("captions")

        if not image:
            messages.error(request, "Image not received")
            return redirect("createpost")
        
        posts.objects.create(
            user=request.user,
            image=image,
            captions=captions,

        )
        
        messages.info(request,"Post Created!!!")
        return redirect("/")
    return render(request,"createpost.html")

