from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

class Tag(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class UserTag(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='tags',
        help_text="The user to whom this tag belongs."
    )

    def __str__(self):
        return self.name

class Note(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()
    audio_file = models.FilePathField(path='media', recursive=True)

    PRIORITY_CHOICES = [
        (0, '0 - Highest!!!'),
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5 - Lowest'),
    ]

    priority = models.IntegerField(
        choices=PRIORITY_CHOICES,
        default=4,
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        help_text="Priority scale from 0 (highest) to 5 (lowest). Default is 5 (diploma?)."
    )

    tags = models.ManyToManyField(
        to='Tag',
        related_name='notes',
        blank=True
    )
    user_tags = models.ManyToManyField(
        to='UserTag',
        related_name='notes',
        blank=True
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='notes',
        help_text='The users notes'
    )
    recipient = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='received_notes',
        help_text='Notes sent by other users',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name


