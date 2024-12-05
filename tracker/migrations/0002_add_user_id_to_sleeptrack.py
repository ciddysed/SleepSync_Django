
from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),  # Adjust this to your latest migration file
    ]

    operations = [
        migrations.AddField(
            model_name='sleeptrack',
            name='user_id',
            field=models.IntegerField(null=True),
        ),
    ]