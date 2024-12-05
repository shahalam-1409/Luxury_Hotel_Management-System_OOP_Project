import tkinter as tk
from tkinter import ttk, messagebox
from db_connection import connect_to_db

class FeedbackManagement:
    def __init__(self, root):
        # Create a top-level window for Feedback Management
        self.window = tk.Toplevel(root)
        self.window.title("Manage Feedback")
        self.window.geometry("800x600")
        self.window.configure(bg="#333333")  # Dark background for a luxurious feel

        # Add a title label
        title_label = ttk.Label(
            self.window,
            text="Manage Feedback",
            font=("Georgia", 24, "bold"),
            foreground="#FFD700",  # Gold color
            background="#333333",  # Match background
        )
        title_label.pack(pady=20)  # Add spacing around the title

        # Create a frame to hold input fields
        input_frame = ttk.Frame(self.window, padding="20 20 20 20", style="Dark.TFrame")
        input_frame.pack(pady=10, padx=20, fill="x", expand=True)

        # Feedback fields with bold labels
        ttk.Label(input_frame, text="Guest ID:", font=("Arial", 12, "bold"), foreground="#FFFFFF").grid(row=0, column=0, sticky="w", pady=5)
        self.guest_id_entry = ttk.Entry(input_frame, font=("Arial", 14), width=40, style="Custom.TEntry")  # Larger text field and white text
        self.guest_id_entry.grid(row=0, column=1, pady=5, padx=10)

        ttk.Label(input_frame, text="Feedback Text:", font=("Arial", 12, "bold"), foreground="#FFFFFF").grid(row=1, column=0, sticky="w", pady=5)
        self.feedback_entry = ttk.Entry(input_frame, font=("Arial", 14), width=40, style="Custom.TEntry")  # Larger text field and white text
        self.feedback_entry.grid(row=1, column=1, pady=5, padx=10)

        ttk.Label(input_frame, text="Rating (1-5):", font=("Arial", 12, "bold"), foreground="#FFFFFF").grid(row=2, column=0, sticky="w", pady=5)
        self.rating_entry = ttk.Entry(input_frame, font=("Arial", 14), width=40, style="Custom.TEntry")  # Larger text field and white text
        self.rating_entry.grid(row=2, column=1, pady=5, padx=10)

        # Add a frame for buttons
        button_frame = ttk.Frame(self.window, padding="10 10 10 10", style="Dark.TFrame")
        button_frame.pack(pady=20)

        # Buttons with matching color scheme
        add_button = ttk.Button(
            button_frame,
            text="Add Feedback",
            command=self.add_feedback,
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

        # Entry Style (Ensuring white text and background)
        style.configure("Custom.TEntry",
                        fieldbackground="#666666",  # Darker background for entry fields
                        foreground="#FFFFFF",  # White text for readability
                        borderwidth=1)

    def add_feedback(self):
        """Add feedback to the database."""
        guest_id = self.guest_id_entry.get()
        feedback = self.feedback_entry.get()
        rating = self.rating_entry.get()

        conn = connect_to_db()
        cursor = conn.cursor()
        try:
            # Ensure rating is a valid integer between 1 and 5
            if not rating.isdigit() or not (1 <= int(rating) <= 5):
                messagebox.showerror("Error", "Rating must be a number between 1 and 5!")
                return

            query = "INSERT INTO Feedback (GuestID, FeedbackText, Rating) VALUES (%s, %s, %s)"
            cursor.execute(query, (guest_id, feedback, int(rating)))
            conn.commit()
            messagebox.showinfo("Success", "Feedback added successfully!")
            self.clear_entries()  # Clear fields after adding feedback
        except Exception as e:
            messagebox.showerror("Error", str(e))
        finally:
            cursor.close()
            conn.close()

    def clear_entries(self):
        """Clear all input fields."""
        self.guest_id_entry.delete(0, tk.END)
        self.feedback_entry.delete(0, tk.END)
        self.rating_entry.delete(0, tk.END)
