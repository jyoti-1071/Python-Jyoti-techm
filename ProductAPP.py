class ProductApp:
    def __init__(self):

        self.products = {}

    def add_product(self):
        pid = input("Enter Product ID: ")
        name = input("Enter Product Name: ")
        category = input("Enter Product Category: ")
        price = float(input("Enter Product Price: "))
        mag_date=input("Enter manufacturing date: ")
        exp_date=input("Enter expiry date of product: ")
        self.products[pid] = {'Name': name, 'Category': category, 'Price': price, 'manufacturing_date':mag_date, 'Expiry_date':exp_date}
        print(f"Product {name} added successfully!")

    def update_product(self):
        pid = input("Enter Product ID to update: ")
        if pid in self.products:
            name = input("Enter new Product Name: ")
            category = input("Enter new Product Category: ")
            price = float(input("Enter new Product Price: "))
            mag_date=input("Enter manufacturing date: ")
            exp_date=input("Enter expiry date of product: ")

            self.products[pid] = {'Name': name, 'Category': category, 'Price': price,'manufacturing_date':mag_date, 'Expiry_date':exp_date}
            print(f"Product {pid} updated successfully!")
        else:
            print("Product not found.")

    def delete_product(self):
        pid = input("Enter Product ID to delete: ")
        if pid in self.products:
            del self.products[pid]
            print(f"Product {pid} deleted successfully!")
        else:
            print("Product not found.")

    def get_product_by_id(self):
        pid = input("Enter Product ID to search: ")
        if pid in self.products:
            print(f"Product Details: {self.products[pid]}")
        else:
            print("Product not found.")

    def get_all_products(self):
        if self.products:
            for pid, details in self.products.items():
                print(f"ID: {pid}, Details: {details}")
        else:
            print("No products available.")

    def get_products_by_category(self):
        category = input("Enter Category to search products: ")
        filtered_products = {pid: details for pid, details in self.products.items() if details['Category'].lower() == category.lower()}
        if filtered_products:
            for pid, details in filtered_products.items():
                print(f"ID: {pid}, Details: {details}")
        else:
            print("No products found in this category.")

    def get_products_between_prices(self):
        min_price = float(input("Enter minimum price: "))
        max_price = float(input("Enter maximum price: "))
        filtered_products = {pid: details for pid, details in self.products.items() if min_price <= details['Price'] <= max_price}
        if filtered_products:
            for pid, details in filtered_products.items():
                print(f"ID: {pid}, Details: {details}")
        else:
            print("No products found in this price range.")

    def menu(self):
        while True:
            print("\n--- Product Management App ---")
            print("1. Add Product")
            print("2. Update Product")
            print("3. Delete Product")
            print("4. Get Product By ID")
            print("5. Get All Products")
            print("6. Get Products By Category")
            print("7. Get Products Between Prices")
            print("8. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_product()
            elif choice == '2':
                self.update_product()
            elif choice == '3':
                self.delete_product()
            elif choice == '4':
                self.get_product_by_id()
            elif choice == '5':
                self.get_all_products()
            elif choice == '6':
                self.get_products_by_category()
            elif choice == '7':
                self.get_products_between_prices()
            elif choice == '8':
                print("Exiting the application.")
                break
            else:
                print("Invalid choice, please try again.")

# Create an instance of the ProductApp and start the menu
app = ProductApp()
app.menu()