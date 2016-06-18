from django.shortcuts import render
from models import Student, Grades
from django.http.response import HttpResponseRedirect
# Create your views here.

def home(request):
	return render(request, 'storeinfo.html')

def StoreInfo(request):
	if request.method == 'POST':
		first_name = request.POST.get('first_name')
		last_name = request.POST.get('last_name')
		age = request.POST.get('age')
		gender = request.POST.get('gender')
		sgpa = request.POST.get('sgpa')
		cgpa = request.POST.get('cgpa')

		Student.objects.create(first_name=first_name,last_name=last_name,age=age,gender=gender)
		student_object = Student.objects.get(first_name=first_name,last_name=last_name)
		Grades.objects.create(student=student_object,sgpa=sgpa,cgpa=cgpa)

		return HttpResponseRedirect('/display-info/')

def DisplayInfo(request):
	grade_object = Grades.objects.all()

	return render(request, 'displayinfo.html', {'grades': grade_object})
