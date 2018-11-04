from django.shortcuts import render
from django.http import HttpResponse
from .models import Members
# Create your views here.

def index(request):
    return HttpResponse("hellooooo. Welcome to the index.")

def member_list(request):
    members = Members.objects.all()
    return render(request, 'members/members.html', {'members': members})