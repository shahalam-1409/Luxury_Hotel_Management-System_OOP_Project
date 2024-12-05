import tkinter as tk
from tkinter import ttk, messagebox
from db_connection import connect_to_db

class GuestManagement:
    def __init__(self, root):
        # Create a top-level window for Guest Management
        self.window = tk.Toplevel(root)
        self.window.title("Manage Guests")
        self.window.geometry("800x600")
        self.window.configure(bg="#333333")  # Dark background for consistency

        # Add a title label
        title_label = ttk.Label(
            self.window,
            text="Manage Guests",
            font=("Georgia", 24, "bold"),
            foreground="#FFD700",  # Gold color for a luxurious touch
            background="#333333",
        )
        title_label.pack(pady=20)  # Add spacing around the title

        # Create a frame to hold input fields
        input_frame = ttk.Frame(self.window, padding="20 20 20 20", style="Dark.TFrame")
        input_frame.pack(pady=10, padx=20, fill="x", expand=True)

        # Guest fields with bold labels
        ttk.Label(input_frame, text="Name:", font=("Arial", 12, "bold"), foreground="#FFFFFF").grid(row=0, column=0, sticky="w", pady=5)
        self.name_entry = ttk.Entry(input_frame, font=("Arial", 12), style="Custom.TEntry")
        self.name_entry.grid(row=0, column=1, pady=5, padx=10)

        ttk.Label(input_frame, text="Phone:", font=("Arial", 12, "bold"), foreground="#FFFFFF").grid(row=1, column=0, sticky="w", pady=5)
        self.phone_entry = ttk.Entry(input_frame, font=("Arial", 12), style="Custom.TEntry")
        self.phone_entry.grid(row=1, column=1, pady=5, padx=10)

        ttk.Label(input_frame, text="Email:", font=("Arial", 12, "bold"), foreground="#FFFFFF").grid(row=2, column=0, sticky="w", pady=5)
        self.email_entry = ttk.Entry(input_frame, font=("Arial", 12), style="Custom.TEntry")
        self.email_entry.grid(row=2, column=1, pady=5, padx=10)

        ttk.Label(input_frame, text="Address:", font=("Arial", 12, "bold"), foreground="#FFFFFF").grid(row=3, column=0, sticky="w", pady=5)
        self.address_entry = ttk.Entry(input_frame, font=("Arial", 12), style="Custom.TEntry")
        self.address_entry.grid(row=3, column=1, pady=5, padx=10)

        # Add a frame for buttons
        button_frame = ttk.Frame(self.window, padding="10 10 10 10", style="Dark.TFrame")
        button_frame.pack(pady=20)

        # Buttons with matching color scheme
        add_button = ttk.Button(
            button_frame,
            text="Add Guest",
            command=self.add_guest,
            style="Luxury.TButton"
        )
        add_button.grid(row=0, column=0, padx=10)

        # Style Configuration
        style = ttk.Style()
        # Button Style
        style.configure("Luxury.TButton",
                        font=("Arial", 12, "bold"),
                        padding=10,
                        foreground="#000000",  # Black text
                        background="#FFD700",  # Gold background
                        borderwidth=1)
        style.map("Luxury.TButton", background=[("active", "#E6B800")])  # Slightly darker gold on hover

        # Frame Style
        style.configure("Dark.TFrame", background="#333333")  # Match frame background

        # Entry Style
        style.configure("Custom.TEntry",
                        fieldbackground="#666666",  # Darker background for entry fields
                        foreground="#FFFFFF",  # White text for readability
                        borderwidth=1)

    def add_guest(self):
        """Add guest to the database."""
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        conn = connect_to_db()
        cursor = conn.cursor()
        try:
            # Insert guest details into the database
            query = "INSERT INTO Guests (Name, PhoneNumber, Email, Address) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (name, phone, email, address))
            conn.commit()
            messagebox.showinfo("Success", "Guest added successfully!")
            self.clear_entries()  # Clear fields after adding a guest
        except Exception as e:
            messagebox.showerror("Error", str(e))
        finally:
            cursor.close()
            conn.close()

    def clear_entries(self):
        """Clear all input fields."""
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
