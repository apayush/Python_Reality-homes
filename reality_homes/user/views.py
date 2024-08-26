from django.shortcuts import render,redirect
from django.contrib.auth.models import auth,User
from myadmin.models import *
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os
from django.contrib import messages


# Create your views here.

def home(request):
    result = City.objects.all()
    result1 = Area.objects.all()
    result2 = Post_property.objects.all()

    selected_city_id = request.GET.get('city', None)
    if selected_city_id:
        result1 = result1.filter(city_id=selected_city_id)
    
    context = {'result':result,'result1':result1,'properties': result2,'selected_city_id': selected_city_id}
    return render(request, 'user/home.html', context)

# def home(request):
#     cities = City.objects.all()
#     areas = Area.objects.all()
#     result2 = Post_property.objects.all()

#     selected_city_id = request.GET.get('city', None)
#     if selected_city_id:
#         areas = Area.objects.filter(city_id=selected_city_id)
    
#     context = {'cities':cities,'areas':areas,'properties': result2,'selected_city_id': selected_city_id}
#     return render(request, 'user/home.html', context)

def about(request):
    context = {}
    return render(request, 'user/about.html', context)

def registration(request):
    context = {}
    return render(request, 'user/registration.html', context)

def rstore(request):
    # User model

    firstname = request.POST['fname']
    lastname = request.POST['lname']
    email = request.POST['email']
    username = request.POST['username']
    password = request.POST['password']
    cpassword = request.POST['cpassword']

    # Customer model

    contact = request.POST['contact']
    address = request.POST['address']   
    gender = request.POST['gender']
    myimg = request.FILES['image']

    mylocation =  os.path.join(settings.MEDIA_ROOT,'upload')
    obj =  FileSystemStorage(location=mylocation)
    obj.save(myimg.name,myimg)

    if password  == cpassword:
        result = User.objects.create_user(first_name=firstname,last_name=lastname,email=email,username=username,password=password)
        Customers.objects.create(contact=contact,address=address,gender=gender,user_id=result.id,image=myimg)
        return redirect('/user/login')

    else:
        print('missmatch password') 

def login(request):
    context = {}
    return render(request, 'user/login.html', context)

def login_check(request):
    uname = request.POST['username']
    passwd = request.POST['password']

    result = auth.authenticate(request, username=uname,password=passwd)

    if result is None:
        print('Invalid username or password')
        return redirect('/user/login')

    else:
        auth.login(request, result)
        return redirect('/user/home')

def logout(request):
    auth.logout(request)
    return  redirect('/user/login')

def contact(request):
    context = {}
    return render(request, 'user/contact.html', context)

def contact_store(request):
    fname =  request.POST['fname']
    lname = request.POST['lname']
    phone = request.POST['phone']
    email = request.POST['email']
    subject = request.POST['subject']
    message = request.POST['message']

    Contact.objects.create(firstname=fname,lastname=lname,phone=phone,email=email,subject=subject,message=message)
    return redirect('/user/contact')

def feedback(request):
    context = {}
    return render(request, 'user/feedback.html', context)

def feedback_store(request):
    rating = request.POST['rating']
    comment = request.POST['comment']

    id = request.user.id
    cus_id = Customers.objects.get(user_id=id)
    customer_id = cus_id.id

    Feedback.objects.create(rating=rating,comment=comment,customers_id=customer_id)
    return redirect('/user/feedback')

def view_profile(request):
    id = request.user.id
    view_customer = Customers.objects.filter(user_id=id)
    context = {'view_customer':view_customer}
    return render(request, 'user/view_profile.html', context)

def edit_profile(request,id):
    id = request.user.id
    result = Customers.objects.get(user_id=id) 
    context = {'result':result}
    return render(request,'user/edit_profile.html',context)

def update_profile(request,id):
    result = Customers.objects.get(pk=id)
    u_id = request.user.id

    if len(request.FILES) != 0:
        img = request.FILES['image']
        mylocation =  os.path.join(settings.MEDIA_ROOT,'upload')
        obj =  FileSystemStorage(location=mylocation)
        obj.save(img.name,img)
        filename = img.name
    else:
        filename = result.image


    data = {
                'first_name' :request.POST['fname'],
                'last_name'  :request.POST['lname'],
                'email'      :request.POST['email'],
            }
    data1 = {
                'gender'  :request.POST['gender'],
                'address' :request.POST['address'],
                'contact' :request.POST['contact'],
                'image'   :filename
            }
    User.objects.update_or_create(pk=u_id,defaults=data)
    Customers.objects.update_or_create(pk=id,defaults=data1)
    return redirect('/user/view_profile')

def add_property(request):
    result = City.objects.all()
    result1 = Area.objects.all()
    context = {'result':result,'result1':result1}
    return render(request, 'user/add_property.html', context)

