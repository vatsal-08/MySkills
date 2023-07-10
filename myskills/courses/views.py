from django.shortcuts import redirect, render
from .models import Course
from django.shortcuts import get_object_or_404
import os
from django.db.models import Q
from django.contrib import messages
from django.urls import reverse

def delete_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)

def truncate_text(text, max_length):
    if len(text) > max_length:
        truncated_text = text[:max_length] + "..."
    else:
        truncated_text = text
    return truncated_text

def index(request):
    return redirect("courses")

def search_view(request):
    query = request.GET.get('query')
    if query:
        condition = Q(name__icontains=query) | Q(description__icontains=query)
        courses = Course.objects.filter(condition)  
        context={
            'query':query,
            'courses':courses
        }
        return render(request,'courses/search.html',context)
    return redirect('courses')


def about(request):
    return render(request, 'courses/about-me.html')

def list_view(request):
    courses = Course.objects.all()
    context = {"courses": courses}
    create_view_url = reverse('create-view')
    add_course_button = f'<a href="{create_view_url}"><i class="fa-solid fa-circle-plus"></i></a>'
    if not request.user.is_authenticated or not request.user.is_superuser:
        add_course_button=""
    context["add_course_button"]=add_course_button
    return render(request, 'courses/home.html', context)


def course_detail(request, pk):
    try:
        course = Course.objects.get(pk=pk)
        context = {'course': course}
        return render(request, 'courses/detail.html', context)
    except Course.DoesNotExist:
        messages.error(request, "Course does not exist.")
        return redirect('courses')

def create_view(request):
    if not request.user.is_authenticated or not request.user.is_superuser:
        messages.error(request,"You are not authorised")
        return redirect('courses')
    if request.method == 'POST':
        name = request.POST.get('name')
        cost = request.POST.get('cost')
        uploadimg = request.FILES['uploadimg']
        pdfupload = request.FILES['pdfupload']
        description = request.POST.get('description')
        if name and cost and uploadimg and pdfupload and description:
            obj = Course(name=name, cost=cost, img=uploadimg, pdf_file=pdfupload, description=description)
            obj.save()
            return redirect('/')
    return render(request, "courses/new_courses_add.html")

def update_course(request, pk):
    if not request.user.is_authenticated or not request.user.is_superuser:
        messages.error(request,"You are not authorised")
        return redirect('courses')
    try:
        course = Course.objects.get(pk=pk)
        img_file_name = course.img.name.split("/")[-1]
        pdf_file_name = course.pdf_file.name.split("/")[-1]

        if request.method == 'POST':
            action = request.POST.get('update-button')
            if action == "cancel":
                return redirect('courses')
            name = request.POST.get('name')
            cost = request.POST.get('cost')
            description = request.POST.get('description')
            course.name = name
            course.cost = cost
            course.description = description
            if 'uploadimg' in request.FILES:
                try:
                    uploaded_img = request.FILES['uploadimg']

                    if course.img:
                        delete_file(course.img.path)

                    course.img = uploaded_img
                except Exception as e:
                    message=f"Error uploading image: {str(e)}"
                    messages.error(request,message)
                    return redirect('courses')

            if 'pdfupload' in request.FILES:
                try:
                    uploaded_pdf = request.FILES['pdfupload']

                    if course.pdf_file:
                        delete_file(course.pdf_file.path)

                    course.pdf_file = uploaded_pdf
                except Exception as e:
                    message=f"Error uploading PDF: {str(e)}"
                    messages.error(request,message)
                    return redirect('courses')

            course.save()
            messages.success(request,"Successfully updated the course")
            return redirect('courses')

        pdf_file_name, extension1 = os.path.splitext(pdf_file_name)
        pdf_file_name = truncate_text(pdf_file_name, 15) + extension1
        
        img_file_name, extension2 = os.path.splitext(img_file_name)
        img_file_name = truncate_text(img_file_name, 15) + extension2

        context = {
            "course": course,
            "pdf_file_name": pdf_file_name,
            "img_file_name": img_file_name
        }
        return render(request, 'courses/course_update.html', context)
    except Course.DoesNotExist:
        messages.error(request,"Invalid link")
        return redirect("courses")

def delete_course(request, pk):
    if not request.user.is_authenticated or not request.user.is_superuser:
        messages.error(request,"You are not authorised")
        return redirect('courses')
    course = get_object_or_404(Course, pk=pk)

    if request.method == 'POST':
        action = request.POST.get('course-delete-name')

        if action == 'yes':
            if course.pdf_file:
                delete_file(course.pdf_file.path)

            if course.img:
                delete_file(course.img.path)

            course.delete()

        return redirect('courses')

    return render(request, "courses/course_delete.html", context={"course": course})

