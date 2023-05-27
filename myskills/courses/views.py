from django.shortcuts import redirect, render
from django.views.generic import  ListView,DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Course
from django.shortcuts import get_object_or_404

def index(request):
    return redirect("courses/")

def about(request):
    return render(request,'courses/about-me.html')

class CourseList(ListView):
    model = Course
    template_name="courses/home.html"
    context_object_name='courses'

class CourseDetail(LoginRequiredMixin,DetailView):
    model = Course
    template_name="courses/detail.html"
    context_object_name='course'

class CourseUpdateView(UpdateView):
    model = Course
    template_name = "course/update.html"
    context_object_name='course'

def create_view(request):
    if request.method=='POST':
        name = request.POST['name']
        cost = request.POST['cost']
        uploadimg = request.FILES['uploadimg']
        pdfupload = request.FILES['pdfupload']
        description = request.POST['description']
        if name and cost and uploadimg and pdfupload and description:
            obj = Course(name=name,cost=cost,img=uploadimg,pdf_file=pdfupload,description=description)
            obj.save()
            return redirect('/')
    return render(request,"courses/new_courses_add.html")

def update_course(request,pk):
    course = get_object_or_404(Course,pk=pk)
    if request.method=='POST':
        action = request.POST['update-button']
        if action=="cancel":
            return redirect('courses')
        name = request.POST['name']
        cost = request.POST['cost']
        description = request.POST['description']
        course.name=name
        course.cost=cost
        course.description=description
        if 'uploadimg' in request.FILES:
            uploaded_img = request.FILES['uploadimg']
            course.img = uploaded_img
        if 'pdfupload' in request.FILES:
            uploaded_pdf = request.FILES['pdfupload']
            course.pdf_file = uploaded_pdf
        course.save()
        return redirect('courses')
    context={
        course:course
    }
    return render(request,'courses/course_update.html',{'course':course})

def delete_course(request,pk):
    course = get_object_or_404(Course,pk=pk)
    if request.method=='POST':
        action = request.POST['course-delete-name']
        if action=='yes':
            course.delete()
        return redirect('courses')
    return render(request,"courses/course_delete.html",context = {"course":course})
