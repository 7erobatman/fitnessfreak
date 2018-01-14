from django.shortcuts import render,redirect
from django.conf import settings
from django.core.mail import send_mail
# from django.contrib.auth.forms import UserCreationForm
from . forms import RegistrationForm
from .forms import ContactForm

# Create your views here.
def register(request):
	 # if request.method="POST":
		form = RegistrationForm(request.POST)
		args = {'form':form}
		if form.is_valid():
			form.save()
			return redirect ('/login')
		return render(request,'register.html',args)

		# else:
		# 	form = UserCreationForm()
		# 	args = {'form':form}
		# 	return render(request,'register.html',args) 

def home(request):
	return render(request, "index.html", {})

def blog(request):
	form = ContactForm(request.POST or None)
	if form.is_valid():
		email = form.cleaned_data.get("email")
		contact_message = "thanks for subscribing"
		subject ='HI ! FITNESS freaker'
		from_email = settings.EMAIL_HOST_USER
		to_email = [email]
		send_mail(subject, contact_message, from_email, to_email, fail_silently=False)
	context={
	"form":form,
	}
	return render(request, "blog.html", context)

def images(request):
	form = ContactForm(request.POST or None)
	if form.is_valid():
		email = form.cleaned_data.get("email")
		contact_message = "thanks for subscribing"
		subject ='HI ! FITNESS freaker'
		from_email = settings.EMAIL_HOST_USER
		to_email = [email]
		send_mail(subject, contact_message, from_email, to_email, fail_silently=False)
	context={
	"form":form,
	}
	return render(request, "pic.html", context)

def strpics(request):
	form = ContactForm(request.POST or None)
	if form.is_valid():
		email = form.cleaned_data.get("email")
		contact_message = "thanks for subscribing"
		subject ='HI ! FITNESS freaker'
		from_email = settings.EMAIL_HOST_USER
		to_email = [email]
		send_mail(subject, contact_message, from_email, to_email, fail_silently=False)
	context={
	"form":form,
	}
	return render(request, "stpic.html", context)

def stretch(request):
	form = ContactForm(request.POST or None)
	if form.is_valid():
		email = form.cleaned_data.get("email")
		contact_message = "thanks for subscribing"
		subject ='HI ! FITNESS freaker'
		from_email = settings.EMAIL_HOST_USER
		to_email = [email]
		send_mail(subject, contact_message, from_email, to_email, fail_silently=False)
	context={
	"form":form,
	}
	return render(request, "stvid.html", context)

def workout(request):
	form = ContactForm(request.POST or None)
	if form.is_valid():
		email = form.cleaned_data.get("email")
		contact_message = "thanks for subscribing"
		subject ='HI ! FITNESS freaker'
		from_email = settings.EMAIL_HOST_USER
		to_email = [email]
		send_mail(subject, contact_message, from_email, to_email, fail_silently=False)
	context={
	"form":form,
	}
	return render(request, "exvid.html", context)
def exepics(request):
	form = ContactForm(request.POST or None)
	if form.is_valid():
		email = form.cleaned_data.get("email")
		contact_message = "thanks for subscribing"
		subject ='HI ! FITNESS freaker'
		from_email = settings.EMAIL_HOST_USER
		to_email = [email]
		send_mail(subject, contact_message, from_email, to_email, fail_silently=False)
	context={
	"form":form,
	}
	return render(request, "expic.html", context)
def mentor(request):
	form = ContactForm(request.POST or None)
	if form.is_valid():
		email = form.cleaned_data.get("email")
		contact_message = "thanks for subscribing"
		subject ='HI ! FITNESS freaker'
		from_email = settings.EMAIL_HOST_USER
		to_email = [email]
		send_mail(subject, contact_message, from_email, to_email, fail_silently=False)
	context={
	"form":form,
	}
	return render(request, "mentor.html", context)

def bmi(request):
	form = ContactForm(request.POST or None)
	if form.is_valid():
		email = form.cleaned_data.get("email")
		contact_message = "thanks for subscribing"
		subject ='HI ! FITNESS freaker'
		from_email = settings.EMAIL_HOST_USER
		to_email = [email]
		send_mail(subject, contact_message, from_email, to_email, fail_silently=False)
	context={
	"form":form,
	}
	return render(request, "bmi.html", context)

def video(request):
	form = ContactForm(request.POST or None)
	if form.is_valid():
		email = form.cleaned_data.get("email")
		contact_message = "thanks for subscribing"
		subject ='HI ! FITNESS freaker'
		from_email = settings.EMAIL_HOST_USER
		to_email = [email]
		send_mail(subject, contact_message, from_email, to_email, fail_silently=False)
	context={
	"form":form,
	}
	return render(request, "vid.html", context)

def contact(request):
	form = ContactForm(request.POST or None)
	if form.is_valid():
		email = form.cleaned_data.get("email")
		full_name = form.cleaned_data.get("full_name")
		message = form.cleaned_data.get("message")
		contact_message = "thanks for subscribing"
		subject ='HI ! FITNESS freaker'
		from_email = settings.EMAIL_HOST_USER
		to_email = [email]
		send_mail(subject, contact_message, from_email, to_email, fail_silently=False)
	context={
	"form":form,
	}
	return render(request,"forms.html", context)		
		