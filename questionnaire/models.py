# -*- coding: utf-8 -*-

from itertools import chain

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings

from multiselectfield import MultiSelectField



class Area(models.Model):
    area_text = models.CharField(max_length=100)
    symbol = models.CharField(max_length=2)
    overallweight = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])
    
    class Meta:
        ordering = ('symbol',)

    def __str__(self):
        return self.area_text

    @property
    def overall_maturity_scoring(self):

        for q in self.area.question_set.all():
            overall_maturity_scoring += area.overallweight * area.question.maturity_scoring
            print(q)
        return overall_maturity_scoring


class Question(models.Model):
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=300)
    number = models.IntegerField(null=0)
    weight = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])
   
    class Meta:
        ordering = ('number',)

    def __str__(self):
        return self.question_text
 
    @property
    def maturity_scoring(self):
        q = question.weight * question.answer.score

        return q


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=200)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.answer_text

   
  

class ContactDetails(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)
    name = models.CharField(max_length=250)
    email = models.EmailField()
    cell_phone = models.CharField(max_length=250)

    def __str__(self):
        return "%s - %s - %s" % (self.name, self.email, self.cell_phone)

class ServiceDescription(models.Model):
     service_description = models.CharField(max_length=250)

     def __str__(self):
        return self.service_description

class ServiceOwner(models.Model):
    public_administration = models.CharField(max_length=250)

    def __str__(self):
        return self.public_administration

class EndUser(models.Model):
    end_user = models.CharField(max_length=250)

    def __str__(self):
        return self.end_user

class AdministrativeLevel(models.Model):
    LOCAL = 'local'
    REGIONAL = 'regional'
    NATIONAL = 'national'
    EUROPEAN = 'european'
    INTERNATIONAL = 'international'

    ADMINISTRATIVE_LEVEL_CHOICES = (
        (LOCAL, 'Τοπικό(π.χ.πόλη, δήμος)'),
        (REGIONAL, 'Περιφερειακό'),
        (NATIONAL, 'Εθνικό'),
        (EUROPEAN, 'Ευρωπαϊκό'),
        (INTERNATIONAL, 'Διεθνές')
    )
    main_administrative_level = models.CharField(max_length=250, choices=ADMINISTRATIVE_LEVEL_CHOICES, default=LOCAL)
    alternative_administrative_level = models.CharField(max_length=250, choices=ADMINISTRATIVE_LEVEL_CHOICES, default=LOCAL)

    def __str__(self):
        return "%s - %s" % (self.main_administrative_level, self.alternative_administrative_level)


class DeliveryChannel(models.Model):
    TRADITIONAL_DELIVERY_CHANNELS_LIST = (
        ('counter_desk', 'Γραφείο/κισέ'),
        ('postal', 'Ταχυδρομικά'),
        ('telephone', 'Τηλεφωνικά')
    )
    DIGITAL_DELIVERY_CHANNELS_LIST = (
        ('dedicated_app', 'Ειδική εφαρμογή'),
        ('website_portal', 'Διαδίκτυο και/ή Διαδικτυακή πύλη'),
        ('portal', 'Διαδικτυακή πύλη')
    )

    TOTAL_OPTIONS = set(chain(TRADITIONAL_DELIVERY_CHANNELS_LIST, DIGITAL_DELIVERY_CHANNELS_LIST))

    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    traditional_channel = MultiSelectField(max_length=150, choices=TRADITIONAL_DELIVERY_CHANNELS_LIST, null=True, blank=True)
    digital_channel = MultiSelectField(max_length=150, choices=DIGITAL_DELIVERY_CHANNELS_LIST, null=True, blank=True)
 


class AccessibilityOption(models.Model):
    option_text = models.CharField(max_length=300, null=True, blank=True)
    score = models.IntegerField(null=0)

    def __str__(self):
        return self.option_text

