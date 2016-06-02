from django.shortcuts import render
from django.views.generic import ListView
from core.models import Note


def index(request):
    return render(request, 'core/index.html', {})


class NoteList(ListView):
    model = Note
    template_name = 'core/notes.html'
note_list = NoteList.as_view()
