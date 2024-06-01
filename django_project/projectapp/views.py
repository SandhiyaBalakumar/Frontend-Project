from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .models import Datas
from django.contrib.auth import login,authenticate
from django.contrib import messages
from.forms import UserRegistrationForm


"""
def home(request):  # 127.0.0.1:8000/
    mydata=Datas.objects.all()
    if(mydata!=""):
        return render(request,"form.html",{"datas":mydata})
    else:
        return render(request,"form.html")    
      
"""

def sandhiya(request):
    if request.method=="POST":
        name=request.POST["name"]
        age=request.POST["age"]
        contact=request.POST["contact"]
        address=request.POST["address"]
        mail=request.POST["mail"]
        gender=request.POST["gender"]
        
        obj=Datas()
        obj.Name=name
        obj.Age=age
        obj.Contact=contact
        obj.Address=address
        obj.Mail=mail
        obj.Gender=gender
        obj.save()
        mydata=Datas.objects.all()
        return redirect("home")
    return render(request,"form.html")



def updateData(request,id):
    mydata=Datas.objects.get(id=id)
    if request.method=="POST":
        name=request.POST["name"]
        age=request.POST["age"]
        contact=request.POST["contact"]
        address=request.POST["address"]
        mail=request.POST["mail"]
        gender=request.POST["gender"]

        mydata.Name=name
        mydata.Age=age
        mydata.Contact=contact
        mydata.Address=address
        mydata.Mail=mail
        mydata.Gender=gender
        mydata.save()
        return redirect("home")
    return render(request,"update.html",{"data":mydata})

def deleteData(request,id):
    mydata=Datas.objects.get(id=id)
    mydata.delete()
    return redirect("home")


def form(request):
    template = loader.get_template('form.html')
    return HttpResponse(template.render())
 

def register(request):
    if request.method=='POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request,'Your account has been created.You can Login now!')
            return redirect('login')
    else:
            form=UserRegistrationForm()


            context={'form':form}
            return render(request,'register.html',context) 
"""

def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())
 
def logout(request):
    template = loader.get_template('logout.html')
    return HttpResponse(template.render())
"""
def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())
 
# Create your views here.
