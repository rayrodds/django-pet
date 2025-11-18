from django.db import models

# Create your models here.

from django.contrib.auth.models import User


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	full_name = models.CharField(max_length=200, blank=True)
	# avatar image
	image = models.ImageField(upload_to='avatars/', null=True, blank=True)
	cpf_cnpj = models.CharField(max_length=50, blank=True)
	phone = models.CharField(max_length=30, blank=True)
	birth_date = models.DateField(null=True, blank=True)
	gender = models.CharField(max_length=20, blank=True)

	cep = models.CharField(max_length=20, blank=True)
	city = models.CharField(max_length=100, blank=True)
	neighborhood = models.CharField(max_length=100, blank=True)
	street = models.CharField(max_length=200, blank=True)
	number = models.CharField(max_length=20, blank=True)

	def __str__(self):
		return f"Profile: {self.user.username}"
