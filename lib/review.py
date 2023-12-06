class Review:
    reviews = []

    def __init__(self, customer, restaurant, rating, comment=None):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        self.comment = comment
        Review.reviews.append(self)

    def rating(self):
        return self.rating

    @classmethod
    def all(cls):
        return cls.reviews

    def customer(self):
        return self.customer

    def restaurant(self):
        return self.restaurant

    def __str__(self):
        return f"Review by {self.customer.full_name()} for {self.restaurant.name}: {self.rating} stars, Comment: {self.comment}"
