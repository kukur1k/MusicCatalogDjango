from django.db import models
from django.urls import reverse

class Musician(models.Model):
    name = models.CharField(
        max_length=100, 
        verbose_name="Имя исполнителя"
    )
    country = models.CharField(
        max_length=50, 
        verbose_name="Страна исполнителя", 
        blank=True 
    )
    start_year = models.IntegerField(
        verbose_name="Начало карьеры",
        null=True,  
        blank=True 
    )

    cover_image = models.ImageField(
        upload_to='musician_covers/',  # Папка для загрузки файлов
        verbose_name="Фото исполнителя", 
        blank=True, 
        null=True  # Может быть NULL в базе данных
    )

    dedcription = models.TextField(
        verbose_name="Об исполнителе", 
        blank=True  # Может быть пустым
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Исполнитель"  # Название в единственном числе
        verbose_name_plural = "Исполнители"  # Название во множественном числе



class MusicTrack(models.Model):
    title = models.CharField(
        max_length=100, 
        verbose_name="Название трека" 
    )
    file = models.FileField(
        upload_to='mus_files/',  # Папка для загрузки файлов
        verbose_name="файл трека", 
        blank=True, 
        null=True  # Может быть NULL в базе данных
    )

    release_date = models.DateField(
        verbose_name="дата выхода",
        null=True,  
        blank=True 
    )

    cover_image = models.ImageField(
        upload_to='track_covers/',  # Папка для загрузки файлов
        verbose_name="Обложка трека", 
        blank=True, 
        null=True  # Может быть NULL в базе данных
    )

    is_folove = models.BooleanField(
        default=False,  # По умолчанию книга доступна
        verbose_name="В избранном"
    )

    musician = models.ForeignKey(
        Musician,
        on_delete=models.CASCADE,
        related_name='tracks', 
        verbose_name="Исполнитель"
    )

    album = models.ForeignKey(
        Album, 
        on_delete=models.CASCADE,
        related_name='tracks', 
        verbose_name="Альбом"
    )

    class Meta:
        verbose_name = "Трек"  # Название в единственном числе
        verbose_name_plural = "Треки"  # Название во множественном числе

    def get_absolute_url(self):
        """
        Возвращает URL для просмотра деталей трека.
        Используется в шаблонах для создания ссылок.
        """
        return reverse('track_detail', args=[str(self.id)])


    def __str__(self):
        return f"{self.title} - {self.musician.name}"


class Album(models.Model):
    title = models.CharField(
        max_length=100, 
        verbose_name="Название альбома" 
    )
    release_date = models.DateField(
        verbose_name="дата выхода",
        null=True,  
        blank=True 
    )
    cover_image = models.ImageField(
        upload_to='album_covers/',  # Папка для загрузки файлов
        verbose_name="Обложка альбома", 
        blank=True, 
        null=True  # Может быть NULL в базе данных
    )

    musician = models.ForeignKey(
        Musician, 
        on_delete=models.CASCADE,
        related_name='Albums', 
        verbose_name="Исполнитель"
    )

    class Meta:
        verbose_name = "Альбом"  # Название в единственном числе
        verbose_name_plural = "Альбомы"  # Название во множественном числе


    def __str__(self):
        return f"{self.title} - {self.musician.name}"








