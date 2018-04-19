# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
# from .models import User  
from models import *
import bcrypt
def registration(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect("/loginpage")
    else:
        pw = request.POST["password"]
        hash1 = bcrypt.hashpw(pw.encode(), bcrypt.gensalt())
        b = User.objects.create(first_name=request.POST["first_name"], last_name=request.POST["last_name"],email=request.POST["email"], password=hash1)
        request.session["user_id"] = b.id
        request.session["security"] = b.user_level
    return redirect("/users/show/"+b.id)
def login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect("/loginpage")
    else:
        user = User.objects.get(email = request.POST["email"])
        request.session["user_id"] = user.id
        request.session["security"] = user.user_level
    return redirect("/users/show/"+str(user.id))
def index(request):
    return render(request, 'index.html')
def loginpage(request):
    return render(request, "login.html")
def admin_newuser(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect("/users/new")
    else:
        pw = request.POST["password"]
        hash1 = bcrypt.hashpw(pw.encode(), bcrypt.gensalt())
        b = User.objects.create(first_name=request.POST["first_name"], last_name=request.POST["last_name"],email=request.POST["email"], password=hash1)
    return redirect("/dashboard/admin")
def users_show(request, id):
    user=User.objects.get(id=id)
    context = {
        "user" : user
    }
    return render(request, 'user_info.html', context)
def message_save(request):
    user = User.objects.get(id=request.session["user_id"])
    post = Message.objects.create(message=request.POST["message"], user=user)
    return redirect("/users/show/message")
def users_show_message(request):
    user=User.objects.get(id=request.session["user_id"])
    context = {
        "user" : 
    }




    
    return render(request, "user_info.html")

def logout(request):
    request.session.flush()
    return redirect('/')
def dash_admin(request): #display user info with queries
    users = User.objects.all()
    context = {
        "users" : users
    }
    return render(request, "dash_admin.html", context)
def admin_edit(request, id):
    user = User.objects.get(id=id)
    context = {
        "user" : user
    }
    return render(request, "edit_user.html", context)
def admin_new(request):
    return render(request, "new_user.html")
def update_user(request, id):
    user = User.objects.get(id=id)
    user.first_name=request.POST["first_name"]
    user.last_name=request.POST["last_name"]
    user.email=request.POST["email"]
    user.save()
    return redirect("/dashboard/admin")
def update_user_self(request, id):
    user = User.objects.get(id=id)
    user.first_name=request.POST["first_name"]
    user.last_name=request.POST["last_name"]
    user.email=request.POST["email"]
    user.description=request.POST["description"]
    user.save()
    return redirect("/dashboard")
def update_user_pw(request, id):
    errors = User.objects.pw_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect("/users/edit/"+str(id))
    else:
        pw = request.POST["password"]
        hash1 = bcrypt.hashpw(pw.encode(), bcrypt.gensalt())
        user = User.objects.get(id=id)
        user.password=hash1
        user.save()
    return redirect("/dashboard/admin")
def update_user_pw_self(request):
    errors = User.objects.pw_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect("/users/edit")
    else:
        pw = request.POST["password"]
        hash1 = bcrypt.hashpw(pw.encode(), bcrypt.gensalt())
        user = User.objects.get(id=request.session["user_id"])
        user.password=hash1
        user.save()
    return redirect("/dashboard")
def remove(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect("/dashboard/admin")
def users_edit(request):
    user = User.objects.get(id=request.session["user_id"])
    context = {
        "user" : user
    }
    return render(request, "edit_profile.html", context)
def dashboard(request):
    users = User.objects.all()
    context = {
        "users" : users
    }
    return render(request, "dashboard.html", context)








def create_comment(request, id):
    return redirect('users/show/'+id)
def create_message(request, id):
    return redirect('users/show/'+id)






def add(request):
    errors = TravelPlans.objects.add_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect("/travels/add")
    else:
        a = User.objects.get(name=request.session['name'])
        TravelPlans.objects.create(destination=request.POST["destination"], description=request.POST["description"], travel_date_from=request.POST["travel_date_from"], travel_date_to=request.POST["travel_date_to"], user = a)
        return redirect("/travels")
def travels(request):
    c = User.objects.get(id=request.session["user_id"])
    d = User.objects.exclude(id=request.session["user_id"])
    context = {
        "travel_plans" : TravelPlans.objects.filter(user = c),
        "others_plans" : TravelPlans.objects.filter(user = d),
        "joined_plans" : TravelPlans.objects.filter(travelers=request.session["user_id"])}
    return render(request, 'travels.html', context)
def destination(request, id):
    context = {
        "travel_plans" : TravelPlans.objects.get(id=id)
        }
    return render(request, 'destination.html', context)
def join(request, id):
    userjoin = User.objects.get(id=request.session["user_id"])
    e = TravelPlans.objects.get(id=id)
    userjoin.trips.add(e)  
    return redirect('/travels')
    # e.travelers=request.session["user_id"]
