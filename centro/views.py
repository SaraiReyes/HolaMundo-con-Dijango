from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. Mi primer hola con Django")