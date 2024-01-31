from django.contrib import admin

from .models import ExamDetails, ExamIndex


class ExamDetailsInline(admin.StackedInline):  
    model = ExamDetails
    extra = 1  # The number of empty forms to display
    max_num=1


class ExamIndexAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['exam_name','slug', 'university','exam_date']}),
    ]
    prepopulated_fields = {
        "slug": ("exam_name",),
    }
    list_filter = ('university',"exam_date")
    inlines = [ExamDetailsInline]




admin.site.site_header = "Exam Details Admin"
admin.site.site_title = "Exam Details Admin Portal"
admin.site.index_title = "Welcome to Exam Details Portal"
admin.site.register(ExamIndex, ExamIndexAdmin)