from django.shortcuts import render

# Create your views here.

def rats(request):

	rats = "rats"

	return render(request,'rats.html',{
                'rats': rats,
                })