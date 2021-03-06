# -*- coding: utf-8 -*-

from itertools import chain

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings

from multiselectfield import MultiSelectField
from phonenumber_field.modelfields import PhoneNumberField


class Area(models.Model):
    area_text = models.CharField(max_length=100)
    symbol = models.CharField(max_length=2)
    overallweight = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])
    
    class Meta:
        ordering = ('symbol',)

    def __str__(self):
        return self.area_text



class Question(models.Model):
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    question_text = models.TextField(blank=True, null=True, max_length=910)
    number = models.IntegerField(null=0)
    weight = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])
    percentage = models.IntegerField(default=0)
   
    class Meta:
        ordering = ('number',)

    def __str__(self):
        return self.question_text
     


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=200)
    score = models.DecimalField(max_digits=5, decimal_places=3, default=0)
    maturity = models.DecimalField(max_digits=5, decimal_places=3, default=0)
   
    class Meta:
        ordering = ('question_id',)

    def __str__(self):
        return "%s - %s - %s" % (self.answer_text, self.score, self.maturity)
       

class ContactDetails(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)
    name = models.CharField(max_length=250)
    email = models.EmailField()
    cell_phone = PhoneNumberField(blank=True)

    def __str__(self):
        return "%s - %s - %s" % (self.name, self.email, self.cell_phone)

class ServiceDescription(models.Model):
     service_description = models.TextField(max_length=250)

     def __str__(self):
        return self.service_description

#class ServiceOwner(models.Model):
 #   public_administration = models.CharField(max_length=250)

 #   def __str__(self):
  #      return self.public_administration

class EndUser(models.Model):
    end_user = models.CharField(max_length=250)

    def __str__(self):
        return self.end_user

class AdministrativeLevel(models.Model):

    ADMINISTRATIVE_LEVEL_LIST = (
        ('local', 'Τοπικό(π.χ.πόλη, δήμος)'),
        ('regional', 'Περιφερειακό'),
        ('national', 'Εθνικό'),
        ('european', 'Ευρωπαϊκό'),
        ('international', 'Διεθνές')
    )
    administrative_level = MultiSelectField(max_length=50, choices=ADMINISTRATIVE_LEVEL_LIST, null=True, blank=True)

   

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
 


class ServiceOwnerOption(models.Model):
    option_text = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.option_text

class ServiceOwner(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)
    service_owner = models.ForeignKey(ServiceOwnerOption, null=True, blank=True)



class ConsumedService(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True)
    maturity_level = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])

    def __str__(self):
        return self.name



class ServiceConsumption(models.Model):
    CONSUMED_SERVICES_OPTIONS = (
        ('authentication_service', 'Υπηρεσία Αυθεντικοποίησης'),
        ('e_signature_service', 'Υπηρεσία Ηλεκτρονικών Υπογραφών'),
        ('e_payment_service', 'Υπηρεσία Ηλεκτρονικών Πληρωμών'),
        ('messaging_service', 'Yπηρεσία Μηνυμάτων'),
        ('audio_visual_service', 'Υπηρεσία Οπτικοακουστικών Μέσων'),
        ('data_transformation_service', 'Υπηρεσία Μετασχηματισμού Δεδομένων'),
        ('data_validation_service', 'Υπηρεσία Επικύρωσης Δεδομένων'),
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
        ('specific_services', 'Άλλες Εξειδικευμένες Υπηρεσίες'),
    )
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)
    service_consumption = MultiSelectField(max_length=250, choices= CONSUMED_SERVICES_OPTIONS, null=True)


class ReuseAndSharing(models.Model):
    REUSE_SHARING_OPTIONS = (
        ('1', 'Ανταλλαγή τεκμηρίωσης για την παροχή σε άλλους (σχετιζόμενους) οργανισμούς πολύτιμων πληροφοριών σχετικά με τις διαδικασίες, την οργάνωση, τη διακυβέρνηση, τις επιλογές τεχνολογίας κλπ.'),
        ('2', 'Κοινή χρήση πηγαίου κώδικα ή λογισμικού με δυνατότητα λήψης για να δοθεί η δυνατότητα σε άλλες οργανώσεις να δημιουργήσουν αποτελεσματικά τις υπηρεσίες τους.'),
        ('3', 'Δημιουργία διαθέσιμων υπηρεσιών Web-API για να δοθεί η δυνατότητα σε άλλους οργανισμούς και ιδιώτες  να (επανα-)χρησιμοποιήσουν τη λειτουργικότητα ή / και να αποκτήσουν πρόσβαση σε δεδομένα μέσω διαδικτύου και / ή εφαρμογών για κινητά.'),
        ('4', 'Παροχή υποστήριξης σε οργανισμούς που αξιοποιούν τους πόρους που παρέχονται.'),
        ('5', 'Κανένα από τα παραπάνω.'),
    )
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)
    reuse_and_sharing = MultiSelectField(max_length=250, choices= REUSE_SHARING_OPTIONS, max_choices=4, null=True)
    maturity = models.DecimalField(max_digits=5, decimal_places=3, default=0)

   
 
        

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
