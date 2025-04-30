# Final Project - Dip n Sip Coffee App
# author: omg
# date: 2025-04-
# Purpose of this app to make ordering easy for customers
# CODING ASSISTANCE https://python.plainenglish.io/coffee-shop-implementation-in-python-b9e9671295db
# CODING ASSISTANCE https://github.com/AmirakbariSXL/CoffeeShopOrder/blob/main/CoffeShop.py


# Pseudocode
# Create class to house all objects created
# Create functions for all of the for the different window selections
# Create functions for welcome screen, coffee choice menu, customization menu
# create local variables in the functions ans class
# create buttons and labels to identify windows and to move throught he app


# Import tkinter module to build GUI applications
import tkinter as tk
from tkinter import messagebox


# Defines the mainclass to for the coffee ordering app
class CoffeeOrderingApp:
    def __init__(self, root):
        self.root = root  # Creates the main window for the app
        # sets the window title for the main app
        self.root.title("Drip n’ Sip Coffee Ordering System")
        # sets the window size for the main window
        # sets the window size for the main window in pixels
        self.root.geometry("400x500")

       # Creates objects to store the selections for the users
        self.coffee_type = tk.StringVar()
        self.size = tk.StringVar()  # create to hold the size choice variable
        self.milk = tk.StringVar()  # created to hold the milk choice variable
        self.sweetener = tk.StringVar()  # create to hold the sweeter choice variable

        # Calls the method to display the welcome screen to the user
        self.show_welcome_screen()

    # Defines th method clear_window for retrieving and clearing widgets in the window
    def clear_window(self):
        for widget in self.root.winfo_children():  # gathers widgets in the window
            widget.destroy()  # removes the widgets from the screen

    # Defines the method to show the welcome screen
    def show_welcome_screen(self):
        self.clear_window()  # Calls the clear window method to clear any widgets

        # Creates a welcome label for the welcome screen
        welcome_label = tk.Label(
            # creates the label text and applies the Arial font.
            self.root, text="Welcome to Drip n’ Sip!", font=("Arial", 16))
        # adds a pad of 30 pixels and displays the welcome message.
        welcome_label.pack(pady=30)

        # Create an "Order Here" button for the window and sets it to call the menu screen
        start_button = tk.Button(
            self.root, text="Order Here", command=self.show_menu_screen)
        # displays the button on the window screen with pad
        start_button.pack(pady=20)

    # Defines the method that will brin up the menu screen
    def show_menu_screen(self):
        self.clear_window()  # calls the clear window method to clear any widgets

        # Creates a label for coffe type and applies font
        label = tk.Label(self.root, text="Select Coffee Type",
                         font=("Arial", 14))
        label.pack(pady=10)  # displays the label on the window with a pad

        # Create a list of coffee options from the user to choose from and places it in a variable
        coffee_options = [
            "Espresso", "Latte", "Cappuccino", "Americano",
            "Cold Brew", "Ice Coffee", "NOLA"
        ]

        # creates a for loop to radio buttons for all of the coffee options in the list
        for coffee in coffee_options:
            tk.Radiobutton(self.root, text=coffee,
                           variable=self.coffee_type, value=coffee).pack(anchor="w")

        # Create next button to call the customization screen
        next_button = tk.Button(self.root, text="Next",
                                command=self.show_customization_screen)
        # apply the button to the select coffee screen with pad
        next_button.pack(pady=20)  # adds the button to the window

    # Defines the method to create the customization screen
    def show_customization_screen(self):
        self.clear_window()  # Clears any existing widgets from the window

        # Creates the size label for the window and applies the font
        size_label = tk.Label(
            self.root, text="Select Size", font=("Arial", 12))
        size_label.pack(pady=5)  # places the label on the window

        # Creates a list for the sizes offered to the customer
        size_options = ["Café (4oz)", "Small (8oz)",
                        "Medium (12oz)", "Large (16oz)"]
        # for loop to create a radio button for all of the different sizes offered.
        for size in size_options:
            tk.Radiobutton(self.root, text=size,
                           variable=self.size, value=size).pack(anchor="w")

        # creates the milk selection label for the window
        milk_label = tk.Label(
            self.root, text="Select Milk", font=("Arial", 12))
        # applies the milk selection label to the window
        milk_label.pack(pady=5)

        # Creates a list of the milk options that are available to the user
        milk_options = ["Whole", "Skim", "Almond", "Soy"]
        for milk in milk_options:  # applies a for loop to create all the radio buttons for the options of milk
            tk.Radiobutton(self.root, text=milk,
                           variable=self.milk, value=milk).pack(anchor="w")

        # Creates a label for the window
        sweet_label = tk.Label(
            self.root, text="Select Sweetener", font=("Arial", 12))
        sweet_label.pack(pady=5)  # adds the sweetner label to the window

        # Creates a list of the sweetner options for the user to choose from
        sweetener_options = ["Sugar", "Whipped Cream",
                             "Honey", "Stevia", "Syrup Flavors"]
        for sweet in sweetener_options:  # creates a for loop to create radio buttons for all the sweetner optons
            tk.Radiobutton(self.root, text=sweet,
                           variable=self.sweetener, value=sweet).pack(anchor="w")

        # Create next button for
        next_button = tk.Button(self.root, text="Next",
                                command=self.show_order_summary)
        next_button.pack(pady=10)  # applies the button to the window

    # Defines the method to show the summary of the selections from the other methods/functions
    def show_order_summary(self):
        self.clear_window()  # clears the window of any widgets
        # creates the summary to be display using formatted strings
        summary = f"You ordered a: {self.size.get()}{self.coffee_type.get()} with {self.milk.get()} milk and {self.sweetener.get()}."
        #creates the summary information label to be applied to the window
        summary_label = tk.Label(
            self.root, text=summary, font=("Arial", 12), wraplength=300)
        summary_label.pack(pady=20)# applies the information to the window
        # creates start over button to redo the entire process
        start_over = tk.Button(
            self.root, text="Start Over", command=self.show_welcome_screen)
        start_over.pack(pady=10) # adds the start over button to the screen
        # creates the place order button to place the order and complete the app
        place_order_button = tk.Button(self.root, text="Place Order",
                                       command=self.place_order)
        place_order_button.pack(pady=10) # adds the place order button to the window

    # Defines the method place order to order the item and and close program
    def place_order(self):
        messagebox.showinfo("Order Placed", "Thank you for your order!") # Displays message box with string
        self.root.destroy() # closes the message box 


# checks to see if the python app is run directly or imported.
if __name__ == "__main__":
    root = tk.Tk()  # Create main Tkinter window
    app = CoffeeOrderingApp(root)  # Starts the app
    root.mainloop()  # Runs the application loop and keeps it from closing
