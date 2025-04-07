#  Asseessment on Class

# 1.Create a class Student,  create accept method to get the 3 subjects marks
# Create calculate method to get total & percentage
# Create display method to show total marks & percentage

class Student:
    def accept(self):
        self.sub1 = int(input("Enter marks for Subject 1: "))
        self.sub2 = int(input("Enter marks for Subject 2: "))
        self.sub3 = int(input("Enter marks for Subject 3: "))

    def calculate(self):
        self.total = self.sub1 + self.sub2 + self.sub3
        self.percentage = self.total / 3

    def display(self):
        print("Total Marks:", self.total)
        print("Percentage:", round(self.percentage, 2))

s = Student()
s.accept()
s.calculate()
s.display()


# 2. Create class Circle, accept the radius & calculate the area of circle & display

class Circle:
    def accept(self):
        # Accepting radius as input from the user and converting it to float
        self.radius = float(input("Enter radius of the circle: "))

    def calculate_area(self):
        # Using approximate value of pi (π ≈ 3.1416)
        pi = 3.1416
        # Formula for area of circle = π * r^2
        self.area = pi * self.radius * self.radius

    def display(self):
        # Printing the area rounded to 2 decimal places
        print("Area of Circle:", round(self.area, 2))


c = Circle()
c.accept()         
c.calculate_area() 
c.display()        


# 3. Create product class accept  code, name, price , give 20% discount if price is >10000,  5k-10k 15% discount , below 5k 5% discount
# Display code, name, actual price & discounted price

class Product:
    def get_details(self):
        self.product_code = input("Enter product code: ")
        self.product_name = input("Enter product name: ")
        self.product_price = float(input("Enter product price: "))

    def apply_discount(self):
        
        if self.product_price > 10000:
            discount_rate = 0.20
        elif self.product_price >= 5000:
            discount_rate = 0.15
        else:
            discount_rate = 0.05
        
        self.discount_amount = self.product_price * discount_rate
        self.final_price = self.product_price - self.discount_amount

    def show_details(self):
        print("Product Code:", self.product_code)
        print("Product Name:", self.product_name)
        print("Original Price:", self.product_price)
        print("Price After Discount:", round(self.final_price, 2))


product = Product()
product.get_details()
product.apply_discount()
product.show_details()



