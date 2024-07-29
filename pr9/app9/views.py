from django.shortcuts import render,redirect
from.forms import DocumentForm
from.forms import dataform
from.models import *

def upload_document(request):
    if request.method=='POST':
        form=DocumentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('document_list')
    else:
            form=DocumentForm()
            return render(request,'form.html',{'form':form})
    
def document_list(request):
    documents=Document.objects.all()
    return render(request,'document.html',{'documents':documents})
from django.shortcuts import render,redirect
from django.http import HttpResponse

def set_session(request):
     request.session['name']='JOhn Doe'
     return HttpResponse('Session data set')
def get_session(request):
     name=request.session.get('name','Session data not set')
     return HttpResponse(f'Session data:{name}')

def set_cookie(request):
     response=HttpResponse('Cookie data set')
     response.set_cookie('name','Jane Doe',max_age=3600)#Cookie expires in 1 hour
     return response
def get_cookie(request):
     name=request.COOKIES.get('name','Cookie data not set')
     return HttpResponse(f'Cookie data:{name}')
#session cookie workout
def login(request):
    if request.method=='POST':
       print("form")
       forms=dataform(request.POST)
       print("form")

       if forms.is_valid():
            print("username")
            
            username=forms.cleaned_data['username']
            password=forms.cleaned_data['password']
            print(username,password)

            if password=="admin":
                 print("password")
                 request.session['name']=username
                 return HttpResponse('Session data set')
              
            else:
                 return redirect('set_cookie')
    else:
         forms=dataform()
         return render(request,'session.html',{'form':forms})
         
               





