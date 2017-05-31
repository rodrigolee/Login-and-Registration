from django.shortcuts import render, redirect
from models import Users
def index(request):
    return render(request, 'loginandreg/index.html')
def create(request):
    if request.method =="POST":
        print request.POST
        Users.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=request.POST['password'], pw_confirm=request.POST['pw_confirm'])
        # User= Users.objects.all()
        context = {
        "Registered":Users.objects.all()
        }
    return render(request, 'loginandreg/success.html', context)
