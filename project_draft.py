# Final Project - Dip n Sip Coffee App
# author: omg
# date: 2025-04-
# Purpose of this app to make ordering easy for customers

# Pseudocode
# Create class to house all objects created
# Create functions for all of the for the different window selections
# create local variables in the class
# create buttons, labels,
# add images background images to the program


# Import tkinter module to build GUI applications
import tkinter as tk
from tkinter import messagebox

# Define main class for the application

# Create class as a bluprint for the


class CoffeeOrderingApp:
    def __init__(self, root):
        self.root = root  # Creates the man window if the program
        # Creates the main window title
        self.root.title("Drip n’ Sip Coffee Ordering System")
        # sets the window size for the main window of the program
        self.root.geometry("400x400")

        # Initialize variables to hold order selections
        # will hold the variable for the coffee type variable
        self.coffee_type = tk.StringVar()
        self.size = tk.StringVar()  # create to hold the size choice variable
        self.milk = tk.StringVar()  # created to hold the milk choice variable
        self.sweetener = tk.StringVar()  # create to hold the sweeter choice variable

        # Start with welcome screen
        self.show_welcome_screen()

    # Function to display welcome screen when the app is started
    def show_welcome_screen(self):  # defines the fuction for the welcome screen GUI
        self.clear_window()  # Clear current content from the window

        # Create a welcome label
        welcome_label = tk.Label(
            # Creates a label for the welcome screen
            self.root, text="Welcome to Drip n’ Sip!", font=("Arial", 16))
        # adds a pad of 30 pixels and places the welcome label on the welcome string
        welcome_label.pack(pady=30)

        # Create an "Order Here" button to like to the mene function for orders
        start_button = tk.Button(
            self.root, text="Order Here", command=self.show_menu_screen)
        # adds button to window and adds a y-axis padding of 20 pixels
        start_button.pack(pady=20)

    # Function to show menu screen for coffee types
    def show_menu_screen(self):
        self.clear_window()  # Clear current window

        # # create window label to select coffee type
        label = tk.Label(self.root, text="Select Coffee Type",
                         font=("Arial", 14))
        # adds the label to the window and 10 pixels of pad
        label.pack(pady=10)

        # Create a list of coffee options from the user to choose from
        coffee_options = [
            "Espresso", "Latte", "Cappuccino", "Americano",
            "Cold Brew", "Ice Coffee", "NOLA"
        ]

        # Create for loop for the radio buttons for each coffee type for the user to select
        for coffee in coffee_options:
            tk.Radiobutton(self.root, text=coffee,
                           variable=self.coffee_type, value=coffee).pack(anchor="w")

        # Create next button to go to customization screen to customize the coffee purchase
        next_button = tk.Button(self.root, text="Next",
                                command=self.show_customization_screen)
        # apply the button to the select coffee screen with pad
        next_button.pack(pady=20)

    # Function to show customization screen
    def show_customization_screen(self):
        self.clear_window()  # Clear current window

        # Size selection label
        size_label = tk.Label(
            self.root, text="Select Size", font=("Arial", 12))
        size_label.pack(pady=5)

        # Size options
        size_options = ["Café (4oz)", "Small (8oz)",
                        "Medium (12oz)", "Large (16oz)"]
        for size in size_options:
            tk.Radiobutton(self.root, text=size,
                           variable=self.size, value=size).pack(anchor="w")

        # Milk selection label
        milk_label = tk.Label(
            self.root, text="Select Milk", font=("Arial", 12))
        milk_label.pack(pady=5)

        # Milk options
        milk_options = ["Whole", "Skim", "Almond", "Soy"]
        for milk in milk_options:
            tk.Radiobutton(self.root, text=milk,
                           variable=self.milk, value=milk).pack(anchor="w")

        # Sweetener selection label
        sweet_label = tk.Label(
            self.root, text="Select Sweetener", font=("Arial", 12))
        sweet_label.pack(pady=5)

        # create a list for sweetener options
        sweetener_options = ["Sugar", "Whipped Cream",
                             "Honey", "Stevia", "Syrup Flavors"]
        # Radio button created to pick sweetner options
        for sweet in sweetener_options:
            tk.Radiobutton(self.root, text=sweet,
                           variable=self.sweetener, value=sweet).pack(anchor="w")

        # Button to show order summary
        next_button = tk.Button(self.root, text="Next",
                                command=self.show_order_summary)
        next_button.pack(pady=10)  # add label with padding of 10

    # Function to show order summary
    def show_order_summary(self):
        self.clear_window()  # Clear current window

        # Create a summary message using selected options
        summary = f"Order Summary:\n\nCoffee: {self.coffee_type.get()}\nSize: {self.size.get()}\nMilk: {self.milk.get()}\nSweetener: {self.sweetener.get()}"

        # Display order summary
        label = tk.Label(self.root, text=summary,
                         font=("Arial", 12), justify="left")
        label.pack(pady=20)  # add label with padding of 20

        # Button to place order on the summary screen
        place_order_btn = tk.Button(
            self.root, text="Place Order", command=self.confirm_order)
        # adds button to the window and a pad of 10
        place_order_btn.pack(pady=10)

    # Function to confirm the order
    def confirm_order(self):
        self.clear_window()  # Clear current window

        # Confirmation message that he order has gone through
        confirm_label = tk.Label(
            self.root, text="Thank you for your order!", font=("Arial", 16))
        confirm_label.pack(pady=40)  # add label with padding of 40

        # Button to return to start
        restart_btn = tk.Button(
            self.root, text="Place Another Order", command=self.show_welcome_screen)
        restart_btn.pack(pady=10)  # add label with padding of 10

    # Utility function to clear the window for new content
    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()


# Run the app
if __name__ == "__main__":
    root = tk.Tk()  # Create main Tkinter window
    app = CoffeeOrderingApp(root)  # Create instance of our app
    root.mainloop()  # Run the application loop
