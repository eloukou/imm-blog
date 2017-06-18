# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-18 09:31
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('questionnaire', '0024_auto_20170618_1139'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReuseAndSharing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reuse_and_sharing', multiselectfield.db.fields.MultiSelectField(choices=[('1', 'Ανταλλαγή τεκμηρίωσης για την παροχή σε άλλους (σχετιζόμενους) οργανισμούς πολύτιμων πληροφοριών σχετικά με τις διαδικασίες, την οργάνωση, τη διακυβέρνηση, τις επιλογές τεχνολογίας κλπ.'), ('2', 'Κοινή χρήση πηγαίου κώδικα ή λογισμικού με δυνατότητα λήψης για να δοθεί η δυνατότητα σε άλλες οργανώσεις να δημιουργήσουν αποτελεσματικά τις υπηρεσίες τους.'), ('3', 'Δημιουργία διαθέσιμων υπηρεσιών Web-API για να δοθεί η δυνατότητα σε άλλους οργανισμούς και ιδιώτες  να (επανα-)χρησιμοποιήσουν τη λειτουργικότητα ή / και να αποκτήσουν πρόσβαση σε δεδομένα μέσω διαδικτύου και / ή εφαρμογών για κινητά.'), ('4', 'Παροχή υποστήριξης σε οργανισμούς που αξιοποιούν τους πόρους που παρέχονται.'), ('5', 'Κανένα από τα παραπάνω.')], max_length=250, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='serviceconsumption',
            name='service_consumption',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('authentication_service', 'Υπηρεσία Αυθεντικοποίησης'), ('e_signature_service', 'Υπηρεσία Ηλεκτρονικών Υπογραφών'), ('e_payment_service', 'Υπηρεσία Ηλεκτρονικών Πληρωμών'), ('messaging_service', 'Yπηρεσία Μηνυμάτων'), ('audio_visual_service', 'Υπηρεσία Οπτικοακουστικών Μέσων'), ('data_transformation_service', 'Υπηρεσία Μετασχηματισμού Δεδομένων'), ('data_validation_service', 'Υπηρεσία Επικύρωσης Δεδομένων'), ('machine_translation_service', 'Υπηρεσία Αυτόματης Μετάφρασης'), ('data_exchange_service', 'Υπηρεσία Ανταλλαγής Δεδομένων'), ('business_analytics_service', 'Υπηρεσία Επιχειρηματικής Ανάλυσης'), ('business_reporting_service', 'Υπηρεσία Αναφοράς Επιχειρήσεων'), ('forms_management_service', 'Υπηρεσία Διαχείρισης Φορμών'), ('records_management_service', 'Υπηρεσία Διαχείρισης Αρχείων'), ('document_management_service', 'Υπηρεσία Διαχείρισης Εγγράφων'), ('content_management_service', 'Υπηρεσία Διαχείρισης Περιεχομένου'), ('access_management_service', 'Υπηρεσία Διαχείρισης Πρόσβασης'), ('logging_service', 'Υπηρεσία Σύνδεσης'), ('audit_service', 'Υπηρεσία Ελέγχου'), ('metadata_management_service', 'Υπηρεσία Διαχείρισης Μεταδεδομένων'), ('networking_service', 'Υπηρεσία Δικτύωσης'), ('hosting_service', 'Υπηρεσία Φιλοξενίας'), ('storage_service', 'Υπηρεσία Αποθήκευσης'), ('base_registry_information_source', 'Υπηρεσία Πληροφοριών Μητρώου'), ('specific_services', 'Άλλες Εξειδικευμένες Υπηρεσίες')], max_length=250, null=True),
        ),
    ]
