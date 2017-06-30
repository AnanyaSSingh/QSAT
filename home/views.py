from django.shortcuts import render
from .forms import *
from django.core.mail import EmailMessage
from django.http import HttpResponseRedirect
from django.template.loader import *
from django.template import Context
# Create your views here.

def home(request):
	return render(request,'index.html')

def register(request):
	form = RegisterForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit = False)
		email = instance.email
		city = instance.city
		name = instance.name
		instance.save()
		
		subject = city + ': Confirmation mail for participation in qSAT'
		to = [email]
		from_email = 'confirmation@qsat.bits-quark.org'
		message = get_template('email.html').render(Context({'name': name.partition(' ')[0],'city': city,}))
		msg = EmailMessage(subject, message, from_email, to)
		msg.content_subtype = "html"
		msg.send()
		return render(request, "registercom.html")
	
	return render(request, 'register.html',{'form': form,})	

def registercom(request):
	return render(request, "registercom.html")

def download(request):
	return render (request, "downloads.html")

def team(request):
	return render(request, "team.html")

def handler404(request):
    response = render_to_response('error.html', {'error' : 404},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request):
    response = render_to_response('error.html', {'error' : 500},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response