from django.shortcuts import render,redirect,get_object_or_404
from .models import posts,Comment
from django.contrib import messages
from django.contrib.auth.decorators import login_required
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


@login_required
def post_like(request,post_id):
    post = get_object_or_404(posts,id=post_id)

 
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return redirect('/')
    

@login_required
def add_comment(request, post_id):
    post = get_object_or_404(posts, id=post_id)

    if request.method == "POST":
        text = request.POST.get("comment")
        if text:
            Comment.objects.create(
                post=post,
                user=request.user,
                text=text
            )
    return redirect('/')


