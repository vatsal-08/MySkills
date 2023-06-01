from django.shortcuts import redirect, render
from .models import Course
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
import os

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
    return redirect("courses/")

def about(request):
    return render(request, 'courses/about-me.html')

def list_view(request):
    courses = Course.objects.all()
    context={'courses':courses,"add_course":""}
    if request.user.is_authenticated:
        if request.user.is_superuser:
            context["add_course"] = '<a href="{% url \'create-view\' %}"><i class="fa-solid fa-circle-plus"></i></a>'
    return render(request,'courses/home.html',context)

@login_required
def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    context = {'course': course}
    return render(request, 'courses/detail.html', context)

def create_view(request):
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
    course = get_object_or_404(Course, pk=pk)
    img_file_name = course.img.name.split("/")[-1]
    pdf_file_name = course.pdf_file.name.split("/")[-1]

    if request.method == 'POST':
        action = request.POST.get('update-button')

        if action == "cancel":
            return redirect('courses')

        name = request.POST.get('name')
        cost = request.POST.get('cost')
        description = request.POST.get('description')

        # Update course fields
        course.name = name
        course.cost = cost
        course.description = description

        # Handle image upload
        if 'uploadimg' in request.FILES:
            try:
                uploaded_img = request.FILES['uploadimg']

                if course.img:
                    delete_file(course.img.path)

                course.img = uploaded_img
            except Exception as e:
                # Handle the exception (e.g., log the error, display a message)
                print(f"Error uploading image: {str(e)}")

        # Handle PDF upload
        if 'pdfupload' in request.FILES:
            try:
                uploaded_pdf = request.FILES['pdfupload']

                if course.pdf_file:
                    delete_file(course.pdf_file.path)

                course.pdf_file = uploaded_pdf
            except Exception as e:
                # Handle the exception (e.g., log the error, display a message)
                print(f"Error uploading PDF: {str(e)}")

        # Save the updated course
        course.save()

        return redirect('courses')

    # Truncate file names for display
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


import os

def delete_course(request, pk):
    course = get_object_or_404(Course, pk=pk)

    if request.method == 'POST':
        action = request.POST.get('course-delete-name')

        if action == 'yes':
            # Remove the PDF file
            if course.pdf_file:
                delete_file(course.pdf_file.path)

            # Remove the image file
            if course.img:
                delete_file(course.img.path)

            # Delete the course
            course.delete()

        return redirect('courses')

    return render(request, "courses/course_delete.html", context={"course": course})

