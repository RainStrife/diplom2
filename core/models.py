from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    short_text = models.CharField(max_length=300, blank=True, verbose_name='Краткое описание')
    text = models.TextField(blank=True, verbose_name='Полное описание')
    img = models.ImageField(blank=True, verbose_name='Изображение', upload_to='event/')
    event_date = models.DateTimeField(verbose_name='Дата события')
    tags = models.ManyToManyField("Tag", blank=True, related_name='events')  # Все теги прикреплённые к событию
    published_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')

    def __str__(self):
        return self.title


class Note(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    short_text = models.CharField(max_length=300, blank=True, verbose_name='Краткое описание')
    text = models.TextField(blank=True, verbose_name='Полное описание')
    published_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    photos = models.ManyToManyField("Photo", blank=True, related_name='notes')
    tags = models.ManyToManyField("Tag", blank=True, related_name='notes')  # Все теги прикреплённые к новости

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=100, verbose_name='Тэг')

    def __str__(self):
        return self.title


class PhotoAlbum(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название Альбома')
    img = models.ImageField(upload_to='albums/', verbose_name='Превью Альбома')

    def __str__(self):
        return self.title


class VideoAlbum(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название Альбома')
    img = models.ImageField(upload_to='albums/', verbose_name='Превью Альбома')

    def __str__(self):
        return self.title


class Photo(models.Model):
    title = models.CharField(max_length=100, blank=True, verbose_name='Название фотографии')
    img = models.ImageField(verbose_name='Изображение',  upload_to='photo/')
    album = models.ForeignKey(PhotoAlbum, blank=True, null=True, related_name='photos')
    tags = models.ManyToManyField(Tag, blank=True, related_name='photos')

    def __str__(self):
        return self.title


class Video(models.Model):
    title = models.CharField(max_length=50, blank=True, verbose_name='Название видео')
    url = models.URLField(verbose_name='Ссылка на видео')
    album = models.ForeignKey(VideoAlbum, blank=True, null=True, related_name='videos')
    tags = models.ManyToManyField(Tag, blank=True, related_name='videos')

    def __str__(self):
        return self.title


class Formation(models.Model):
    title = models.CharField(max_length=200, blank=True, verbose_name='Название клубного формирования')
    short_text = models.CharField(max_length=300, blank=True, verbose_name='Краткое описание')
    text = models.TextField(blank=True, verbose_name='Полное описание')
    photos = models.ManyToManyField(Photo, blank=True, related_name='formations')
    leader = models.CharField(max_length=300, verbose_name='Руководитель')

    def __str__(self):
        return self.title


class FormationTime(models.Model):
    day_of_the_week = (
        ('Mon', 'Понедельник'),
        ('Tue', 'Вторник'),
        ('Wed', 'Среда'),
        ('Thu', 'Четверг'),
        ('Fri', 'Пятница'),
        ('Sat', 'Суббота'),
        ('Sun', 'Воскресенье'),
    )
    day = models.CharField(max_length=3, choices=day_of_the_week)
    time = models.TimeField()
    formation = models.ForeignKey(Formation)

    def __str__(self):
        title = self.formation.title + " " + self.day + " " + str(self.time)
        return title
