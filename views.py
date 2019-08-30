from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    my_dictionary = {'insert_me':" I am from another galaxy"}
    return render(request,'second_app/project1.html',context=my_dictionary)


def contact(request):
    return render(request,'second_app/contact.html')
