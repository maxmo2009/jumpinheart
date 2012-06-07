from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
def signup(request):
    return render_to_response('auth/signup.html', {}, context_instance=RequestContext(request))

def signup_form(request):
	username = request.POST['username']
	email = request.POST['email']
	pw = request.POST['pw']
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
