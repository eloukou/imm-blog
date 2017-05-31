from django.contrib import admin

from .models import *


#admin.site.register(Post)

admin.site.register(Area)

admin.site.register(Answer)

#admin.site.register(ServiceLandscape)

admin.site.register(ContactDetails)

admin.site.register(ServiceDescription)

admin.site.register(ServiceOwner)
 
admin.site.register(EndUser)

admin.site.register(AdministrativeLevel)


#admin.site.register(AccessibilityOption)
#admin.site.register(PreFillingFormsOption)
#admin.site.register(MultillingualismOption)
#admin.site.register(CrossReferencingOption)
#admin.site.register(ServiceCatalogueOption)
#admin.site.register(ServiceDelivery)
#admin.site.register(ConsumedService)
#admin.site.register(SpecificServicesList)
#admin.site.register(Consumption)

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Ενότητα: ', {'fields': ['area']}),
        ('Ερώτηση: ', {'fields': ['number','question_text']}),
        ('Βάρος: ', {'fields': ['weight']})
    ]
    inlines = [AnswerInline]
admin.site.register(Question, QuestionAdmin)

#class SpecificServicesListInline(admin.TabularInline):
#    model = SpecificServicesList

#class LandscapingServiceConsumptionAdmin(admin.ModelAdmin):
#    inlines = [
#        SpecificServicesListInline
#    ]
#admin.site.register(LandscapingServiceConsumption, LandscapingServiceConsumptionAdmin)
