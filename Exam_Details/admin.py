from django.contrib import admin
from .models import ExamIndex,ExamDetails


class ExamDetailsInline(admin.StackedInline):  # You can also use admin.StackedInline for a different display style
    model = ExamDetails
    extra = 1  # The number of empty forms to display
    max_num=1


class ExamIndexAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['exam_name', 'university','exam_date','slug']}),
    ]
    prepopulated_fields = {
        "slug": ("exam_name",),
    }
    inlines = [ExamDetailsInline]
    ExamIndex._meta.verbose_name = "Exam Details"


# Register your models here.
admin.site.register(ExamIndex, ExamIndexAdmin)
