from django.shortcuts import render,redirect
from .models import Student
from django.http import HttpResponse
from django.views import View
# Create your views here.
class Home(View):
    def get(self,request):
        return render(request,'home.html')
class InsertInput(View):
    def get(self,request):
        return render(request,'studentinput.html')
class Insert(View):
    def get(self,request):
        s_id=int(request.GET["t1"])
        s_name=request.GET["t2"]
        s_class=int(request.GET["t3"])
        s_jd=request.GET["t4"]
        s_cd=request.GET["t5"]
        s=Student(sid=s_id,sname=s_name,sclass=s_class,sjd=s_jd,scd=s_cd)
        s.save()
        return HttpResponse("student inserted successfully")
class Display(View):
    def get(self,request):
        qs=Student.objects.all()
        condic={"records":qs}
        return render(request,'display.html',context=condic)
class DeleteInput(View):
    def get(self,request):
        qs = Student.objects.all()
        condic = {"records": qs}
        return render(request, 'deleteinput.html', context=condic)
class Delete(View):
    def get(self,request):
        s_id=int(request.GET["t1"])
        s=Student.objects.get(sid=s_id)
        s.delete()
        return redirect('/studentapp/display')
class UpdateInput(View):
    def get(self,request):
        qs = Student.objects.all()
        condic = {"records": qs}
        return render(request, 'updateinput.html', context=condic)
class UpdateDetails(View):
    def get(self,request):
        s_id=int(request.GET["t1"])
        prod=Student.objects.get(sid=s_id)
        condic={'rec':prod}
        return render(request,'update.html',context=condic)
class Update(View):
    def get(self,request):
        s_id=int(request.GET["t1"])
        prod=Student.objects.get(sid=s_id)
        prod.sname=request.GET["t2"]
        prod.sclass=float(request.GET["t3"])
        prod.sjd=request.GET["t4"]
        prod.scd=request.GET["t5"]
        prod.save()
        return redirect('/studentapp/display')
