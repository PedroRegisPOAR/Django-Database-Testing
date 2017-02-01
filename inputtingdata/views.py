from django.shortcuts import render, HttpResponse

from inputtingdata.models import Number


# Create your views here.

def home(request):
	if request.method == "POST":
		n = float(request.POST["num"])
		number = Number(number=n)
		number.save()
	return render(request, 'inputtingdata/mytemplate.html')