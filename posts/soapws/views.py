from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .forms import CreateUserForm


# Create your views here.
from django.shortcuts import render
from suds.client import Client
soap_client = Client('http://10.100.51.100:8080/soapwebsrv/sakilaws?WSDL')


def show_users(request):
	results = soap_client.service.actors()
	context = {'results':results, }
	return render(request, 'soapws/allusers.html', context)


def create_user(request):
	if request.method == 'GET':
		form = CreateUserForm()
	else:
		form = CreateUserForm(request.POST)
		if form.is_valid():
			firstName = form.cleaned_data['firstName']
			lastName = form.cleaned_data['lastName']
			result = soap_client.service.createactor(firstName, lastName)
			if result:
				return HttpResponseRedirect(reverse('soapws:all-users'))
			else:
				return HttpResponse("User Not Created")

	return render(request, 'soapws/createuser.html', {
	   'form': form,
	})
