import tkinter as tk
from tkinter import messagebox

# --- Functions ---


def welcome_screen():
    clear_screen(root)
    tk.Label(root, text="Welcome to Drip n' Sip!",
             font=("Arial", 20)).pack(pady=10)
    tk.Button(root, text="Order Here", command=open_order_window).pack(pady=5)
    tk.Button(root, text="Exit", command=exit_app).pack(pady=5)


def open_order_window():
    global order_window
    order_window = tk.Toplevel(root)
    order_window.title("Order Your Coffee")

    tk.Label(order_window, text="Choose Your Coffee",
             font=("Arial", 16)).pack(pady=10)

    global coffee_var
    coffee_var = tk.StringVar(value="Espresso")
    coffees = ["Espresso", "Latte", "Cappuccino",
               "Americano", "Cold Brew", "Ice Coffee", "NOLA"]
    for coffee in coffees:
        tk.Radiobutton(order_window, text=coffee,
                       variable=coffee_var, value=coffee).pack(anchor='w')

    tk.Button(order_window, text="Next",
              command=next_customization).pack(pady=10)
    tk.Button(order_window, text="Back",
              command=order_window.destroy).pack(pady=5)


def next_customization():
    clear_screen(order_window)

    tk.Label(order_window, text="Customize Your Coffee",
             font=("Arial", 16)).pack(pady=10)

    global size_var, milk_var, sweetener_var
    size_var = tk.StringVar(value="Small")
    milk_var = tk.StringVar(value="Whole")
    sweetener_var = tk.StringVar(value="Sugar")

    # Size Options
    tk.Label(order_window, text="Select Size:").pack()
    sizes = ["Café (4oz)", "Small (8oz)", "Medium (12oz)", "Large (16oz)"]
    for size in sizes:
        tk.Radiobutton(order_window, text=size,
                       variable=size_var, value=size).pack(anchor='w')

    # Milk Options
    tk.Label(order_window, text="Select Milk:").pack()
    milks = ["None", "Whole", "Skim", "Almond", "Soy"]
    for milk in milks:
        tk.Radiobutton(order_window, text=milk,
                       variable=milk_var, value=milk).pack(anchor='w')

    # Sweetener Options
    tk.Label(order_window, text="Select Sweetener:").pack()
    sweeteners = ["None", "Sugar", "Whipped Cream",
                  "Honey", "Stevia", "Syrup Flavors"]
    for sweetener in sweeteners:
        tk.Radiobutton(order_window, text=sweetener,
                       variable=sweetener_var, value=sweetener).pack(anchor='w')

    tk.Button(order_window, text="See Summary",
              command=show_summary).pack(pady=10)


def show_summary():
    if not coffee_var.get() or not size_var.get() or not milk_var.get() or not sweetener_var.get():
        messagebox.showerror(
            "Input Error", "Please make a selection for all options.")
        return

    clear_screen(order_window)
    order_window.geometry("400x600")

    summary = f"Coffee: {coffee_var.get()}\nSize: {size_var.get()}\nMilk: {milk_var.get()}\nSweetener: {sweetener_var.get()}"
    tk.Label(order_window, text="Order Summary",
             font=("Arial", 16)).pack(pady=10)
    tk.Label(order_window, text=summary, font=("Arial", 12)).pack(pady=10)

    tk.Button(order_window, text="Place Order",
              command=place_order).pack(pady=10)
    tk.Button(order_window, text="Back",
              command=order_window.destroy).pack(pady=5)


def place_order():
    messagebox.showinfo("Order Placed", "Thank you for your order!")
    order_window.destroy()


def exit_app():
    if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
        root.destroy()


def clear_screen(window):
    for widget in window.winfo_children():
        widget.destroy()


# --- Main Program ---
root = tk.Tk()
root.title("Drip n' Sip Coffee Ordering System")
root.geometry("300x200")

# Start App
welcome_screen()
root.mainloop()