class Accessibility(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    accessibility = models.ForeignKey(AccessibilityOption)
    accessibility_weight = models.FloatField()

    def __str__(self):
        return self.accessibility


class ConsumedService(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True)
    maturity_level = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])

    def __str__(self):
        return self.name

class SpecificServicesList(models.Model):
    service_name = models.CharField(max_length=150, null=True, blank=True)
    landscaping_service_consumption = models.ForeignKey("LandscapingServiceConsumption", null=True)

    def __str__(self):
        return self.service_name


class LandscapingServiceConsumption(models.Model):
    GENERIC_SERVICES_LIST = (
        ('authentication_service', 'Υπηρεσία Αυθεντικοποίησης'),
        ('e_signature_service', 'Υπηρεσία Ηλεκτρονικών Υπογραφών'),
        ('e_payment_service', 'Υπηρεσία Ηλεκτρονικών Πληρωμών'),
        ('messaging_service', 'Yπηρεσία Μηνυμάτων'),
        ('audio_visual_service', 'Υπηρεσία Οπτικοακουστικών Μέσων'),
        ('data_transformation_service', 'Υπηρεσία Μετασχηματισμού Δεδομένων'),
        ('machine_translation_service', 'Υπηρεσία Αυτόματης Μετάφρασης'),
        ('data_exchange_service', 'Υπηρεσία Ανταλλαγής Δεδομένων'),
        ('business_analytics_service', 'Υπηρεσία Επιχειρηματικής Ανάλυσης'),
        ('business_reporting_service', 'Υπηρεσία Αναφοράς Επιχειρήσεων'),
        ('forms_management_service', 'Υπηρεσία Διαχείρισης Φορμών'),
        ('records_management_service', 'Υπηρεσία Διαχείρισης Αρχείων'),
        ('document_management_service', 'Υπηρεσία Διαχείρισης Εγγράφων'),
        ('content_management_service', 'Υπηρεσία Διαχείρισης Περιεχομένου'),
        ('access_management_service', 'Υπηρεσία Διαχείρισης Πρόσβασης'),
        ('logging_service', 'Υπηρεσία Σύνδεσης'),
        ('audit_service', 'Υπηρεσία Ελέγχου'),
        ('metadata_management_service', 'Υπηρεσία Διαχείρισης Μεταδεδομένων'),
        ('networking_service', 'Υπηρεσία Δικτύωσης'),
        ('hosting_service', 'Υπηρεσία Φιλοξενίας'),
        ('storage_service', 'Υπηρεσία Αποθήκευσης'),
        ('base_registry_information_source', 'Υπηρεσία Πληροφοριών Μητρώου'),
    )
    CONSUMED_SERVICES_OPTIONS = set(GENERIC_SERVICES_LIST)

    landscaping_service_consumption = MultiSelectField(max_length=250, choices=CONSUMED_SERVICES_OPTIONS, null=True)
    consumed_service_maturity_level = models.FloatField()

    def __str__(self):
        return self.id

    def __unicode__(self):
        return str(self.id)

    @property
    def consumed_services(self):
        return self.specificserviceslist_set.all()


class Consumption(models.Model):
    service_consumed_today = models.CharField(max_length=120, null=False, blank=False)
    reusing_of_services = models.CharField(max_length=120, null=True, blank=True)
    processing_mode = models.CharField(max_length=120, null=True, blank=True)
    push_pull_mechanisms = models.CharField(max_length=120, null=True, blank=True)
    common_protocol_usage = models.CharField(max_length=120, null=True, blank=True)
    reuse_of_network = models.CharField(max_length=120, null=True, blank=True)
    semantic_alignment = models.CharField(max_length=120, null=True, blank=True)
    exception_handling = models.CharField(max_length=120, null=True, blank=True)
    certification = models.CharField(max_length=120, null=True, blank=True)
    specification_process = models.CharField(max_length=120, null=True, blank=True)

    def __str__(self):
        return self.service_consumed_today
