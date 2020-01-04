from main.views import main
from django.db import models

# Create your models here.


'''
Описываем модель категории (имя/краткое_описание/дата изменений/дата создания)
Описываем модель продукта (имя/ссылка на атрибут категория/ссылка на атрибут картинки/краткое_описание/стоимость товара/дата изменений/дата создания)
'''

class Category(models.Model):
	title = models.CharField(max_length = 250,)
	snippet = models.TextField(blank = True, null = True)
	modified = models.DateTimeField(auto_now = True)
	created = models.DateTimeField(auto_now_add = True)
	
	def __str__(self):
		return self.title

class Product(models.Model):
	title = models.CharField(max_length = 250,)
	category = models.ForeignKey(
		Category,
		on_delete = models.CASCADE,
		blank = True,
		null = True,
		)
	image = models.ForeignKey(
		'images.Image',
		on_delete = models.PROTECT,
		null = True,
		blank = True,
		)
	snippet = models.TextField(blank = True, null = True)
	cost = models.DecimalField(
		max_digits = 12,
		decimal_places = 2,
		default = 0,
		)
	modified = models.DateTimeField(auto_now = True)
	created = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return self.title
