from django.db import models
from django.contrib.auth.models import User
from datetime import *

class Customers(models.Model):
	address = models.TextField()
	contact = models.BigIntegerField()
	gender = models.CharField(max_length=10)
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	image = models.CharField(max_length=255, default='')

	class Meta:
		db_table = 'customers'

class Contact(models.Model):
	firstname = models.CharField(max_length=50)
	lastname = models.CharField(max_length=50)
	phone = models.BigIntegerField()
	email = models.CharField(max_length=100)
	subject = models.CharField(max_length=200)
	message = models.TextField()

	class Meta:
		db_table = 'contact'

class Feedback(models.Model):
	rating = models.CharField(max_length=50)
	comment = models.TextField()
	date = models.DateField(auto_now=True)
	customers = models.OneToOneField(Customers,on_delete=models.CASCADE)

	class Meta:
		db_table = 'feedback'

class City(models.Model):
	citys = models.CharField(max_length=150)

	class Meta:
		db_table = 'city'

class Area(models.Model):
	area = models.CharField(max_length=150)
	city = models.ForeignKey(City,on_delete=models.CASCADE)

	class Meta:
		db_table = 'area'

class Post_property(models.Model):
	property_for = models.CharField(max_length=50)
	property_type = models.CharField(max_length=30)
	sub_property_type = models.CharField(max_length=150)
	property_name = models.CharField(max_length=150)
	price = models.DecimalField(max_digits=9, decimal_places=2)
	rooms = models.CharField(max_length=50)
	property_age = models.CharField(max_length=30)
	types = models.CharField(max_length=30)
	facility = models.CharField(max_length=150)
	maintenance = models.CharField(max_length=50)
	sq_area = models.CharField(max_length=150,default='')
	property_description = models.TextField()
	address = models.TextField()
	contact = models.BigIntegerField()
	property_image = models.CharField(max_length=255)
	city = models.ForeignKey(City,on_delete=models.CASCADE,default='')
	area = models.ForeignKey(Area,on_delete=models.CASCADE,default='')
	customers = models.ForeignKey(Customers,on_delete=models.CASCADE)

	class Meta:
		db_table = 'post_property'

class Add_more_images(models.Model):
	image = models.CharField(max_length=255)
	post_property = models.ForeignKey(Post_property,on_delete=models.CASCADE)

	class Meta:
		db_table = 'add_more_images'

class Buy_property(models.Model):
	post_property = models.ForeignKey(Post_property,on_delete=models.CASCADE)
	message = models.TextField()
	from_user = models.ForeignKey(Customers,on_delete=models.CASCADE,related_name='from_user')
	cur_date = models.DateField(default=date.today)
	status = models.CharField(max_length=50,default='pending')
	to_user = models.ForeignKey(Customers,on_delete=models.CASCADE,related_name='to_user')

	class Meta:
		db_table = 'buy_property'