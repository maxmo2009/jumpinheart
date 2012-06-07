from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
def index(request):
	user = request.user
	message = '';
	if user.is_authenticated():
		message = 'Authenticated!'
	else:
		message = 'Not authenticated!'
	return render_to_response('index/index.html', {'message': message})
