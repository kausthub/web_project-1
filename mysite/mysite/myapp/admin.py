

from django.contrib import admin

from .models import ChoiceMain , Question , Subject , result_final

class QuestionInLine(admin.StackedInline):
    model = Question
    extra = 3


class SubjectAdmin(admin.ModelAdmin):
    fieldsets = [
        (Subject,               {'fields': ['subject_code']}),

    ]
    inlines = [QuestionInLine,]


class resultadmin(admin.ModelAdmin):
    readonly_fields = ['name','subject','q1','q2','q3','q4','q5','q6','q7','q8','q9','q10','q11','q12','q13','q14','q15','q16','q17','q18','q19','q20']
    list_filter = ('subject',)

    def name(self, obj):
        if obj.name:
            return obj.name
        else:
            return 'N/A'

admin.site.register(Subject, SubjectAdmin)
admin.site.register(ChoiceMain)
admin.site.register(result_final,resultadmin)