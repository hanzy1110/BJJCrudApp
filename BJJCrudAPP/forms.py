import re
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Row, Column
from .models import Student

from datetime import date

# gender => age_class => max_weight
CATEGORIES = {
    "m": {
        "adulto": {
            57.5: "gallo",
            64: "pluma",
            70: "pena",
            76: "leve",
            82.3: "medio",
            88.3: "medio pesado",
            94.3: "pesado",
            100.5: "super pesado",
            -1: "Pesadisimo",
        },
        "master": {
            57.5: "gallo",
            64: "pluma",
            70: "pena",
            76: "leve",
            82.3: "medio",
            88.3: "medio pesado",
            94.3: "pesado",
            100.5: "super pesado",
            -1: "Pesadisimo",
        },
        "juveniles": {
            53.5: "gallo",
            58.5: "pluma",
            64: "pena",
            69: "leve",
            74: "medio",
            79.3: "medio pesado",
            84.3: "pesado",
            89.5: "super pesado",
            -1: "Pesadisimo",
        },
    },
    "f": {
        "adulto": {
            48.5: "gallo",
            53.5: "pluma",
            58.5: "pena",
            64: "leve",
            69: "medio",
            74: "medio pesado",
            79.3: "pesado",
            100.5: "super pesado",
        },
        "master": {
            48.5: "gallo",
            53.5: "pluma",
            58.5: "pena",
            64: "leve",
            69: "medio",
            74: "medio pesado",
            79.3: "pesado",
            100.5: "super pesado",
        },
        "juveniles": {
            53.5: "gallo",
            58: "pluma",
            64: "pena",
            69: "leve",
            74: "medio",
            79.3: "medio pesado",
            84.3: "pesado",
            -1: "super pesado",
        },
    },
}

AGE_CATEGORIES = {
    7: "infantiles",
    18: "juveniles",
    30: "adulto",
    36: "master",
    41: "master1",
    46: "master2",
}


def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


def assign_class(instance: Student):
    age = calculate_age(instance.date_of_birth)

    age_class = ""
    age_limits = list(AGE_CATEGORIES.keys())
    for i, age_limit in enumerate(age_limits):
        if age < age_limit:
            age_class = AGE_CATEGORIES[age_limits[i]]
            break

    if "master" in age_class:
        age_class = age_class.replace("1", "").replace("2", "")
        weigth_class = CATEGORIES[instance.gender][age_class]
    else:
        weigth_class = CATEGORIES[instance.gender][age_class]

    w_denomination = ""
    for weigth_limit, weigth_denomination in weigth_class.items():
        if instance.weight < weigth_limit:
            w_denomination = weigth_denomination
            break

    print("AGE => ", age)
    print("WEIGTH CLASS  => ", weigth_class)

    instance.weight_class = w_denomination
    instance.age_class = age_class

    return instance


class StudentForm(forms.ModelForm):
    date_of_birth = forms.DateField(
        label="Fecha de Nacimiento",
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date"}),
    )
    belt_colour = forms.ChoiceField(choices=Student.BELT_COLORS)

    class Meta:
        model = Student
        fields = (
            "name",
            "surname",
            "date_of_birth",
            "personal_id",
            "belt_colour",
            "weight",
            "gender",
            "academy",
            "absoluto",
        )
        # exclude = ("monto_pago",)

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column("name", css_class="col-md-8"),
                Column("surname", css_class="col-md-8"),
            ),
            Row(
                Column("date_of_birth", css_class="col-md-8"),
            ),
            Row(
                Column("personal_id", css_class="col-md-8"),
            ),
            Row(
                Column("weight", css_class="col-md-6"),
                Column("gender", css_class="col-md-6"),
            ),
            Row(
                Column("belt_colour", css_class="col-md-8"),
            ),
            Row(
                Column("academy", css_class="col-md-6"),
                Column("absoluto", css_class="col-md-6"),
            ),
        )
        self.helper.form_class = "form-control form-control-lg"
        self.helper.label_class = "form-label"
        self.helper.field_class = "col-md-8"
        self.helper.add_input(Submit("submit", "Submit", css_class="btn-primary"))
        self.helper.form_method = "POST"
        # self.helper.add_input(forms.Submit("submit", "Save"))

    def is_valid(self):
        validation = super().is_valid()

        print(self.data)
        print(self.errors)
        return validation

    def save(self, commit=True):
        instance = super().save(commit=False)
        if instance.date_of_birth and instance.weight:
            instance = assign_class(instance)
        if commit:
            instance.save()
        return instance
