from django.shortcuts import render_to_response
from django.http import HttpResponse

def signup(request):
    return render_to_response('auth/signup.html', {})
