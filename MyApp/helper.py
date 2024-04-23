from .models import *
def function():
    products = [
        {'name': 'Headphones', 'price': 200, 'rating': 3},
        {'name': 'Smartwatch', 'price': 300, 'rating': 4},
        {'name': 'Tablet', 'price': 800, 'rating': 5},
        {'name': 'Camera', 'price': 1200, 'rating': 2},
        {'name': 'Speaker', 'price': 250, 'rating': 1},
        {'name': 'Gaming Console', 'price': 400, 'rating': 3},
        {'name': 'Fitness Tracker', 'price': 150, 'rating': 4},
        {'name': 'E-reader', 'price': 100, 'rating': 4},
        {'name': 'Wireless Router', 'price': 80, 'rating': 5},
        {'name': 'External Hard Drive', 'price': 120, 'rating': 4},
        {'name': 'Bluetooth Earbuds', 'price': 100, 'rating': 3},
        {'name': 'Portable Charger', 'price': 50, 'rating': 2},
        {'name': 'Virtual Reality Headset', 'price': 300, 'rating': 5},
        {'name': 'Wireless Mouse', 'price': 40, 'rating': 1}
    ]

    for product in products:
        obj = Product(name=product['name'], price=product['price'], rating=product['rating'])
        print(obj)
        obj.save()
        print(obj)
        print("-------------------")