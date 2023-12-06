class Customer:
    customers = []

    def __init__(self, given_name, family_name, email):
        self.given_name = given_name
        self.family_name = family_name
        self.email = email
        Customer.customers.append(self)

    def given_name(self):
        return self.given_name

    def family_name(self):
        return self.family_name

    def full_name(self):
        return f"{self.given_name} {self.family_name}"

    @classmethod
    def all(cls):
        return cls.customers

    def num_reviews(self):
        return len([review for review in Review.all() if review.customer() == self])

    @classmethod
    def find_by_name(cls, name):
        return next((customer for customer in cls.customers if customer.full_name() == name), None)

    @classmethod
    def find_all_by_given_name(cls, name):
        return [customer for customer in cls.customers if customer.given_name == name]

    def __str__(self):
        return f"Customer: {self.full_name()}, Email: {self.email}"
    
