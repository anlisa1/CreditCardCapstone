# This is where all the database collections are defined. A collection is a place to hold a defined 
# set of data like Users, Blogs, Comments. Collections are defined below as classes. Each class name is 
# the name of the data collection and each item is a data 'field' that stores a piece of data.  Data 
# fields have types like IntField, StringField etc.  This uses the Mongoengine Python Library. When 
# you interact with the data you are creating an onject that is an instance of the class.

from sys import getprofile
from tokenize import String
from typing import KeysView
from xmlrpc.client import Boolean

from setuptools import SetuptoolsDeprecationWarning
from app import app
from flask import flash
from flask_login import UserMixin
from mongoengine import FileField, EmailField, StringField, IntField, ReferenceField, DateTimeField, BooleanField, ListField, CASCADE
from flask_mongoengine import Document
import datetime as dt
import jwt
from time import time
from bson.objectid import ObjectId


class User(UserMixin, Document):
    createdate = DateTimeField(defaultdefault=dt.datetime.utcnow)
    gid = StringField(sparse=True, unique=True)
    gname = StringField()
    gprofile_pic = StringField()
    username = StringField()
    fname = StringField()
    lname = StringField()
    email = EmailField()
    image = FileField()
    prononuns = StringField()
    role = StringField()
    age = IntField()

    # quiz results saved here
    creditcard = StringField()
    student = StringField()
    business = StringField()
    travel = StringField()
    dine = StringField()
    cashback = StringField()
    quizTake = BooleanField(default=False)
    
    # for the quiz and modules below
    quizComplete=BooleanField(default=False)
    CompletedModules=ListField()
    # all list fields below useless
    modulesDone=ListField()
    modules_completed=ListField()
    courses_marked=ListField()
    # will use the above lsit for modules
    meta = {
        'ordering': ['lname','fname']
    }

    
class Blog(Document):
    author = ReferenceField('User',reverse_delete_rule=CASCADE) 
    subject = StringField()
    content = StringField()
    tag = StringField()
    tag2 = StringField()
    create_date = DateTimeField(default=dt.datetime.utcnow)
    modify_date = DateTimeField()
    meta = {
        'ordering': ['-createdate']
    }

# class modules(Document):
    

class Module(Document):
    author = ReferenceField('User',reverse_delete_rule=CASCADE) 
    user_display = StringField()
    cover_image=FileField()
    title = StringField()
    content1 = StringField()
    image1 = FileField()
    image1size=IntField()
    video1 = StringField()
    content2 = StringField()
    image2 = FileField()
    video2 = StringField()
    content3= StringField()
    image3 = FileField()
    content4 = StringField()
    video3 = StringField()
    verified = BooleanField(default=False)
    create_date = DateTimeField(default=dt.datetime.utcnow)
    modify_date = DateTimeField()
    meta = {
        'ordering': ['-createdate'],
    }

class Comment(Document):
    # Line 63 is a way to access all the information in Course and Teacher w/o storing it in this class
    author = ReferenceField('User',reverse_delete_rule=CASCADE) 
    blog = ReferenceField('Blog',reverse_delete_rule=CASCADE)
    # This could be used to allow comments on comments
    comment = ReferenceField('Comment',reverse_delete_rule=CASCADE)
    # Line 68 is where you store all the info you need but won't find in the Course and Teacher Object
    content = StringField()
    create_date = DateTimeField(default=dt.datetime.utcnow)
    modify_date = DateTimeField()

    meta = {
        'ordering': ['-createdate']
    }

    