from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from django.contrib.auth.forms import UserCreationForm
def signup(request):
	form = UserCreationForm()    
	return render_to_response('auth/signup.html', {}, context_instance=RequestContext(request))

def signup_form(request):
	if request.method == 'POST':
		email = request.POST['email']
		pw = request.POST['pw']
		username = 'peterchou139'
		user = User.objects.create_user(username, email, pw)
		user.save()
	
		login_user = authenticate(username=username, password=pw)
		if login_user is not None:
			return login_redirect(request, login_user)

def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')

def login_view(request):
	return render_to_response('auth/login.html', context_instance=RequestContext(request))

def login_form(request):
	if request.POST == 'POST':
		email = request.POST['email']
		pw = request.POST['pw']
		try:
			user = User.objects.get(email=email)
			login_user = authenticate(username=user.username, password=pw)
			if login_user is not None:
				return login_redirect(request, login_user)
		except User.DoesNotExist:
			return HttpResponseRedirect('/')

def login_redirect(request, login_user):
	if login_user.is_active:
		login(request, login_user)
		return HttpResponseRedirect('/')
def check_username(request):
  if request.is_ajax():
    if request.method == 'POST':
      username = request.POST['username']
	  if len(username)>30 or len(username)<2
	    return HttpResponse('too long')
	  
      try:
        user = User.objects.get(username=username)
        return HttpResponse('not ok')
      except User.DoesNotExist:
        return HttpResponse('ok')
def check_email(request):
  if request.is_ajax():
    if request.method == 'POST':
      email = request.POST['email']
      try:
	    user = User.objects.get(email=email)
	    return HttpResponse('not ok')
      except User.DoesNotExist:
	    return HttpResponse('ok')

