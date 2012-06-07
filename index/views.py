from django.http import HttpResponse
from django.contrib.auth.models import User
def index(request):
	user = request.user
	if user.is_authenticated():
		return HttpResponse('Authenticated!')
	else:
		return HttpResponse('Not authenticated!')
