from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .forms import NoteForm, UserTagForm
from .models import Note, Tag, UserTag

def create_note(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = NoteForm(request.POST, user=request.user)
            if form.is_valid():
                note = form.save(commit=False)
                note.user = request.user  # Assuming the user creating the note is the logged-in user
                note.save()
                form.save_m2m()  # To save many-to-many relationships
                return redirect('core:record', note_id=note.id)
        else:
            form = NoteForm(user=request.user)
        return render(request, 'notes/note_form.html', {'form': form})
    else:
        return redirect('authorization_message')

def notes_list(request):
    if request.user.is_authenticated:
        notes = request.user.notes.filter(is_active=True)
        
        # Сортировка по дедлайну
        sort_by_deadline = request.GET.get('sort_by_deadline', None)
        if sort_by_deadline:
            notes = notes.order_by('deadline')
        
        # Фильтрация по тегам и пользовательским тегам
        selected_tags = request.GET.getlist('tags')
        selected_user_tags = request.GET.getlist('user_tags')
        if selected_tags:
            notes = notes.filter(tags__in=selected_tags).distinct()
        if selected_user_tags:
            notes = notes.filter(user_tags__in=selected_user_tags).distinct()
        
        # Получение всех тегов и пользовательских тегов для отображения в фильтре
        tags = Tag.objects.all()
        user_tags = request.user.tags.all()

        return render(request, 'notes/notes_list.html', {
            'notes': notes,
            'tags': tags,
            'user_tags': user_tags,
            'selected_tags': selected_tags,
            'selected_user_tags': selected_user_tags
        })
    else:
        return redirect('authorization_message')

def note_detail(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    
    if request.method == "POST":
        if "delete_note" in request.POST:
            note.is_active = False
            note.save()
            return redirect(reverse('notes_list'))

        form = NoteForm(request.POST, instance=note, user=request.user)
        if form.is_valid():
            form.save()
            if "record_audio" in request.POST:
                return redirect('core:record', note_id=note.id)
            return redirect(reverse('notes_list'))  # Assuming 'note_list' is the name of your notes listing URL
    else:
        form = NoteForm(instance=note, user=request.user)
    
    return render(request, 'notes/note_detail.html', {'form': form, 'note': note})

def add_user_tag(request):
    if request.method == 'POST':
        form = UserTagForm(request.POST)
        if form.is_valid():
            user_tag = form.save(commit=False)
            user_tag.user = request.user
            user_tag.save()
            return redirect(request.GET.get('next', 'note_list'))  # Redirect back to the previous page
    else:
        form = UserTagForm()

    return render(request, 'notes/add_user_tag.html', {'form': form})