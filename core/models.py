# core > models.py

import uuid

from django.db import models
from django.urls.base import reverse
from django.utils import timezone

class Record(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    voice_record = models.FileField(upload_to="records")

    class Meta:
        verbose_name = "Record"
        verbose_name_plural = "Records"

    def __str__(self):
        return str(self.voice_record.name)

    def get_absolute_url(self):
        return reverse("record_detail", kwargs={"id": str(self.id)})


