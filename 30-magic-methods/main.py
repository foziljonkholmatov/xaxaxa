# class Contact:
#     def __init__(self, name, phone_number):
#         self.name = name
#         self.phone_number = phone_number
#
#
#     def __str__(self):
#         return f"{self.name} : {self.phone_number}"
#
#     def __repr__(self):
#         return f"Contact {self.name} : {self.phone_number}"
#
# c1 = Contact('ali',+9989)
# print(str(c1))
#
# c2 = Contact('vali', +998955588899)
# print(repr(c2))
#
#
# class Book:
#     def __init__(self, pages):
#         self.pages = pages
#         self.index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index < len(self.pages):
#             page = self.pages[self.index]
#             self.index +=  1
#             return page
#         else:
#             raise StopIteration
#
# book = Book(["Sahifa 1", "Sahifa 2", "Sahifa 3"])
# for page in book:
#      print(page)
#


# class ShoppingCart:
#     def __init__(self):
#         self.products = []
#
#     def add_product(self, product):
#         self.products.append(product)
#
#     def __add__(self, other):
#         new_cart = ShoppingCart()
#         new_cart.products = self.products + other.products
#         return new_cart
#
#     def __str__(self):
#         return ', '.join(self.products)
#
#
# cart1 = ShoppingCart()
# cart1.add_product("Laptop")
# cart1.add_product("Smartphone")
#
# cart2 = ShoppingCart()
# cart2.add_product("Headphones")
# cart2.add_product("Mouse")
#
# cart3 = cart1 + cart2
# print("Birlashtirilgan savat:", cart3)  # Laptop, Smartphone, Headphones, Mouse


# """4. __call__ — SMS yuboruvchi obyekt
# Vazifa: SMS yuboradigan obyekt yaratilsin."""
#
# class SmsSender:
#     def __init__(self, name):
#         self.name = name
#
#     def __call__(self, phone, message):
#
#         print(f"from {self.name} to {phone}")
#         print(f"Message: {message}")
#
#
# s1 = SmsSender('Beeline')
# s1("+998901534443", "Test")
#
#
# """5. __contains__ va __len__ — Ishchilar ro‘yxati
# Vazifa: Ishchilar ro‘yxatini tekshirish
# """
#
# class Company:
#     def __init__(self, name, employee):
#         self.name = name
#         self. employee = employee
#
#     def __contains__(self, employees):
#         return employees in self.employee
#
#     def __len__(self):
#         return len(self.employee)
#
#
#
# it_company = Company("TechSoft", ["Ali", "Laylo", "Bobur"])
# print("Ali" in it_company)
# print(len(it_company))


""" _getitem__, __setitem__, __delitem__ — Elektron kundalik (dnevnik)
Vazifa: O‘quvchining fanlar bo‘yicha baholarini boshqaradigan klass yozing"""

class Diary:
    def __init__(self):
        self.grades = {}

    def __getitem__(self, sub):
        if sub in self.grades:
            return self.grades[sub]










