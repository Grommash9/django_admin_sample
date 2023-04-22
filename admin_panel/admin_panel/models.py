from django.db import models


class City(models.Model):
    record_id = models.AutoField(unique=True, null=False, primary_key=True)
    title = models.CharField(max_length=50, unique=True)
    enabled = models.BooleanField(default=False)

    class Meta:
        db_table = "wallet_title"
        verbose_name_plural = 'Назви гаманців'

    def __str__(self):
        return f"{self.title}"

