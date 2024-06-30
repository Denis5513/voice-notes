from django.shortcuts import render, redirect
from .forms import NoteForm

def create_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user  # Assuming the user creating the note is the logged-in user
            note.save()
            form.save_m2m()  # To save many-to-many relationships
            return redirect('core:record', note_id=note.id)
    else:
        form = NoteForm()
    return render(request, 'notes/note_form.html', {'form': form})