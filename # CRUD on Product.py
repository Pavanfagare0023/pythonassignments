# CRUD on Product

class Product:
    def __init__(self, productid, name, price):
        self.productid = productid
        self.name = name
        self.price = price

    def __str__(self):
        return f"Id: {self.productid}, Name: {self.name}, Price: {self.price}"

class ProductManager:
    def __init__(self):
        self.products = []

    def create_(self):
        productid = int(input("Enter Product id: "))
        name = input("Enter Product Name: ")
        price = float(input("Enter Product Price: "))
        new_product = Product(productid, name, price)
        self.products.append(new_product)
        print("Product added successfully")

    
    def update_product(self):
        productid = int(input("Enter Product id to update: "))
        for product in self.products:
            if product.productid == productid:
                product.name = input("Enter new product name: ")
                product.price = float(input("Enter new product price: "))
                print("product updated successfully")
                return
        

    def delete_product(self):
        productid = int(input("Enter Product id to delete: "))
        for product in self.products:
            if product.productid == productid:
                self.products.remove(product)
                print("Product removed successfully")
                return
        

def main():
    manager = ProductManager()
    while True:
        print("1. Add Product")
        print("2. View Products")
        print("3. Update Product")
        print("4. Delete Product")
        print("5. Exit")
        choice = int(input("Enter your choice (1-5): "))

        if choice==1:
            manager.create()
        elif choice==2:
            manager.update()
        elif choice==3:
            manager.delete()
        elif choice==4:
            manager.exit()
        elif choice==5:
            break
        else:
            break

main()