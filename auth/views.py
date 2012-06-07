from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
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
		if login_user.is_active:
			login(request, login_user)
			return HttpResponseRedirect('/')
