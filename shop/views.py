from django.shortcuts import redirect, render
from .models import Prof
from .models import Contact

# Create your views here.
def homepg(request):
    return render(request,"homepg.html")
def contact(request):
    if request.method=='POST':
        a=request.POST.get("username")
        b=request.POST.get("contactnumber")
        c=request.POST.get("email")
        d=request.POST.get("message")
        e=Contact(username=a,contactnumber=b,email=c,message=d)
        e.save()
        return redirect("/home")
    return render(request,"contactus.html")
def profile(request):
    if request.method=='POST':
        a=request.FILES.get("photo")
        b=request.POST.get("username")
        c=request.POST.get("phnumber")
        d=request.POST.get("address")
        e=request.POST.get("postcode")
        f=Prof(profile_photo=a,username=b,phone_number=c,address=d,postal_code=e)
        f.save()
        return redirect("/home")
    return render(request,"profelec.html")
