from django.http import HttpResponse

def hello(request):
    return HttpResponse("来权是个大傻逼！")