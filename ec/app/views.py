from django.shortcuts import render
from django.db.models import Count
from urllib import request
from django.http import HttpResponse
from django.views import View
from . models import Product
from . forms import CustomerRegistrationForm
# import pyrebase

def home(request):
    return render(request,"app/home.html")

def about(request):
    return render(request,"app/about.html")

def contact(request):
    return render(request,"app/contact.html")

class CategoryView(View):
    def get(self,request,val):
        product=Product.objects.filter(category=val)
        title=Product.objects.filter(category=val).values('title')
        return render(request,"app/category.html",locals())

class CategoryTitle(View):
    def get(self,request,val):
        product=Product.objects.filter(title=val)
        title=Product.objects.filter(category=product[0].category).values('title')
        return render(request,"app/category.html",locals())

class ProductDetail(View):
    def get(self,request,pk):
        product=Product.objects.get(pk=pk)
        return render(request,"app/productdetail.html",locals())
    
class CustomerRegistrationView(View):
     def get(self,request):
         form=CustomerRegistrationForm()
         return render(request,'app/customerregistration.html',locals())


# config={
#     apiKey: "AIzaSyDlrHyujdfcbfybow1s6peCa6Q2LOKyDc8",
#     authDomain: "Use Your authDomain Here",
#     databaseURL: "Use Your databaseURL Here",
#     projectId: "Use Your projectId Here",
#     storageBucket: "Use Your storageBucket Here",
#     messagingSenderId: "Use Your messagingSenderId Here",
#     appId: "Use Your appId Here"
# }
# # Initialising database,auth and firebase for further use 
# firebase=pyrebase.initialize_app(config)
# authe = firebase.auth()
# database=firebase.database()
 
# def signIn(request):
#     return render(request,"Login.html")
# def home(request):
#     return render(request,"Home.html")
 
# def postsignIn(request):
#     email=request.POST.get('email')
#     pasw=request.POST.get('pass')
#     try:
#         # if there is no error then signin the user with given email and password
#         user=authe.sign_in_with_email_and_password(email,pasw)
#     except:
#         message="Invalid Credentials!!Please ChecK your Data"
#         return render(request,"Login.html",{"message":message})
#     session_id=user['idToken']
#     request.session['uid']=str(session_id)
#     return render(request,"Home.html",{"email":email})
 
# def logout(request):
#     try:
#         del request.session['uid']
#     except:
#         pass
#     return render(request,"Login.html")
 
# def signUp(request):
#     return render(request,"Registration.html")
 
# def postsignUp(request):
#      email = request.POST.get('email')
#      passs = request.POST.get('pass')
#      name = request.POST.get('name')
#      try:
#         # creating a user with the given email and password
#         user=authe.create_user_with_email_and_password(email,passs)
#         uid = user['localId']
#         idtoken = request.session['uid']
#         print(uid)
#      except:
#         return render(request, "Registration.html")
#      return render(request,"Login.html")
