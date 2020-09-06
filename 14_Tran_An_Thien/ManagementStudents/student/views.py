from django.shortcuts import render, redirect, HttpResponse
from student.forms import StudentsForm
from student.models import Students


def std(request):
    if request.method == "POST":
        form = StudentsForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/')
            except:
                pass
    else:
        form = StudentsForm()
    return render(request, 'student/home.html', {'form': form})


def view(request):
    students = Students.objects.all()
    return render(request, 'view.html', {'students': students})


def delete(request, id):
    students = Students.objects.get(id=id)
    students.delete()
    return redirect("/")


def edit(request, id):
    students = Students.objects.get(id=id)
    return render(request, 'edit.html', {'students': students})


# Create your views here.


def home(request):
    # return render(request, 'student/home.html')
    students = Students.objects.all()
    return render(request, 'student/home.jinja2', {'students': students})


def about(request):
    return render(request, 'student/testjinja2.jinja', {'title': 'about'})
