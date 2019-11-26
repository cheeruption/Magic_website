from django.db import models


class Image(models.Model):
	title = models.CharField(max_length = 150)
	value = models.ImageField(upload_to = 'images')


# у каждого экземпляра модели есть метод для вызова url адреса картинки
@property
def url(self):
	return self.value.url


# каждый экземпляр модели вызывается по его атрибуту title
@property
def __str__(self):
	return self.title

