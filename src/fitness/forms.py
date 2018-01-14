from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
	email = forms.EmailField(required=True)

	def __init__(self, *args, **kwargs):
        		super(RegistrationForm, self).__init__(*args, **kwargs)

            		for fieldname in ['username', 'password1', 'password2']:
            			self.fields[fieldname].help_text = None

	class Meta:
		model = User
		fields = {'username' , 'first_name' , 'last_name' , 'email' , 'password1' , 'password2' }


		def save(self, commit=True):
			User =super(RegistrationForm,self).save(commit=False)
			User.first_name=self.cleaned_data['first_name']
			User.last_name=self.cleaned_data['last_name']
			User.email=self.cleaned_data['email']

			if commit:
				User.save()

			return User

class ContactForm(forms.Form):
	#full_name=forms.CharField(required=False)
	email=forms.EmailField()
	#message=forms.CharField()

	# def clean_email(self):
	# 	email =  self.cleaned_data.get('email')
	# 	email_base, provider = email.split("@")
	# 	domain,extension = provider.split(".") 
	# 	#if not extension =="edu":
	# 		#if not "edu" in email:
	# 		#raise forms.ValidationError("please use a valid .EDU email address")

	# 	if not domain =='gmail':
	# 	          raise forms.ValidationError("please provide gmail address")	
	# 	return email



