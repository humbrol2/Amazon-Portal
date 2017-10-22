from django.contrib import admin
from .models import facilityGoal, coaEntry, coaQuestionBank


# Register your models here.
admin.site.register(facilityGoal)
admin.site.register(coaEntry)
admin.site.register(coaQuestionBank)
