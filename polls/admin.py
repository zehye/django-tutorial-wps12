from django.contrib import admin


from .models import Question, Choice


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text']
    fieldsets = [
        ('Question text', {'fields':['question_text']}),
        ('Date information', {'fields':['pub_date']}),
    ]


# class ChoiceInline(admin.StackedInline):
#     model = Choice
#     extra = 3


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    pass
