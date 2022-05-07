class User:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.name = ""

    def display_user(self):
        print("Username: ", self.username)
        print("Name: ", self.name)


class Product:
    def __init__(self):
        self.productID = ""
        self.price = ""
        self.name = ""
        self.brand = ""
        self.color = ""
        self.numOfItems = ""
        self.description = ""

    def display_product(self):
        print("Product ID: ", self.productID)
        print("Price: ", self.price)
        print("Name: ", self.name)
        print("Brand: ", self.brand)
        print("Color: ", self.color)
        print("Number of items: ", self.numOfItems)
        print("Description: ", self.description)


class Cart:
    def __init__(self):
      self.items = []
      self.totalPrice = ""
      self.cartID = ""

    def display_cart(self):
      for i in range(0, len(self.items)):
        print("Items: ", self.items[i])
      print("Total price: ", self.totalPrice)
      print("Card ID", self.cartID)
