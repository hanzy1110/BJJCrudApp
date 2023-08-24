from django.views.generic import CreateView
from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt
from .models import Student
from .forms import StudentForm  # You'll create this form in the next step


@csrf_exempt
class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = (
        # "student_form.html"
        "new_student_form.html"
    )
    success_url = "/success/"  # Redirect to this URL after successful form submission


def registration_successful_view(request):
    return render(request, "success.html")
