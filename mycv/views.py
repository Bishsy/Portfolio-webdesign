from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse
# Create your views here.
'''def index(request):
    dests = Image.objects.all()
    return render(request, "index.html", {'dests':dests})'''
def index(request):
    return render(request , "index.html")


'''def contact(request):
    if request.method == "POST":
        user_name = request.POST['name']
        user_email = request.POST['email']
        user_message = request.POST['message']
        #send an email
        send_mail(
            #subject
            user_name,
            #message
            user_message,
            #from email
            email,
            ['bishalsunarbad@gmail.com'],
            #to email
        )


        return render(request, "index.html" , {'user_name' : user_name})
    else:
        return render(request, "index.html")'''
