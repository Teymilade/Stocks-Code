import math

# Define the StockItem class
class StockItem:
    Stock_category = "Car accessories"  # Class-level variable shared by all instances
    
    def __init__(self, stock_code, quantity, price):
        # Constructor to initialise instance variable
        self.__stockCode = stock_code
        self.__quantity = quantity
        self.__price = price

    # Getters for stock name and description (returns default values)
    def getStockName(self):
        return "Unknown stock name."

    def getStockDescription(self):
        return "Unknown stock description."

    # Getter for stock code
    def getStockCode(self):
        return self.__stockCode

    # Getter for quantity
    def getQuantity(self):
        return self.__quantity

    # Getter for price without VAT
    def get_price_without_VAT(self):
        return self.__price

    # Method to increase stock quantity
    def increase_Stock(self, amount):
        if amount < 1:
            print("Error: Amount must be greater than or equal to one.")
            print("-----------------------------------------------------")
        elif self.__quantity + amount > 100:
            print("Error: Stock exceeds maximum limit of 100.")
            print("-----------------------------------------------------")
        else:
            self.__quantity += amount
            print("Amount of stocks bought:", amount)
            print("New stock Quantity:", self.__quantity)
            print("------------------------------------------------------")
    
    # Method to decrease stock quantity
    def sell_Stock(self, amount):
        if amount < 1:
            print("Error: Amount must be greater than zero.")
            print("------------------------------------------------------")
        elif amount > self.__quantity:
            print("Error: Insufficient stock.")
            print("------------------------------------------------------")
        else:
            self.__quantity -= amount
            print("Amount of stocks sold:", amount)
            print("New stock Quantity:", self.__quantity)
            print("------------------------------------------------------")
    
    # Method to adjust the price of the stock
    def adjust_price(self, new_price):
        if new_price < 0:
            print("Error: Price cannot be negative.")
            print("------------------------------------------------------") 
        else:
            self.__price = new_price
            print("Price of stock is", new_price)
            print("------------------------------------------------------")      
    
    # Setter for stock code
    def setStockCode(self, val):
        self.__stockCode = val
            
    # Method to calculate and return price with VAT
    def get_price_with_VAT(self):
        return self.__price * (1 + self.get_VAT() / 100)

    # Getter for VAT rate
    def get_VAT(self):
        return 17.5

    # Method to return a string representation of the stock item
    def __str__(self):
        return (f"\nStock Category: {StockItem.Stock_category}"
                f"\nStock Name: {self.getStockName()}"
                f"\nDescription: {self.getStockDescription()}"
                f"\nStock Code: {self.getStockCode()}"
                f"\nPrice With VAT (%17.5): {self.get_price_with_VAT():.2f}"
                f"\nPrice without VAT: {self.get_price_without_VAT():.2f}"
                f"\nTotal unit in stock: {self.getQuantity()}"
        )


# Define the NavSys class that extends StockItem
class NavSys(StockItem):
    def __init__(self, stock_code, quantity, price, brand):
        super().__init__(stock_code, quantity, price)  # Initialize inherited attributes
        self.__navsysBrand = brand  # Private attribute for NavSys

    # Override the method to return specific stock name
    def getStockName(self):
        return "Navigation system"

    # Override the method to return specific stock description
    def getStockDescription(self):
        return "GeoVision Sat Nav"

    # Setter for the brand
    def setBrand(self, brand):
        self.__navsysBrand = brand

    # Getter for the brand
    def getBrand(self):
        return self.__navsysBrand

    # Provide a custom string representation for NavSys
    def __str__(self):
        return f"{super().__str__()}\nBrand: {self.getBrand()}"


# Function to display menu and interact with the stock item
def menu(nav_item):
    while True:
        print("Current Stock Information:")
        print(nav_item)
        print("\nChoose an Action")
        print("1. Buy/Increase stock")
        print("2. Sell/Decrease stock")
        print("3. Adjust Stock Price")
        print("4. Change the stock code")
        if isinstance(nav_item, NavSys):  #isinstance will Return whether an object is an instance of a class or of a subclass..
            print("5. Change the brand")
            print("6. Exit")
        else:
            print("5. Exit")
        
        choice = input("Enter your choice (1-5):") if not isinstance(nav_item, NavSys) else input("Enter your choice (1-6):")
        
        if choice == '1':
            amount = int(input("Enter the amount to increase:"))
            nav_item.increase_Stock(amount)
        elif choice == '2':
            amount = int(input("Enter the amount to decrease:"))
            nav_item.sell_Stock(amount)
        elif choice == '3':
            new_price = float(input("Enter the new Price:"))
            nav_item.adjust_price(new_price)
        elif choice == '4':
            new_code = input("Enter the new stock code:")
            nav_item.setStockCode(new_code)
        elif choice == '5' and isinstance(nav_item, NavSys):
            new_brand = input("Enter the new brand:")
            nav_item.setBrand(new_brand)
        elif choice == '5' or (choice == '6' and isinstance(nav_item, NavSys)):
            print("Exiting program...")
            break
        else:
            print("Choice selected is not valid. Please choose a valid option (1-5).")

# Main function to create instances and call the menu function
def main():
    nav_item = StockItem("NS101", 10, 99.99)  # Create an instance of StockItem
    nav_item2 = NavSys("NS102", 40, 89.99, "TomTom")  # Create an instance of NavSys
    menu(nav_item)  # Call menu function with StockItem instance
    menu(nav_item2)  # Call menu function with NavSys instance

# Ensure the main function is called when the script runs
if __name__ == "__main__":
    main()
