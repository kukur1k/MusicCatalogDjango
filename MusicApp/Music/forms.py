from django import forms
from .models import Musician, MusicTrack, Album

# Форма для создания и редактирования авторов
class MusicianForm(forms.ModelForm):
    """
    Форма для работы с моделью Musician.
    Позволяет создавать и редактировать записи об авторах.
    """
    class Meta:
        model = Musician
        # Поля, которые будут отображаться в форме
        fields = ['cover_image', 'name', 'start_year', 'country', 'description']
        # Настройка внешнего вида полей (виджеты)
        widgets = {
            'cover_image': forms.FileInput(attrs={
                'class': '',
                'placeholder': 'Имя исполнителя'
            }),
            'name': forms.TextInput(attrs={
                'class': '',  # CSS класс Bootstrap
                'placeholder': 'Имя исполнителя'  # Подсказка в поле ввода
            }),
            'start_year': forms.NumberInput(attrs={
                'class': '',
                'placeholder': 'Год рождения'
            }),
            'country': forms.TextInput(attrs={
                'class': '',
                'placeholder': 'Страна'
            }),
            'description': forms.Textarea(attrs={
                'class': '',
                'placeholder': 'Об исполнителе'
            }),
        }
