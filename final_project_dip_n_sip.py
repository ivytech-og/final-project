# Final Project - Dip n Sip Coffee App
# author: omg
# date: 2025-05-08
# Purpose of this app to allow customers select a coffee, customize it and place and order through a GUI
# CODE ASSISTANCE https://www.youtube.com/watch?v=pBoeFAapQx8
# CODE ASSISTANCE https://github.com/AmirakbariSXL/CoffeeShopOrder/blob/main/CoffeShop.py
# CODE ASSISTANCEhttps://www.youtube.com/watch?v=x-QgQebpQEM


# Pseudocode
# Create class to house all objects created
# Create functions for all of the for the different window selections with error correction
# create local variables in the class
# create buttons, labels,
# add images background images to the program
# use try except statements for error handling

# ------ Start Program design-------
# Import tkinter for GUI components
import tkinter as tk

# Import messagebox for user prompts (e.g., order confirmation)
from tkinter import messagebox

# Import Image modules from Pillow for displaying coffee images
from PIL import Image, ImageTk

# NEW: Import os to construct robust image paths
import os


class CoffeeApp:
    # Main GUI class for the Coffee Ordering App.
    # This class handles:
    # Displaying the welcome screen
    # Navigating through order, customization, and summary windows
    # Managing user selections and order confirmations

    def __init__(self, root):
        # Initializes the main application window and sets up the welcome screen.
        # root: The main Tkinter window object.

        self.root = root  # The main tkinter window
        # Sets the window title
        self.root.title("Drip n' Sip Coffee Ordering System")
        self.root.geometry("300x200")  # Set the initial size of the window

        self.order_window = None  # Placeholder for the order selection window

        self.welcome_screen()  # Load the welcome screen on app start

    # NEW: Add a helper function to build full paths to images
    def get_image_path(self, filename):
        # Resolves the full path to an image in the images folder
        # Get the folder where the script is located
        base_dir = os.path.dirname(os.path.abspath(__file__))
        # Return full path to image file
        return os.path.join(base_dir, "images", filename)

    def welcome_screen(self):
        # Displays the welcome screen with branding, image, and navigation buttons.

        # Remove any widgets that may be on the screen
        self.clear_screen(self.root)

        # Display the welcome title
        tk.Label(self.root, text="Welcome to Drip n' Sip!",
                 font=("Arial", 20)).pack(pady=10)

        # Attempt to display the first coffee image
        try:
            # NEW: Use get_image_path instead of hardcoding image path
            # Load the image from file
            img1 = Image.open(self.get_image_path("coffee1.png"))
            img1 = img1.resize((100, 100))  # Resize image for display
            # Convert to Tkinter-compatible image
            photo1 = ImageTk.PhotoImage(img1)

            label_img1 = tk.Label(self.root, image=photo1)
            label_img1.image = photo1  # Prevent garbage collection of image
            label_img1.pack()
            # Alt text displayed below image
            label_img1.config(text="Cup of Coffee", compound='top')
        except FileNotFoundError:
            # Fallback text
            tk.Label(self.root, text="[Image: Cup of Coffee]").pack()

        # Navigation Buttons
        tk.Button(self.root, text="Order Here",
                  command=self.open_order_window).pack(pady=5)  # Start order
        tk.Button(self.root, text="Exit", command=self.exit_app).pack(
            pady=5)  # Close application

    def open_order_window(self):
        # Opens a new window for selecting coffee type.

        if self.order_window:
            self.order_window.destroy()  # Close any existing window

        # Create a new top-level window
        self.order_window = tk.Toplevel(
            self.root)  # window for coffee ordering
        self.order_window.title("Order Your Coffee")
        self.order_window.geometry("400x600")  # Set size for ordering screen

        tk.Label(self.order_window, text="Choose Your Coffee",
                 font=("Arial", 16)).pack(pady=10)

        # --- Display second image for aesthetic ---
        # Attempt to load and display image
        try:
            # NEW: Use get_image_path instead of hardcoding image path
            img2 = Image.open(self.get_image_path(
                "coffee2.png"))  # Load second image
            img2 = img2.resize((120, 120))  # Resize image
            photo2 = ImageTk.PhotoImage(img2)

            label_img2 = tk.Label(self.order_window, image=photo2)
            label_img2.image = photo2  # keep image in memory
            label_img2.pack()
            label_img2.config(text="Coffee Beans",
                              compound='top')  # Image label
        except FileNotFoundError:
            tk.Label(self.order_window, text="[Image: Coffee Beans]").pack()

        # Variable to hold selected coffee type
        # Default coffee selection is Espresso
        self.coffee_var = tk.StringVar(value="Espresso")

        # --- List of available coffee types as radio buttons
        coffees = ["Espresso", "Latte", "Cappuccino",
                   "Americano", "Cold Brew", "Ice Coffee", "NOLA"]
        for coffee in coffees:
            tk.Radiobutton(self.order_window, text=coffee,
                           variable=self.coffee_var, value=coffee).pack(anchor='w')

        # Add buttons for navigation Buttons
        tk.Button(self.order_window, text="Next",
                  command=self.next_customization).pack(pady=10)
        tk.Button(self.order_window, text="Back",
                  command=self.order_window.destroy).pack(pady=5)

    def next_customization(self):
        # Displays customization options for coffee (size, milk, sweetener).

        self.clear_screen(self.order_window)  # Clear previous widgets

        tk.Label(self.order_window, text="Customize Your Coffee",
                 font=("Arial", 16)).pack(pady=10)

        # Declare variables to hold user selections for the customization options
        self.size_var = tk.StringVar(
            value="Espresso (2oz)")  # Default coffee size
        self.milk_var = tk.StringVar(value="None")        # Default milk type
        self.sweetener_var = tk.StringVar(value="None")   # Default sweetener

        # Size options section
        tk.Label(self.order_window, text="Select Size:").pack()
        sizes = ["Espresso (2oz)", "Café (4oz)", "Small (8oz)",
                 "Medium (12oz)", "Large (16oz)"]
        for size in sizes:
            tk.Radiobutton(self.order_window, text=size,
                           variable=self.size_var, value=size).pack(anchor='w')

        # Milk options section
        tk.Label(self.order_window, text="Select Milk:").pack()
        milks = ["None", "Whole", "Skim", "Almond", "Soy"]
        for milk in milks:
            tk.Radiobutton(self.order_window, text=milk,
                           variable=self.milk_var, value=milk).pack(anchor='w')

        # Sweetener options section
        tk.Label(self.order_window, text="Select Sweetener:").pack()
        sweeteners = ["None", "Sugar", "Whipped Cream",
                      "Honey", "Stevia", "Syrup Flavors"]
        for sweetener in sweeteners:
            tk.Radiobutton(self.order_window, text=sweetener,
                           variable=self.sweetener_var, value=sweetener).pack(anchor='w')

        # Navigation Buttons
        tk.Button(self.order_window, text="See Summary",
                  command=self.show_summary).pack(pady=10)
        tk.Button(self.order_window, text="Back",
                  command=self.open_order_window).pack(pady=5)

    def show_summary(self):
        # Displays a summary of the user's coffee order for review.

        # Prices dictionary for sizes available
        PRICES = {
            "Espresso (2oz)": 2.50,
            "Café (4oz)": 3.00,
            "Small (8oz)": 3.50,
            "Medium (12oz)": 4.00,
            "Large (16oz)": 4.50,
        }

        base_price = PRICES[self.size_var.get()]  # Get price from dictionary
        total = base_price  # Store total cost

        # Validate selections before proceeding
        if not all([self.coffee_var.get(), self.size_var.get(), self.milk_var.get(), self.sweetener_var.get()]):
            messagebox.showerror(
                "Input Error", "Please make a selection for all options.")
            return

        self.clear_screen(self.order_window)  # Clear customization widgets
        self.order_window.geometry("400x600")  # Reapply window size

        # Format of summary data in f string
        summary = (f"Coffee: {self.coffee_var.get()}\n"
                   f"Size: {self.size_var.get()}\n"
                   f"Milk: {self.milk_var.get()}\n"
                   f"Sweetener: {self.sweetener_var.get()}\n"
                   f"Total: ${total:.2f}")

        # Display summary
        tk.Label(self.order_window, text="Order Summary",
                 font=("Arial", 16)).pack(pady=10)
        tk.Label(self.order_window, text=summary,
                 font=("Arial", 12)).pack(pady=10)

        # Navigation Buttons
        tk.Button(self.order_window, text="Place Order",
                  command=self.place_order).pack(pady=10)
        tk.Button(self.order_window, text="Back",
                  command=self.next_customization).pack(pady=5)

    def place_order(self):
        # Confirms the order and closes the order window.
        # prompts a thank you message
        # Show confirmation
        messagebox.showinfo("Order Placed", "Thank you for your order!")
        self.order_window.destroy()  # Close the order window and end program

    def exit_app(self):
        # Confirms with the user before exiting the app.

        if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
            self.root.destroy()  # Close the root window

    # clear screen method
    def clear_screen(self, window):
        # Removes all widgets from a specified Tkinter window.
        # window: The window to be cleared.

        for widget in window.winfo_children():
            widget.destroy()  # Destroy each widget in the window


# ------------------ Main Execution Section ------------------
if __name__ == "__main__":
    root = tk.Tk()  # Create the main application window
    app = CoffeeApp(root)  # Instantiate the CoffeeApp with the root window
    root.mainloop()  # Start the Tkinter event loop to display the GUI
