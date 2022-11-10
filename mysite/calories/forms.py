from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Model

from .models import *

class CreateUserForm(UserCreationForm):
	username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control'}))
	password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
	password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
	class Meta:
		model = User
		fields = ('username','password1','password2')

class DataUser(forms.ModelForm):
	CHOICES_gender = [(0, 'Мужчина'), (1, 'Женщина')]
	CHOICES_activity = [(1.2, 'Минимальная активность'), (1.375, 'Слабый уровень активности'),
						(1.55, 'Умеренный уровень активности'), (1.7, 'Тяжелая или трудоемкая активность'),
						(1.9, 'Экстремальный уровень активности')]

	age = forms.IntegerField(label='Возраст, лет', widget=forms.NumberInput(attrs={'class': 'col-md-1'}))
	height = forms.IntegerField(label='Рост, см', widget=forms.NumberInput(attrs={'class': 'col-md-1'}))
	weight = forms.IntegerField(label='Вес, кг', widget=forms.NumberInput(attrs={'class': 'col-md-1'}))
	gender = forms.IntegerField(label='Пол', widget=forms.RadioSelect(choices=CHOICES_gender))
	activity = forms.FloatField(label='Физическая активность', widget=forms.Select(choices=CHOICES_activity))
	class Meta:
		model = UserProfile
		fields = ('age', 'height', 'weight', 'gender', 'activity')

class AddFood(forms.ModelForm):
	amount = forms.IntegerField(label='Количество, граммы', widget=forms.NumberInput(attrs={'class': 'col-md-1'}))
	class Meta:
		model = Visitor
		fields = ('nameProduct', 'amount')

