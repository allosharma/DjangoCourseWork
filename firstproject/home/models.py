from django.db import models
from home.utils import generate_slug
from django.db.models import Q, CheckConstraint, UniqueConstraint

# Create your models here.
class Student(models.Model):
    
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    mobile_number = models.CharField(max_length=15)
    gender_choices = (('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other'))
    gender = models.CharField(max_length=10, choices=gender_choices, default='Male')
    age = models.IntegerField(null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    student_bio = models.TextField(null=True, blank=True)
    file = models.FileField(upload_to='documents/', null=True, blank=True)
    created_at = models.DateTimeField(auto_created=True, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Person(models.Model):
    person_name = models.CharField(max_length=100)

    def __str__(self):
        return self.person
    
class student2(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    mobile_number = models.CharField(max_length=15)
    DOB = models.DateField()

    def __str__(self):
        return self.name
    
class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=10)
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Author(models.Model):
    author_name = models.CharField(max_length=100)

    def __str__(self):
        return self.author_name

class Book(models.Model):
    
    #on_delete=models.CASCADE means if author is deleted then all the books of that author will be deleted, it means that if the parent is deleted then all the child will be deleted
    #on_delete=models.SET_NULL means if author is deleted then the author field of the book will be set to null
    #on_delete=models.PROTECT means if author is deleted then the book will not be deleted and an error will be raised
    #on_delete=models.restrict means if the Author is getting deleted then it will not allow to delete the Author if there are any books associated with that author
    #on_detete=model.Default means if the author is deleted then the author field of the book will be set to the default value
    author = models.OneToOneField(Author, on_delete=models.CASCADE, related_name='books')

    book_name = models.CharField(max_length=100)

    def __str__(self):
        return self.book_name
    
    class Meta: #Meta class is used to change the default behavior of the model
        db_table = 'book_table' # It will change the table name in the database to book_table instead of appname_modelname
        ordering = ('book_name', '-author_id')  # It will order the books in ascending order of book_name, it will not affect the data in the database, it will only affect the way we get the data from the database
        verbose_name = 'Book'  # It will change the name of the model in the admin panel to Book instead of Books
        verbose_name_plural = 'Books'  # It will change the plural name of the model in the admin panel to Books instead of Books
        unique_together = ('author', 'book_name')  # It will make the combination of author and book_name unique, it means that the same author cannot have two books with the same name.
        

class Publisher(models.Model):
    publisher_name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, related_name='publishers')

    def __str__(self):
        return self.publisher_name
    
# It will show ForeignKey relationship
class Distributor(models.Model):
    distributor_name = models.CharField(max_length=100)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='distributors')

    def __str__(self):
        return self.distributor_name

class Brand(models.Model):
    brand_name = models.CharField(max_length=100)

    def __str__(self):
        return self.brand_name
    
class Products(models.Model):
    product_name = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='products')
    slug = models.SlugField(max_length=100, null=True, blank=True)

    def save(self, *args, **kwargs):
        # print('save method called')
        if not self.id:  # Only set the slug if it is not already set
            self.slug = generate_slug(self.product_name, Products)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.product_name
    
class HumanManager(models.Manager):
    def get_queryset(self):
        # return super().get_queryset().filter(age__gte=18)
        return super().get_queryset().filter(is_deleted=False)
    
class Human(models.Model):
    human_name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    mobile_number = models.CharField(max_length=15)

    objects = HumanManager()  # Our custom manager.
    new_humans = models.Manager()  # The default manager.
    # When you will call Human.objects.all() then it will return only those humans who are not soft deleted
    # When you will call Human.new_humans.all() then it will return all the humans including the soft deleted humans
    
    def __str__(self):
        return self.human_name
    
    class Meta:
        abstract = True  # It will not create a table for this model in the database, it will only be used as a base class for other models.
        # I have create two models Employee and Customer which will inherit from this Human model.
        permissions = [  # ✅ Correct plural name
        ("can_delete", "Can delete record"),
        ("can_update", "Can update record")]
        # You can add custom permissions to the model
        # restrictions = models.RestrictedError  # It will raise an error if we try to delete a Human object if there are any Employee or Customer objects associated with that Human object.
        constraints = [
            CheckConstraint(check=Q(age__gte=12), name='age_gte_12'),  # It will ensure that the age is greater than or equal to 0
            UniqueConstraint(fields=['email', 'mobile_number'], name='unique_email_mobile')  # It will ensure that the combination of email and mobile_number is unique
        ]

class Employee(Human):
    employee_id = models.CharField(max_length=100)
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.human_name + ' - ' + self.employee_id
    
    class Meta:
        # index_together = ('employee_id', 'human_name')  # It will create an index on the combination of 'employee_id', 'human_name', it will make the queries faster when we filter the books based on 'employee_id', 'human_name'.
        # proxy = True # It will not create a new table for this model in the database, it will only create a proxy model for the Human model.
        # Proxy as True will make sure it does not follows the Meta class of the parent model.
        constraints = [
                CheckConstraint(check=Q(age__gte=20), name='age_gte_20'),  # It will ensure that the age is greater than or equal to 20
            ]


class Customer(Human):
    customer_id = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.human_name + ' - ' + self.customer_id