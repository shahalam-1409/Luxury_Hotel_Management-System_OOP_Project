import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from db_connection import connect_to_db

class ServiceManagement:
    def __init__(self, root):
        self.window = tk.Toplevel(root)
        self.window.title("Manage Services")
        self.window.geometry("800x600")
        self.window.configure(bg="#333333")  # Dark background for consistency

        # Title label
        title_label = ttk.Label(
            self.window,
            text="Manage Services",
            font=("Georgia", 24, "bold"),
            foreground="#FFD700",  # Gold color for luxury
            background="#333333"  # Dark background for consistency
        )
        title_label.pack(pady=20)

        # Create a frame for the input fields
        input_frame = ttk.Frame(self.window, padding="20 20 20 20", style="Dark.TFrame")
        input_frame.pack(pady=20, padx=20, fill="x", expand=True)

        # Service details labels and entry fields
        ttk.Label(input_frame, text="Booking ID:", font=("Arial", 12, "bold"), foreground="#FFFFFF").grid(row=0, column=0, sticky="w", pady=5)
        self.booking_id_entry = ttk.Entry(input_frame, font=("Arial", 14), style="Custom.TEntry", width=40)
        self.booking_id_entry.grid(row=0, column=1, pady=5, padx=10)

        ttk.Label(input_frame, text="Service Description:", font=("Arial", 12, "bold"), foreground="#FFFFFF").grid(row=1, column=0, sticky="w", pady=5)
        self.description_entry = ttk.Entry(input_frame, font=("Arial", 14), style="Custom.TEntry", width=40)
        self.description_entry.grid(row=1, column=1, pady=5, padx=10)

        ttk.Label(input_frame, text="Service Cost ($):", font=("Arial", 12, "bold"), foreground="#FFFFFF").grid(row=2, column=0, sticky="w", pady=5)
        self.cost_entry = ttk.Entry(input_frame, font=("Arial", 14), style="Custom.TEntry", width=40)
        self.cost_entry.grid(row=2, column=1, pady=5, padx=10)

        # Add a frame for buttons
        button_frame = ttk.Frame(self.window, padding="10 10 10 10", style="Dark.TFrame")
        button_frame.pack(pady=20)

        # Add Service button
        add_button = ttk.Button(
            button_frame,
            text="Add Service",
            command=self.add_service,
            style="Luxury.TButton"
        )
        add_button.grid(row=0, column=0)

        # Style Configuration
        style = ttk.Style()
        
        # Button Style (gold accent on hover)
        style.configure("Luxury.TButton",
                        font=("Arial", 12, "bold"),
                        padding=10,
                        borderwidth=1)
        style.map("Luxury.TButton", background=[("active", "#E6B800")])  # Darker color on hover

        # Frame Style (Dark background to match window)
        style.configure("Dark.TFrame", background="#333333") 

        # Entry Style (Grey background for text fields with white text)
        style.configure("Custom.TEntry",
                        fieldbackground="#666666",  # Darker background for entry fields
                        foreground="#FFFFFF",  # White text for readability                     # Set grey background
                                                   # White text color for contrast
                        borderwidth=1)  # Simple border for inputs

    def add_service(self):
        """Add a new service to the database."""
        booking_id = self.booking_id_entry.get()
        description = self.description_entry.get()
        cost = self.cost_entry.get()

        if not booking_id or not description or not cost:
            messagebox.showerror("Error", "All fields are required!")
            return
        
        try:
            cost = float(cost)
        except ValueError:
            messagebox.showerror("Error", "Service cost must be a valid number!")
            return

        conn = connect_to_db()
        cursor = conn.cursor()
        try:
            query = "INSERT INTO Services (BookingID, ServiceDescription, ServiceCost) VALUES (%s, %s, %s)"
            cursor.execute(query, (booking_id, description, cost))
            conn.commit()
            messagebox.showinfo("Success", "Service added successfully!")
            self.clear_entries()  # Clear input fields after adding the service
        except Exception as e:
            messagebox.showerror("Error", str(e))
        finally:
            cursor.close()
            conn.close()

    def clear_entries(self):
        """Clear all input fields."""
        self.booking_id_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)
        self.cost_entry.delete(0, tk.END)