def property_store(request):
    property_for = request.POST['property_for']
    property_type = request.POST['property_type']
    sub_property_type = request.POST['sub_property_type']
    property_name = request.POST['property_name']
    property_price = request.POST['property_price']
    rooms = request.POST['rooms']
    types = request.POST['types']
    
    facility_list = request.POST.getlist('facility[]')
    facility_str = ','.join(facility_list)

    property_age = request.POST['property_age']
    city = request.POST['city']
    area = request.POST['area']
    maintenance = request.POST['maintenance']
    sq_area = request.POST['sq_area']
    property_description = request.POST['description']
    contact = request.POST['contact']
    address = request.POST['address']

    image = request.FILES['image']

    mylocation =  os.path.join(settings.MEDIA_ROOT,'upload')
    obj =  FileSystemStorage(location=mylocation)
    obj.save(image.name,image)

    id = request.user.id
    cus_id = Customers.objects.get(user_id=id)
    customer_id = cus_id.id

    Post_property.objects.create(property_for=property_for,property_type=property_type,sub_property_type=sub_property_type,property_name=property_name,price=property_price,rooms=rooms,types=types,facility=facility_str,property_age=property_age,maintenance=maintenance,sq_area=sq_area,property_description=property_description,address=address,contact=contact,property_image=image,city_id=city,area_id=area,customers_id=customer_id)
    return redirect('/user/add_property')

def view_my_property(request):
    id = request.user.id
    cus_id = Customers.objects.get(user_id=id)
    customer_id = cus_id.id
    view_property = Post_property.objects.filter(customers_id=customer_id)
    context = {'view_property':view_property}
    return render(request, 'user/view_my_property.html', context)

def add_images(request,id):
    context = {'property_id':id}
    return render(request, 'user/add_images.html', context)

def add_images_store(request):
    add_image = request.FILES['add_image']

    mylocation =  os.path.join(settings.MEDIA_ROOT,'upload')
    obj =  FileSystemStorage(location=mylocation)
    obj.save(add_image.name,add_image)

    property_id = request.POST['hpid']
    
    Add_more_images.objects.create(image=add_image,post_property_id=property_id)
    return redirect('/user/view_my_property')

def view_property_details(request,id):
    result = Post_property.objects.get(pk=id)
    result2 = Add_more_images.objects.filter(post_property_id=id)
    context = {'result':result,'result2':result2}
    return render(request, 'user/view_property_details.html', context)

def search_property(request):
    result = City.objects.all()
    result1 = Area.objects.all()
    context = {'result':result,'result1':result1}
    return render(request, 'user/search_property.html', context)

def search_with_details(request):
    city = request.POST['city']
    area = request.POST['area']
    property_type =  request.POST['property_type']

    request.session['city_id'] = city
    request.session['area_id'] = area
    request.session['property_type'] = property_type

    result = Post_property.objects.filter(city_id=city,area_id=area,property_type=property_type)
    context = {'result':result}
    return render(request, 'user/all_property.html', context)

def view_property(request,id):
    result = Post_property.objects.get(pk=id)
    result2 = Add_more_images.objects.filter(post_property_id=id)
    context = {'result':result,'result2':result2}
    return render(request, 'user/view_property.html', context)



def request(request,id):
    context = {'proerty_id':id}
    return render(request, 'user/request.html', context)

def request_store(request):
    message = request.POST['message']
    property_id = request.POST['proerty_id']

    id = request.user.id
    from_user = Customers.objects.get(user_id=id)
    cid=from_user.id

    result = Post_property.objects.get(pk=property_id)

    Buy_property.objects.create(message=message,post_property_id=property_id,from_user_id=cid,to_user_id=result.customers_id)
    return redirect('/user/search_property')


def view_request(request):
    id = request.user.id
    cus_id = Customers.objects.get(user_id=id)
    result = Buy_property.objects.filter(to_user_id=cus_id, status='pending')
    context = {'result':result}
    return render(request,'user/view_request.html',context)

def accept_request(request,id):
    result = Buy_property.objects.get(pk=id)
    context = {'result':result}
    return render(request,'user/accept_request.html', context)

def accept_request_store(request,id):
    status = request.POST['status']
    reason = request.POST['reason']
    data = {
            'reason' : request.POST['reason'],
            'status' : request.POST['status'],
        }
    Buy_property.objects.update_or_create(pk=id,defaults=data)
    return redirect('/user/view_request')

def all_properties(request):
    result = Post_property.objects.all()
    context = {'result':result}
    return render(request, 'user/all_properties.html', context)

def view_my_request(request):
    id = request.user.id
    cus_id = Customers.objects.get(user_id=id)
    result = Buy_property.objects.filter(from_user_id=cus_id, status='pending')
    context = {'result':result}
    return render(request,'user/view_my_request.html',context)

def change_password(request):
    context = {}
    return render(request, 'user/change_password.html' ,context)

def change_password_update(request):
    username = request.user.username
    old_password  = request.POST['old_password']
    new_password  = request.POST['new_password']
    rnew_password = request.POST['rnew_password']

    if new_password == rnew_password:
        user = auth.authenticate(username=username, password=old_password)
        if user is not None:
            user.set_password(new_password)
            user.save()
            messages.success(request, 'Password Updated Successfully')
            return redirect('/user/login')
        else:
            messages.success(request, 'Invalid Password Try Again')
            return redirect('/user/change_password')     
    else:
         messages.success(request, 'Miss Match Password')

