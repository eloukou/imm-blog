from django.contrib import admin

from .models import *

admin.site.register(Area)

admin.site.register(Answer)

admin.site.register(ContactDetails)

admin.site.register(ServiceDescription)

admin.site.register(ServiceOwner)

admin.site.register(ServiceOwnerOption)
 
admin.site.register(EndUser)

admin.site.register(AdministrativeLevel)

admin.site.register(DeliveryChannel)

admin.site.register(ConsumedService)
admin.site.register(ServiceConsumption)
admin.site.register(ReuseAndSharing)
admin.site.register(Consumption)

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Ενότητα: ', {'fields': ['area']}),
        ('Ερώτηση: ', {'fields': ['number','question_text']}),
        ('Βάρος: ', {'fields': ['weight']}),
        ('Ποσοστό: ', {'fields': ['percentage']})
    ]
    inlines = [AnswerInline]
admin.site.register(Question, QuestionAdmin)


