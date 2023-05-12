from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Topic, Reply
from django.http import HttpResponse

# Create your views here.
def home(request):
	topics = Topic.objects.all()	# models의 Topic 객체를 생성
	return render(request, 'home.html', {'topics' : topics})

def new_topic(request):
    topics = Topic.objects.all()
    if request.method =='POST':
        subject = request.POST['subject']
        message = request.POST['message']
        user = request.user
        topic = Topic.objects.create(
            subject = subject,
            message = message,
            writter = user
        )
        post = Reply.objects.create(
            message = message,
            created_by = user
        )
        return redirect('/')

    return render(request,'new_topic.html',{'topics':topics})
