import tkinter as tk
from tkinter import messagebox, simpledialog

class AdminGUI:
    def __init__(self, controller):
        self.controller = controller
        self.tables = ['role', 'user_acc', 'user_activity', 'patient', 'doctor_category', 'doctor_specialization',
                       'department', 'doctor', 'schedule_slot', 'service', 'appointment', 'appointment_service',
                       'diagnosis', 'prescription', 'patient_diagnosis']
        self.fields = [["Role name"], ["Username", "Password", "Role id"], ["User id", "Activity", "Date", "Time"],
                       ["User id", "First name", "Last name", "Date of birth", "Gender", "Phone", "Email"],
                       ["Category name"], ["Specialization name", "Category id"], ["Department name"],
                       ["User id", "First name", "Last name", "Gender", "Specialization id", "Department id"],
                       ["Date", "Time", "Doctor id"], ["Service name", "Price", "Doctor id"], ["Slot id", "Patient_id"],
                       ["Appointment id", "Service id"], ["Diagnosis name", "Diagnosis code"],
                       ["Note", "Appointment id"], ["Patient id", "Diagnosis id"]]

        self.root = tk.Tk()
        self.root.title("Admin Panel")
        self.create_main_menu()

    def create_main_menu(self):
        frame = tk.Frame(self.root)
        frame.pack(padx=10, pady=10)

        tk.Label(frame, text="Select a table to work with:").pack()

        for i, table in enumerate(self.tables):
            tk.Button(frame, text=table, command=lambda t=table: self.table_menu(t)).pack(fill="x")

        tk.Button(frame, text="Exit", command=self.root.quit).pack(fill="x")

    def table_menu(self, table):
        def back():
            frame.destroy()
            # self.create_main_menu()

        frame = tk.Tk()
        # frame.pack(padx=10, pady=10)

        tk.Label(frame, text=f"Selected Table: {table}").pack()

        tk.Button(frame, text="Show Table", command=lambda: self.show_table(table)).pack(fill="x")
        tk.Button(frame, text="Add Item", command=lambda: self.create_item(table)).pack(fill="x")
        tk.Button(frame, text="Show Item (by ID)", command=lambda: self.show_item(table)).pack(fill="x")
        tk.Button(frame, text="Update Item (by ID)", command=lambda: self.update_item(table)).pack(fill="x")
        tk.Button(frame, text="Delete Item (by ID)", command=lambda: self.delete_item(table)).pack(fill="x")
        tk.Button(frame, text="Back", command=back).pack(fill="x")

    def show_table(self, table):
        data = self.controller.get_table(table)
        if not data:
            messagebox.showinfo("Info", f"No data available for table {table}.")
            return

        table_window = tk.Toplevel(self.root)
        table_window.title(f"Table: {table}")

        for i, row in enumerate(data):
            tk.Label(table_window, text=row).grid(row=i, column=0, sticky="w")

    def create_item(self, table):
        fields = self.fields[self.tables.index(table)]
        inputs = {}

        def save():
            data = {'_'.join(field.lower().split(' ')): entry.get() for field, entry in inputs.items() if entry.get()}
            result = getattr(self.controller, f"create_{table}")(*data.values())
            messagebox.showinfo("Result", result)
            item_window.destroy()

        item_window = tk.Toplevel(self.root)
        item_window.title(f"Create Item: {table}")

        for field in fields:
            tk.Label(item_window, text=field).pack()
            inputs[field] = tk.Entry(item_window)
            inputs[field].pack()

        tk.Button(item_window, text="Save", command=save).pack()

    def show_item(self, table):
        item_id = simpledialog.askinteger("Input", f"Enter ID for {table}:")
        if item_id is None:
            return

        item = self.controller.get_item_by_id(item_id, table)
        if not item:
            messagebox.showinfo("Info", f"No item found with ID {item_id}.")
            return

        item_window = tk.Toplevel(self.root)
        item_window.title(f"Item ID: {item_id}")

        for key, value in zip(["id"] + self.fields[self.tables.index(table)], item):
            tk.Label(item_window, text=f"{key}: {value}").pack()

    def update_item(self, table):
        item_id = simpledialog.askinteger("Input", f"Enter ID to update in {table}:")
        if item_id is None:
            return

        fields = self.fields[self.tables.index(table)]
        inputs = {}

        def save():
            data = {'_'.join(field.lower().split(' ')): entry.get() for field, entry in inputs.items() if entry.get()}
            result = getattr(self.controller, f"update_{table}")(item_id, **data)
            messagebox.showinfo("Result", result)
            item_window.destroy()

        item_window = tk.Toplevel(self.root)
        item_window.title(f"Update Item: {table}")

        for field in fields:
            tk.Label(item_window, text=field).pack()
            inputs[field] = tk.Entry(item_window)
            inputs[field].pack()

        tk.Button(item_window, text="Save", command=save).pack()

    def delete_item(self, table):
        item_id = simpledialog.askinteger("Input", f"Enter ID to delete in {table}:")
        if item_id is None:
            return

        result = self.controller.delete_by_id(item_id, table)
        messagebox.showinfo("Result", result)

    def run(self):
        self.root.mainloop()
