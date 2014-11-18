from django.shortcuts import render

# Create your views here.

from .forms import EmailForm, JoinForm
from .models import Join

def home(request):
	# # print request.POST["email"], request.POST["email_2"]

# This is using regular Django Forms
	# form = EmailForm(request.POST or None)
	# if form.is_valid():
	# 	email = form.cleaned_data['email']
	# 	new_join, created = Join.objects.get_or_create(email=email)
	# 	print new_join, created
	# 	print new_join.timestamp

# This is using Model Forms  
	form = JoinForm(request.POST or None)
	if form.is_valid():
		new_join = form.save(commit=False)
		
		email = form.cleaned_data['email']
		new_join, created = Join.objects.get_or_create(email=email)
		# new_join.save()

	context = {"form":form}
	template = "home.html"
	return render(request, template, context)