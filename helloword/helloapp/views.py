from django.http import HttpResponse
from django.shortcuts import render
from .models import place, profil


# Create your views here.
def home(requast):
    obj=place.objects.all()
    obj1=profil.objects.all()
    # name="india"
    return render(requast,'index.html',{'result':obj,'result1':obj1})
# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     res=x+y
#     res1=x*y
#     res2=x-y
#     res3=x/y
#     return render(request,"result.html", {'result':res,'res1':res1,'res2':res2,'res3':res3})

# def about(requast):
#     return HttpResponse('i am about')
#
# def contact(requast):
#     return render(requast,'contact.html')
# def details(requast):
#     return HttpResponse('i am details')
#
# def thanks(requast):
#     return render(requast,'thanks.html')