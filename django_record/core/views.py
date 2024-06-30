# core > views.py

from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from .models import Record
from django.urls import reverse

def record(request):
    if request.method == "POST":
        audio_file = request.FILES.get("recorded_audio")
        language = request.POST.get("language")
        deadline = request.POST.get("deadline")
        tags = request.POST.get("tags")
        importance = request.POST.get("importance")
        record = Record.objects.create(
            language=language,
            voice_record=audio_file,
            deadline=deadline,
            tags=tags,
            importance=importance
        )
        record.save()
        messages.success(request, "Audio recording successfully added!")
        return JsonResponse(
            {
                "success": True,
                "url": reverse('core:index')
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
