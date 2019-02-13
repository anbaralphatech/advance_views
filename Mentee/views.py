from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Mentee
from .forms import PostForm

# Create your views here.

def Mentee(request):
    return render(request,'Mentee/Mentee.html',{})

def db_mentee(request):
    mentee = Mentee.objects.all()
    return render(request,'Mentee/db_mentee.html', {'mentees':mentee})

def input_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('db_mentee')
    else:
        form = PostForm()
    return render(request,'Mentee/post_new.html', {'forms':form})