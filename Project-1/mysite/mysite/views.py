from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello Kedar!!")

def about(request):
    return HttpResponse("This is about Kedar")