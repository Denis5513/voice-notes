# core > models.py

import uuid

from django.db import models
from django.urls.base import reverse
from django.utils import timezone

class Record(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    voice_record = models.FileField(upload_to="records")
    language = models.CharField(max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    tags = models.CharField(max_length=255, null=True, blank=True)  #comma-separated string
    importance = models.IntegerField(default=1, choices=[(i, i) for i in range(1, 6)], null=True, blank=True)  # Importance on a scale of 1-5

    class Meta:
        verbose_name = "Record"
        verbose_name_plural = "Records"

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse("record_detail", kwargs={"id": str(self.id)})


