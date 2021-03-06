# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-18 08:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('questionnaire', '0023_auto_20170618_1117'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceConsumption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_consumption', multiselectfield.db.fields.MultiSelectField(choices=[('authentication_service', 'Υπηρεσία Αυθεντικοποίησης'), ('e_signature_service', 'Υπηρεσία Ηλεκτρονικών Υπογραφών'), ('e_payment_service', 'Υπηρεσία Ηλεκτρονικών Πληρωμών'), ('messaging_service', 'Yπηρεσία Μηνυμάτων'), ('audio_visual_service', 'Υπηρεσία Οπτικοακουστικών Μέσων'), ('data_transformation_service', 'Υπηρεσία Μετασχηματισμού Δεδομένων'), ('data_validation_service', 'Υπηρεσία Επικύρωσης Δεδομένων'), ('machine_translation_service', 'Υπηρεσία Αυτόματης Μετάφρασης'), ('data_exchange_service', 'Υπηρεσία Ανταλλαγής Δεδομένων'), ('business_analytics_service', 'Υπηρεσία Επιχειρηματικής Ανάλυσης'), ('business_reporting_service', 'Υπηρεσία Αναφοράς Επιχειρήσεων'), ('forms_management_service', 'Υπηρεσία Διαχείρισης Φορμών'), ('records_management_service', 'Υπηρεσία Διαχείρισης Αρχείων'), ('document_management_service', 'Υπηρεσία Διαχείρισης Εγγράφων'), ('content_management_service', 'Υπηρεσία Διαχείρισης Περιεχομένου'), ('access_management_service', 'Υπηρεσία Διαχείρισης Πρόσβασης'), ('logging_service', 'Υπηρεσία Σύνδεσης'), ('audit_service', 'Υπηρεσία Ελέγχου'), ('metadata_management_service', 'Υπηρεσία Διαχείρισης Μεταδεδομένων'), ('networking_service', 'Υπηρεσία Δικτύωσης'), ('hosting_service', 'Υπηρεσία Φιλοξενίας'), ('storage_service', 'Υπηρεσία Αποθήκευσης'), ('base_registry_information_source', 'Υπηρεσία Πληροφοριών Μητρώου'), ('specific_services', 'Εξειδικευμένες Υπηρεσίες')], max_length=250, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='LandscapingServiceConsumption',
        ),
    ]
