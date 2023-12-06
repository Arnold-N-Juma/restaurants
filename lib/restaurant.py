class Restaurant:
    restaurants = []

    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        Restaurant.restaurants.append(self)
        self.reviews = []

    def restaurant_name(self):
        return self.name

    def reviews(self):
        return self.reviews

    def customers(self):
        return list(set(review.customer() for review in self.reviews))

    @classmethod
    def all(cls):
        return cls.restaurants

    def add_review(self, customer, rating):
        review = Review(customer, self, rating)
        self.reviews.append(review)

    def average_star_rating(self):
        if not self.reviews:
            return 0
        total_rating = sum(review.rating for review in self.reviews)
        return total_rating / len(self.reviews)

    def __str__(self):
        return f"Restaurant: {self.name}, Cuisine: {self.cuisine_type}"
