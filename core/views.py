from django.shortcuts import render
from django.views.generic import ListView, DetailView
from core.models import Note, Formation, PhotoAlbum, Video


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

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     list_formation_time = self.object.formation_times.all()
    #     times_in_day = {}
    #     for form_time in list_formation_time:
    #         if times_in_day.get(form_time.day):
    #             pass
    #         else:
    #             times_in_day[form_time.day] = [form_time.time]
    #     context['times_in_day'] = times_in_day
formation_detail = FormationDetail.as_view()


class VideoList(ListView):
    model = Video
    template_name = 'core/video_list.html'
video_list = VideoList.as_view()


class PhotoAlbumList(ListView):
    model = PhotoAlbum
    template_name = 'core/photo_album_list.html'
photo_album_list = PhotoAlbumList.as_view()


class PhotoAlbumDetail(DetailView):
    model = PhotoAlbum
    template_name = 'core/photo_album_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        photo_list = self.object.photos.all()
        context['photo_list'] = photo_list
        return context
photo_album_detail = PhotoAlbumDetail.as_view()
