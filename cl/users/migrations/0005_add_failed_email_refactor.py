# Generated by Django 3.2.13 on 2022-05-24 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_add_email_handling'),
    ]

    operations = [
        migrations.CreateModel(
            name='FailedEmail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, db_index=True, help_text='The moment when the item was created.')),
                ('date_modified', models.DateTimeField(auto_now=True, db_index=True, help_text='The last moment when the item was modified. A value in year 1750 indicates the value is unknown')),
                ('recipient', models.EmailField(help_text='The email address to which the delivery failed.', max_length=254)),
                ('status', models.SmallIntegerField(choices=[(0, 'Waiting for a delivery signal to enqueue.'), (1, 'Awaiting processing in queue after a backoff event.'), (2, 'Awaiting processing in queue due to a delivery event.'), (3, 'Item is currently being processed.'), (4, 'Item processed successfully.')], default=0, help_text='The enqueue failed message status.')),
                ('next_retry_date', models.DateTimeField(blank=True, help_text='The scheduled datetime to retry sending the message.', null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='BackoffEvent',
        ),
        migrations.RemoveConstraint(
            model_name='emailflag',
            name='unique_email_ban',
        ),
        migrations.RemoveField(
            model_name='emailflag',
            name='event_sub_type',
        ),
        migrations.RemoveField(
            model_name='emailflag',
            name='flag',
        ),
        migrations.RemoveField(
            model_name='emailflag',
            name='object_type',
        ),
        migrations.AddField(
            model_name='emailflag',
            name='flag_type',
            field=models.SmallIntegerField(choices=[(0, 'Email banned'), (1, 'Email backoff event')], default=0, help_text='The flag type assigned, Email ban: ban an email address and avoid sending any email. Email backoff event: an active backoff event.'),
        ),
        migrations.AddField(
            model_name='emailflag',
            name='next_retry_date',
            field=models.DateTimeField(blank=True, help_text='The next retry datetime for exponential backoff events.', null=True),
        ),
        migrations.AddField(
            model_name='emailflag',
            name='notification_subtype',
            field=models.SmallIntegerField(choices=[(0, 'Undetermined'), (1, 'General'), (2, 'NoEmail'), (3, 'Suppressed'), (4, 'OnAccountSuppressionList'), (5, 'MailboxFull'), (6, 'MessageTooLarge'), (7, 'ContentRejected'), (8, 'AttachmentRejected'), (9, 'Complaint'), (10, 'Other'), (11, 'MaxRetryReached')], default=0, help_text='The SES notification subtype that triggered the object.'),
        ),
        migrations.AddField(
            model_name='emailflag',
            name='retry_counter',
            field=models.SmallIntegerField(blank=True, help_text='The retry counter for exponential backoff events.', null=True),
        ),
        migrations.AlterField(
            model_name='emailflag',
            name='email_address',
            field=models.EmailField(help_text='The email address the EmailFlag object is related to.', max_length=254),
        ),
        migrations.AddConstraint(
            model_name='emailflag',
            constraint=models.UniqueConstraint(condition=models.Q(('flag_type', 0)), fields=('email_address',), name='unique_email_ban'),
        ),
        migrations.AddConstraint(
            model_name='emailflag',
            constraint=models.UniqueConstraint(condition=models.Q(('flag_type', 1)), fields=('email_address',), name='unique_email_backoff'),
        ),
        migrations.AddField(
            model_name='failedemail',
            name='stored_email',
            field=models.ForeignKey(help_text='The related stored email message.', on_delete=django.db.models.deletion.CASCADE, related_name='failed_emails', to='users.emailsent'),
        ),
        migrations.AddIndex(
            model_name='failedemail',
            index=models.Index(fields=['recipient'], name='users_faile_recipie_c03e8d_idx'),
        ),
        migrations.AddConstraint(
            model_name='failedemail',
            constraint=models.UniqueConstraint(condition=models.Q(('status', 1)), fields=('recipient',), name='unique_failed_enqueued'),
        ),
    ]
