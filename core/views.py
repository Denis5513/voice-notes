from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from .models import Record
from django.urls import reverse

from notes.models import Note

def record(request, note_id):
    if request.method == "POST":
        audio_file = request.FILES.get("recorded_audio")
        record = Record.objects.create(
            voice_record=audio_file,
        )
        record.save()
        note = Note.objects.get(id=note_id)
        note.record = record
        note.save()
        return JsonResponse(
            {
                "success": True,
                "url": reverse('home')
            }
        )
    context = {"page_title": "Record audio"}
    return render(request, "core/record.html", context)

def record_detail(request, id):
    record = get_object_or_404(Record, id=id)
    context = {
        "page_title": "Recorded audio detail",
        "record": record,
    }
    return render(request, "core/record_detail.html", context)

def index(request):
    records = Record.objects.all()
    context = {"page_title": "Voice records", "records": records}
    return render(request, "core/index.html", context)
