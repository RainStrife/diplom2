import datetime
import simplejson
import pyowm
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from core.models import Note, Formation, PhotoAlbum, Video, Event
from project.settings import STATIC_URL


class Index(TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        qs_notes = Note.objects.all()[:5]
        qs_events = Event.objects.all()[:5]

        context['notes'] = qs_notes
        context['events'] = qs_events

        return context
index = Index.as_view()


class ContactInformation(TemplateView):
    template_name = 'core/contact_information.html'
    background = {
        'Thunderstorm': 'core/img_for_weather/1.JPG',
        'Drizzle': 'core/img_for_weather/2.JPG',
        'Rain': 'core/img_for_weather/3.JPG',
        'Snow': 'core/img_for_weather/4.jpg',
        'Atmosphere': 'core/img_for_weather/5.JPG',
        'Clear': 'core/img_for_weather/6.JPG',
        'Clouds': 'core/img_for_weather/7.JPG',
        'Extreme': 'core/img_for_weather/8.JPG',
        'Additional': 'core/img_for_weather/9.JPG',
    }
    #TODO сделать для всех вариантов картинки

    icon_url = 'http://openweathermap.org/img/w/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        owm = pyowm.OWM('5d436488dae946c7fa423d96b8bcd413')
        observation = owm.weather_at_place('Arneyevo, RU')
        observation = observation.get_weather()
        status = observation.get_status()

        context['background'] = self.background[status]
        context['temperature'] = observation.get_temperature('celsius')['temp']
        context['icon'] = self.icon_url + observation.get_weather_icon_name() + '.png'

        return context
contact_information = ContactInformation.as_view()


class CalendarEvents(TemplateView):
    template_name = 'core/calendar_events.html'

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            print(request)
            day = int(request.GET.get('day'))
            month = int(request.GET.get('month'))
            year = int(request.GET.get('year'))

            day = datetime.date(day=day, month=month, year=year)
            week_events_for_day = self.get_week_events_for_day(day)
            week_in_str = self.get_week_days_for_day(day)
            week_events = {'week_in_str': week_in_str, 'week_events': week_events_for_day}
            return JsonResponse(week_events, safe=False)
        else:
            return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_day = datetime.date.today()
        context['for_day'] = current_day.strftime('%m/%d/%Y') # for js DATE
        return context

    @classmethod
    def get_week_events_for_day(cls, day: datetime.date):
        """ [  [1=day, 2=[event1, event2] ], [...] ]
        # event1 = [ 'time', 'title', 'text', 'id']
        return: data for js
        """
        week_events = []
        qs = Event.objects.all()
        week_monday = cls.get_monday_for_week_included_day(day)
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
                elif hasattr(event, 'text'):
                    event_text = event.text[0:45]
                event_data = [event_time, event.title, event_text]
                list_events.append(event_data)

            day_list = [week_day.strftime('%d'), list_events]  # %d.%m.%y
            week_events.append(day_list)
        return week_events

    @classmethod
    def get_week_days_for_day(cls, day):
        ''' 21 06 2016 — 28 06 2016'''
        week_monday = cls.get_monday_for_week_included_day(day)
        week_data = (week_monday.strftime('%d %m %y')) + ' - ' + (week_monday + datetime.timedelta(days=6)).strftime('%d %m %y')
        return week_data

    @staticmethod
    def get_monday_for_week_included_day(day):
        current_weekday = day.weekday()
        monday = day - datetime.timedelta(days=current_weekday)
        return monday
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
