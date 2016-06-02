from django.shortcuts import render
from django.views.generic import ListView, DetailView
from core.models import Note


def index(request):
    return render(request, 'core/index.html', {})


class NoteList(ListView):
    model = Note
    template_name = 'core/note_list.html'
note_list = NoteList.as_view()


class NoteDetail(DetailView):
    model = Note
    template_name = 'core/note_detail.html'
    slug_field = 'id'
note_detail = NoteDetail.as_view()
