import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'firstproject.settings')
django.setup()
import random
from home.models import Brand, Products, Person
import faker
fake = faker.Faker()

Products.objects.create(
    brand = Brand.objects.first(),
    product_name = 'Men Trimmer With Ceramic Blades' # + str(random.randint(1, 1000))
)

#Update the product name
product = Products.objects.get(id= 4)
product.product_name = 'Updated Product Name' # + str(random.randint(1, 1000))
product.save()
#Now if we update the product then the slug will also be updated, which is not a good practice because the slug is used in the URL and if the slug is changed then the URL will also be changed and it will lead to 404 error.
# So, we will only set the slug when the product is created for the first time and not update it again.
# To do this, we can check if the slug is already set or not in the save method of the Products model in models.py file.


# Advantage with bluk_create is that it will create all the objects in a single query, which is more efficient than creating objects one by one.
def bulkCreatePerson(num):
    create = [Person(person_name = fake.name()) for _ in range(num)]
    Person.objects.bulk_create(create)

# bulkCreatePerson(50)

# Advantage of bulk update is that it will update all the objects in a single query, which is more efficient than updating objects one by one.
def bulkUpdatePerson(name):
    print(Person.objects.filter(person_name__icontains=name).count())
    Person.objects.filter(person_name__icontains=name).update(person_name='Alok Sharma')
    # persons = Person.objects.all()
    # for person in persons:
    #     person.person_name = fake.name()
    # Person.objects.bulk_update(persons, ['person_name'])

# bulkUpdatePerson('Michael')

# Advantage of bulk delete is that it will delete all the objects in a single query, which is more efficient than deleting objects one by one.
def bulkDeletePerson(name):
    print(Person.objects.filter(person_name__icontains=name).count())
    Person.objects.filter(person_name__icontains=name).delete()
    # Person.objects.all().delete() # Uncomment this line to delete all the objects in the Person model

# bulkDeletePerson('Alok')


