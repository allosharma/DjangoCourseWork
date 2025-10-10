from django.shortcuts import render, redirect
from django.http import HttpResponse
from home.forms import StudentForm, StudentFormModel
from home.models import student2, UserProfile
from django.db.models import Q

# Create your views here.
def index(request):
    context = {'form': StudentForm()}
    if request.method == 'POST':
        print(request.method)
        form = StudentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            email = form.cleaned_data['email']
            mobile_number = form.cleaned_data['mobile_number']
            DOB = form.cleaned_data['DOB']
            student_instance = student2(
                name=name,
                age=age,
                email=email,
                mobile_number=mobile_number,
                DOB=DOB
            )
            student_instance.save()
            context = {
                'form': StudentForm(),
                'name': name,
                'age': age,
                'email': email,
                'mobile_number': mobile_number,
                'DOB': DOB,
                'submitted': True
            }
            # return render(request, 'index.html', context=context)
            return redirect('/thank_you')
        # form = StudentForm(request.POST)
        # if form.is_valid():
        #     name = form.cleaned_data['name']
        #     age = form.cleaned_data['age']
        #     email = form.cleaned_data['email']
        #     mobile_number = form.cleaned_data['mobile_number']
        #     context = {
        #         'form': StudentForm(),
        #         'name': name,
        #         'age': age,
        #         'email': email,
        #         'mobile_number': mobile_number
        #     }
        #     return render(request, 'index.html', context=context)
        # else:
        #     context = {'form': form}
        #     return render(request, 'index.html', context=context)
    # names = ['Alok', 'Aman', 'Ankit', 'Ashish', 'Ashu', 'Atul']
    # items = {
    #     'Alok': 'A web developer',
    #     'Aman': 'A data scientist',
    #     'Ankit': 'A machine learning engineer',
    #     'Ashish': 'A backend developer',
    #     'Ashu': 'A frontend developer',
    #     'Atul': 'A full stack developer'
    # }
    # context = {
    #     'names': names,
    #     'items': items,
    #     'fruits': None
    #     }
    return render(request, 'index.html', context=context)

def contact(request):
    # context = {'form': StudentFormModel()}
    context = {'StudentFormModel': StudentFormModel()}
    if request.method == 'POST':
        print(request.method)
        form = StudentFormModel(request.POST)
        if form.is_valid():
            form.save()
            context = {
                'StudentFormModel': StudentFormModel(),
                'submitted': True
            }
            return redirect('/thank_you')
        else:
            context = {'StudentFormModel': form}
            return render(request, 'contact.html', context=context)
    return render(request, 'contact.html', context=context)

def about(request):
    return render(request, 'about.html')

def dynamic_route(request, number):
    return HttpResponse(f"This is dynamic route, your number is {number}.")

def thank_you(request):
    return HttpResponse("Thank you for submitting the form.")

def htmlform(request):
    if request.method == 'POST':
        # print(request.POST)
        name = request.POST.get('name')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        profile_image = request.FILES.get('profile_image')
        print(profile_image)
        print(f"Name: {name}, Email: {email}, Gender: {gender}")
        user_profile = UserProfile(
            name=name,
            email=email,
            gender = gender,
            profile_image=profile_image
        )
        user_profile.save()
        return redirect('/thank_you')
    return render(request, 'htmlform.html')

def search_page(request):
    students = student2.objects.all()
    
    search = request.GET.get('search')

    if search:
        # students = students.filter(name__icontains=search) #iconains means case insensitive, it will search for the name in the database without considering the case
        
        students = students.filter(Q(name__icontains=search) | Q(email__icontains=search) | Q(mobile_number__icontains=search))
        # The Q object is used to encapsulate a collection of keyword arguments. It is used to perform complex queries with OR, AND operations.
        # Here | operator is used for OR operation, & operator is used for AND operation

    age_group = request.GET.get('age_group')
    if age_group == "1":
        students = students.filter(age__gte=16, age__lte= 20).order_by('age') #lte means less than or equals to, gte means greater than equal to
    elif age_group == "2":
        students = students.filter(age__gte=21, age__lt= 25).order_by('age')
    elif age_group == "3":
        students = students.filter(age__gte=25).order_by('age')


    context = {
        'students': students,
        'search': search
    }
    # print(student.name)
    return render(request, 'search.html', context=context)