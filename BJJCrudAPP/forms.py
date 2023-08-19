from django import forms
from .models import Student
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column


class StudentForm(forms.ModelForm):
    date_of_birth = forms.DateField()

    class Meta:
        model = Student
        fields = "__all__"  # You can customize this if you don't want to include all fields in the form
        exclude = ("monto_pago",)

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column("date_of_birth", css_class="col-md-4"),
                Column("personal_id", css_class="col-md-4"),
                Column("belt_colour", css_class="col-md-4"),
            ),
            Row(
                Column("weight", css_class="col-md-6"),
                Column("academy", css_class="col-md-6"),
            ),
            Row(
                Column("submit", css_class="col-md-12 text-center"),
            ),
        )
