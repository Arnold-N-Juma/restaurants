from customer import Customer
from restaurant import Restaurant
from review import Review


customer = Customer("John", "Doe", "john@example.com")
restaurant = Restaurant("Italian Delight", "Italian")
rating = 4


review = Review(customer, restaurant, rating)

print(review)
