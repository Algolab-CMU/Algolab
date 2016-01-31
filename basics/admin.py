from django.contrib import admin
from .models import Question, Answer, Class, Comment, UserProfile, Tag, Choice

# Register your models here.
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Class)
admin.site.register(Comment)
admin.site.register(UserProfile)
admin.site.register(Tag)
admin.site.register(Choice)
