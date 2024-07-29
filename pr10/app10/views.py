from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from .forms import *
from .serializers import *

def student_login(r):
    if r.user.is_authenticated and not(r.user.is_staff):
        return redirect("loop3")
    if r.method=='POST':
        form=studentloginform(r,r.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(r,username=username,password=password)
            if user is not None:
                login(r,user)
                return redirect('loop3')
            else:
                form.add_error(None,'Invalid email or password')
    else:
        form=studentloginform()
        return render(r,'index.html',{'form':form})
    
def registration(r):
    if r.method=='POST':
        form=stuform(r.POST,r.FILES)
        if form.is_valid():
            student=form.save(commit=False)
            email=form.cleaned_data['EmailId']
            password=form.cleaned_data['password']
            user=User.objects.create_user(username=email, email=email, password=password)
            student.user=user
            student.save()
            return redirect('loop1')
    else:
        form=stuform()
    return render(r,'register.html',{'form':form})
        

def student_dashboard(r):
    if r.user.is_authenticated and not(r.user.is_staff):
        student=r.user.students
        return render(r,'sample.html',{'name':student})
    else:
        return redirect('loop1')
    
@login_required(login_url='/login1/')
def student_logout(r):
    logout(r)
    return redirect('loop1')
from rest_framework import serializers
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def ApiOverview(r):
    api_urls = {
        'all_items': '/all/',
        'Search by Category': '/?category=category_name',
        'Search by Subcategory': '/?subcategory=category_name',
        'Add': '/create',
        'Update': '/update/pk',
        'Delete': '/item/pk/delete'
    }

    return Response(api_urls)

@api_view(['POST'])
def add_items(r):
    item=Itemserializer(data=r.data)
    if Item.objects.filter(**r.data).exists():
        raise serializers.ValidatationError('This data already exists')
    if item.is_valid():
        item.save()
        return Response(item.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

  
  
@api_view(['GET'])
def view_items(r):
    if r.Query_params:
        items=Item.objects.filter(**r.Query_params.dict())
    else:
        items=Item.objects.all()
    if items:
        serializer=Itemserializer(items,many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
@api_view(['POST'])
def update_items(r,pk):
    item=Item.objects.get(pk=pk)
    data=Item.serializer(instance=item,data=r.data)
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
@api_view(['GET'])
def delete_view(r,pk):
    item=Item.objects.get(pk=pk)
    item.delete()
    return Response(status=status.HTTP_204_NO_FOUND)

