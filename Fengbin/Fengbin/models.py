from django.db import models

class Website(models.Model):
    id = models.AutoField(primary_key=True)
    url = models.CharField(max_length=255, default="")
    comment = models.CharField(max_length=255, default="")
    is_foreign = models.IntegerField(default=0)

    class Meta:
        db_table = 'website'