from django.http import HttpResponse

def hello(request):
    print("========")
    print(request)
    print("========")
    print(dir(request))
    print("========")
    print(request.COOKIES)
    print("========")
    return (HttpResponse("<h1>Hello</h1>"))
