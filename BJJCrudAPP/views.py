from django.views.generic import CreateView
from .models import Student
from .forms import StudentForm  # You'll create this form in the next step


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = "your_app_name/student_form.html"  # Replace 'your_app_name' with the actual name of your app
    success_url = "/success/"  # Redirect to this URL after successful form submission
