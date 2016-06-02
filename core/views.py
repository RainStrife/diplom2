from django.shortcuts import render
from django.views.generic import ListView, DetailView
from core.models import Note, Formation, VideoAlbum, PhotoAlbum


def index(request):
    return render(request, 'core/index.html', {})


def contact_information(request):
    return render(request, 'core/contact_information.html', {})


class NoteList(ListView):
    model = Note
    template_name = 'core/note_list.html'
note_list = NoteList.as_view()


class NoteDetail(DetailView):
    model = Note
    template_name = 'core/note_detail.html'
note_detail = NoteDetail.as_view()


class FormationList(ListView):
    model = Formation
    template_name = 'core/formation_list.html'
formation_list = FormationList.as_view()


class FormationDetail(DetailView):
    model = Formation
    template_name = 'core/formation_detail.html'
formation_detail = FormationDetail.as_view()


class VideoAlbumList(ListView):
    model = VideoAlbum
    template_name = 'core/video_album_list.html'
video_album_list = VideoAlbumList.as_view()


class PhotoAlbumList(ListView):
    model = PhotoAlbum
    template_name = 'core/photo_album_list.html'
photo_album_list = PhotoAlbumList.as_view()
