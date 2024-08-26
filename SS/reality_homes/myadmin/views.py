from django.shortcuts import render,redirect
from myadmin.models import *
from django.contrib.auth.models import auth,User
from django.contrib import messages

# Create your views here.

def dashboard(request):
	context = {}
	return render(request, 'myadmin/dashboard.html', context)

def login(request):
	context = {}
	return render(request, 'myadmin/login.html', context)

def login_check(request):
	username = request.POST['username']
	password = request.POST['password']	

	result = auth.authenticate(request, username=username , password=password)

	if result is None:
		print('Invalid username or password')
		return redirect('/myadmin/')

	else:
		if result.is_superuser:
			auth.login(request, result)
			return redirect('/myadmin/dashboard')

		else:
			print('Invalid username or password')
			return redirect('/myadmin/')

def logout(request):
    auth.logout(request)
    return  redirect('/myadmin/')

def view_customers(request):
	result_cus = Customers.objects.all()
	context = {'result_cus':result_cus}
	return render(request, 'myadmin/view_customers.html', context)

def customer(request,id):
	result = Customers.objects.get(pk=id)
	context = {'result':result}
	return render(request, 'myadmin/customer.html',context)

def view_feedback(request):
	result_feedback = Feedback.objects.all()
	context = {'result_feedback':result_feedback}
	return render(request, 'myadmin/view_feedback.html', context)

def view_inquiry(request):
	result_inquiry = Contact.objects.all()
	context = {'result_inquiry':result_inquiry}
	return render(request, 'myadmin/view_inquiry.html', context)

def add_city(request):
	context = {}
	return render(request, 'myadmin/add_city.html', context)

def city_store(request):
	city = request.POST['city']

	City.objects.create(citys=city)
	return redirect('/myadmin/add_city')

def add_area(request):
	result = City.objects.all()
	context = {'result': result}
	return render(request, 'myadmin/add_area.html', context)

def area_store(request):
	area = request.POST['area']
	mycity = request.POST['city']

	Area.objects.create(area=area,city_id=mycity)
	return redirect('/myadmin/add_area')

def all_cities(request):
	result1 = City.objects.all()
	context = {'result1':result1}
	return render(request, 'myadmin/all_cities.html', context)

def delete_city(request,id):
	result = City.objects.get(pk=id)
	result.delete()
	return redirect('/myadmin/all_cities')

def edit_city(request,id):
	result = City.objects.get(pk=id)
	context = {'result':result}
	return render(request,'myadmin/edit_city.html',context)

def update_city(request,id):
	data = {
			'citys': request.POST['city']
		   }

	City.objects.update_or_create(pk=id,defaults=data)
	return redirect('/myadmin/all_cities')

def all_areas(request):
	result = Area.objects.all()
	context = {'result':result}
	return render(request, 'myadmin/all_areas.html',context)

def delete_area(request,id):
	result = Area.objects.get(pk=id)
	result.delete()
	return redirect('/myadmin/all_areas')

def edit_area(request,id):
	result1 = City.objects.all()
	result = Area.objects.get(pk=id)
	context = {'result':result,'result1':result1}
	return render(request,'myadmin/edit_area.html',context)

def update_area(request,id):
	data = {
			'city_id': request.POST['city'],
			'area' : request.POST['area']
		   }

	Area.objects.update_or_create(pk=id,defaults=data)
	return redirect('/myadmin/all_areas')
