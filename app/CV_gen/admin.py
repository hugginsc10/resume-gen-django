from django.contrib import admin
from .models import CV_data, Interests, Education, WorkExperience, Skills
# Register your models here.

admin.site.register(CV_data)
admin.site.register(Interests)
admin.site.register(Education)
admin.site.register(WorkExperience)
admin.site.register(Skills)
