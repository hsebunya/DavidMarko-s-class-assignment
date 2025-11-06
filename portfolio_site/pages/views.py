from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')
def index(request):
    if request.method== 'POST':
        body=request.POST
        student_name = body.get("student_name")
        tagline = body.get("tagline")
    context = {
        "Student_name": student_name,
        "Tagline": tagline,
    }
    return render(request,'index.html',context)
  
def education(request):
    if request.method== 'POST':
        body=request.POST
        School_name = body.get("School_name")
        Graduation_year = body.get("Graduation_year")
    context = {
        "School_name": School_name,
        "Graduation_year": Graduation_year,
    }
    return render(request,'education.html',context)

def create_id (request):
    return render (request, "create_id.html")
def create_id(request):
    return render(request, "create_id.html")
