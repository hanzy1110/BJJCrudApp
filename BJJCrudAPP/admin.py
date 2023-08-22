from django.contrib import admin
from .models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = (
        "personal_id",
        "full_name",
        "date_of_birth",
        "belt_colour",
        "weight",
        "gender",
        "academy",
        "age_class",
        "weight_class",
        "monto_pago",
        "absoluto",
    )

    def full_name(self, obj):
        return f"{obj.name} {obj.surname}"

    full_name.short_description = "Nombre Completo"


# admin.site.register(models.Verificaciones, VerificacionesFilter)
admin.site.register(Student, StudentAdmin)
