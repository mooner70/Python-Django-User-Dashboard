# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import re
from  datetime import *
import bcrypt
password_regex = re.compile('^(?=\S{6,20}$)(?=.*?\d)(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[^A-Za-z\s0-9])')
class RegManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        count = User.objects.filter(email=postData["email"]).count
        if count > 0:
            errors["email"] = "Email already registered"
        if len(postData["first_name"]) < 3:
            errors["first_name"] = "First name should be more than 3 characters"
        if len(postData["last_name"]) < 3:
            errors["last_name"] = "Last name should be more than 3 characters"
        if len(postData["email"]) < 3:
            errors["email"] = "Email should be more than 3 characters"
        if len(postData["password"]) < 8:
            errors["password"] = "Password should be more thatn 8 characters"
        # elif not password_regex.match(postData["password"]):
        #     errors["password"] = "Invalid password"
        if postData["password"] != postData["confirm_password"]:
            errors["confirm_password"] = "Password confirmation does not match"
        return errors
    def login_validator(self, postData):
        errors = {}
        if len(postData["email"]) < 3:
            errors["email"] = "Email should be more than 3 characters"
        if len(postData["password"]) < 8:
            errors["password"] = "Password must be longer than 8 characters"
        check = User.objects.filter(email=postData["email"])
        if len(check) == 0:
            errors["email"] = "Must enter an email address"
            return errors
        if not bcrypt.checkpw(postData["password"].encode(), check[0].password.encode()):
            errors["password"] = "Password doesn't match"
        return errors
    def pw_validator(self, postData):
        errors = {}
        if len(postData["password"]) < 8:
            errors["password"] = "Password must be longer than 8 characters"
        if postData["password"] != postData["confirm_password"]:
            errors["confirm_password"] = "Password confirmation does not match"
        return errors
    # def add_validator(self, postData):
    #     errors = {}
    #     if len(postData["destination"]) < 1:
    #         errors["destination"] = "Destination field cannot be empty"
    #     if len(postData["description"]) < 1:
    #         errors["description"] = "Description field cannot be empty"
    #     if len(postData["travel_date_from"]) < 1:
    #         errors["travel_date_from"] = "Travel Date From field cannot be empty"
    #     if len(postData["travel_date_to"]) < 1:
    #         errors["travel_date_to"] = "Travel Date To field cannot be empty"
    #     if postData["travel_date_from"] < datetime.now().strftime("%Y-%m-%d"):
    #         errors["travel_date_from"] = "Travel Date From needs to be in the future"

    #     if postData["travel_date_to"] < postData["travel_date_from"]:
    #         errors["travel_date_to"] = "Travel Date From needs to be in the future"
    #     return errors
class MessageManager(models.Manager):
  pass
class CommentManager(models.Manager):
  pass
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    user_level = models.IntegerField(null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = RegManager()

class Message(models.Model):
    message = models.CharField(max_length=255)
    user = models.ForeignKey(User, related_name = "messages")
    receiver = models.IntegerField(null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = MessageManager()

class Comment(models.Model):
    comment = models.CharField(max_length=255)
    message = models.ForeignKey(Message, related_name = "comments")
    user = models.ForeignKey(User, related_name = "comments")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CommentManager()
