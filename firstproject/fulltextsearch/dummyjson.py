import os
import sys
import django
import requests

# Add project root (one level up) to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set up Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'firstproject.settings')
django.setup()

from fulltextsearch.models import Product

Product.objects.all().delete()  # Clear existing data to avoid duplicates

def insertData():
    url = "https://dummyjson.com/products?limit=200"
    response = requests.get(url)
    data = response.json()

    for item in data['products']:
        try:
            Product.objects.create(
                title=item['title'],
                description=item['description'],
                category=item['category'],
                price=item['price'],
                brand=item['brand'],
                sku=item['sku'],
                thumbnail_url=item['thumbnail']
            )
            print(f"Inserted: {item['title']}")
        except Exception as e:
            print(f"Error creating product {item['title']}: {e}")

if __name__ == "__main__":
    insertData()