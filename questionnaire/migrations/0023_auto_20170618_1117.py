# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-18 08:17
from __future__ import unicode_literals

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0022_auto_20170614_2304'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='specificserviceslist',
            name='landscaping_service_consumption',
        ),
        migrations.RemoveField(
            model_name='landscapingserviceconsumption',
            name='consumed_service_maturity_level',
        ),
        migrations.AlterField(
            model_name='administrativelevel',
            name='administrative_level',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('local', 'Τοπικό(π.χ.πόλη, δήμος)'), ('regional', 'Περιφερειακό'), ('national', 'Εθνικό'), ('european', 'Ευρωπαϊκό'), ('international', 'Διεθνές')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='landscapingserviceconsumption',
            name='landscaping_service_consumption',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('authentication_service', 'Υπηρεσία Αυθεντικοποίησης'), ('e_signature_service', 'Υπηρεσία Ηλεκτρονικών Υπογραφών'), ('e_payment_service', 'Υπηρεσία Ηλεκτρονικών Πληρωμών'), ('messaging_service', 'Yπηρεσία Μηνυμάτων'), ('audio_visual_service', 'Υπηρεσία Οπτικοακουστικών Μέσων'), ('data_transformation_service', 'Υπηρεσία Μετασχηματισμού Δεδομένων'), ('data_validation_service', 'Υπηρεσία Επικύρωσης Δεδομένων'), ('machine_translation_service', 'Υπηρεσία Αυτόματης Μετάφρασης'), ('data_exchange_service', 'Υπηρεσία Ανταλλαγής Δεδομένων'), ('business_analytics_service', 'Υπηρεσία Επιχειρηματικής Ανάλυσης'), ('business_reporting_service', 'Υπηρεσία Αναφοράς Επιχειρήσεων'), ('forms_management_service', 'Υπηρεσία Διαχείρισης Φορμών'), ('records_management_service', 'Υπηρεσία Διαχείρισης Αρχείων'), ('document_management_service', 'Υπηρεσία Διαχείρισης Εγγράφων'), ('content_management_service', 'Υπηρεσία Διαχείρισης Περιεχομένου'), ('access_management_service', 'Υπηρεσία Διαχείρισης Πρόσβασης'), ('logging_service', 'Υπηρεσία Σύνδεσης'), ('audit_service', 'Υπηρεσία Ελέγχου'), ('metadata_management_service', 'Υπηρεσία Διαχείρισης Μεταδεδομένων'), ('networking_service', 'Υπηρεσία Δικτύωσης'), ('hosting_service', 'Υπηρεσία Φιλοξενίας'), ('storage_service', 'Υπηρεσία Αποθήκευσης'), ('base_registry_information_source', 'Υπηρεσία Πληροφοριών Μητρώου'), ('specific_services', 'Εξειδικευμένες Υπηρεσίες')], max_length=250, null=True),
        ),
        migrations.DeleteModel(
            name='SpecificServicesList',
        ),
    ]