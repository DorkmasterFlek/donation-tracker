# Generated by Django 2.0.4 on 2018-04-25 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0005_prize_auto_tickets'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bidsuggestion',
            options={'ordering': ['bid__event__date', 'bid__speedrun__starttime', 'bid__parent__name', 'bid__name', 'name']},
        ),
        migrations.AlterModelOptions(
            name='donationbid',
            options={'ordering': ['-donation__timereceived', 'bid__name'], 'verbose_name': 'Donation Bid'},
        ),
        migrations.AlterModelOptions(
            name='donor',
            options={'ordering': ['lastname', 'firstname', 'email', 'alias'], 'permissions': (('delete_all_donors', 'Can delete donors with cleared donations'), ('view_usernames', 'Can view full usernames'), ('view_emails', 'Can view email addresses'))},
        ),
        migrations.AlterModelOptions(
            name='donorprizeentry',
            options={'ordering': ('prize__event__date', 'prize__startrun__starttime', 'prize__starttime', 'prize__name', 'donor__lastname', 'donor__firstname', 'donor__email', 'donor__alias'), 'verbose_name': 'Donor Prize Entry', 'verbose_name_plural': 'Donor Prize Entries'},
        ),
        migrations.AlterModelOptions(
            name='event',
            options={'get_latest_by': 'date', 'ordering': ('date', 'name'), 'permissions': (('can_edit_locked_events', 'Can edit locked events'),)},
        ),
        migrations.AlterModelOptions(
            name='prizecategory',
            options={'ordering': ('name',), 'verbose_name': 'Prize Category', 'verbose_name_plural': 'Prize Categories'},
        ),
        migrations.AlterModelOptions(
            name='prizewinner',
            options={'ordering': ('prize__event__date', 'prize__startrun__starttime', 'prize__starttime', 'prize__name', 'winner__lastname', 'winner__firstname', 'winner__email', 'winner__alias'), 'verbose_name': 'Prize Winner'},
        ),
        migrations.AlterModelOptions(
            name='speedrun',
            options={'ordering': ['event__date', 'order', 'name'], 'permissions': (('can_view_tech_notes', 'Can view tech notes'),), 'verbose_name': 'Speed Run'},
        ),
        migrations.AlterModelOptions(
            name='submission',
            options={'ordering': ('run__event__date', 'run__order', 'run__name', 'game_name', 'category')},
        ),
    ]