import datetime
import simplejson
import pyowm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from core.models import Note, Formation, PhotoAlbum, Video, Event


def index(request):
    return render(request, 'core/index.html', {})


def contact_information(request):
    owm = pyowm.OWM('5d436488dae946c7fa423d96b8bcd413')
    observation = owm.weather_at_place('Arneyevo, RU')
    observation = observation.get_weather()
    return render(request, 'core/contact_information.html', {})


class CalendarEvents(TemplateView):
    template_name = 'core/calendar_events.html'

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            print(request)
            for_day = request.GET.get('for_day')
            print(for_day)
            return HttpResponse()
        else:
            return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_day = datetime.date.today()
        context['for_day'] = current_day
        # events_for_current_day = self.get_week_events_for_day(current_day)
        # context['week_events'] = events_for_current_day
        return context

    @staticmethod
    def get_week_events_for_day(day: datetime.date):
        """ [  [1=day, 2=[event1, event2] ], [...] ]
        # event1 = [ 'time', 'title', 'text', 'id']
        return: data for js
        """
        week_events = []
        qs = Event.objects.all()
        current_day = day
        current_weekday = current_day.weekday()
        week_monday = current_day - datetime.timedelta(days=current_weekday)
        for week_index_day in range(0, 7):
            week_day = week_monday + datetime.timedelta(days=week_index_day)
            day_events = qs.filter(event_date__year=week_day.year,
                                   event_date__month=week_day.month,
                                   event_date__day=week_day.day)
            list_events = []
            for event in day_events:
                event_time = event.event_date.strftime('%H:%M')
                event_text = ''
                if hasattr(event, 'short_text'):
                    event_text = event.short_text
                if hasattr(event, 'text'):
                    event_text = event.text[0:45]
                event_data = [event_time, event.title, event_text]
                list_events.append(event_data)

            day_list = [week_day.strftime('%d'), list_events]  # %d.%m.%y
            week_events.append(day_list)
        return week_events
calendar_events = CalendarEvents.as_view()


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
