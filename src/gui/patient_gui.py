import tkinter as tk
from tkinter import ttk, messagebox


class PatientGUI:
    def __init__(self, controller, pat_id):
        self.controller = controller
        self.patient_id = pat_id
        self.root = tk.Tk()
        self.root.title("Patient Panel")
        self.main_frame = self.root
        self.create_main_menu()

    def create_main_menu(self):
        self.clear_frame()

        tk.Label(self.main_frame, text="Patient Panel", font=("Arial", 16)).pack(pady=10)

        tk.Button(self.main_frame, text="See My Appointments", command=self.view_appointments, width=25).pack(pady=5)
        tk.Button(self.main_frame, text="Get Appointment", command=self.get_appointment, width=25).pack(pady=5)
        tk.Button(self.main_frame, text="My Diagnoses", command=self.view_diagnoses, width=25).pack(pady=5)
        tk.Button(self.main_frame, text="My Prescriptions", command=self.view_prescriptions, width=25).pack(pady=5)
        tk.Button(self.main_frame, text="Exit", command=self.root.quit, width=25).pack(pady=20)

    def view_appointments(self):
        self.clear_frame()

        tk.Label(self.main_frame, text="My Appointments", font=("Arial", 14)).pack(pady=10)

        columns = ["appointment_id", "service", "patient", "doctor", "date", "time", "price"]
        tree = ttk.Treeview(self.main_frame, columns=columns, show="headings")
        for col in columns:
            tree.heading(col, text=col.capitalize())

        appointments = self.controller.get_patient_appointments(self.patient_id)
        for app_id in appointments:
            info = self.controller.get_doctor_app_info(app_id)
            tree.insert("", tk.END, values=info)

        tree.pack(fill=tk.BOTH, expand=True, pady=10)
        tk.Button(self.main_frame, text="Back", command=self.create_main_menu, width=20).pack(pady=5)

    def get_appointment(self):
        self.clear_frame()

        tk.Label(self.main_frame, text="Get Appointment", font=("Arial", 14)).pack(pady=10)

        slots = self.controller.get_app_slots()
        columns = ["id", "date", "time", "doctor"]
        tree = ttk.Treeview(self.main_frame, columns=columns, show="headings")
        for col in columns:
            tree.heading(col, text=col.capitalize())
        for slot in slots:
            tree.insert("", tk.END, values=slot)

        tree.pack(fill=tk.BOTH, expand=True, pady=10)

        self.slot_var = tk.StringVar()
        tk.Label(self.main_frame, text="Select Slot ID:").pack(pady=5)
        tk.Entry(self.main_frame, textvariable=self.slot_var).pack(pady=5)

        tk.Button(self.main_frame, text="Next", command=self.select_service, width=20).pack(pady=5)
        tk.Button(self.main_frame, text="Back", command=self.create_main_menu, width=20).pack(pady=5)

    def select_service(self):
        slot_id = self.slot_var.get()
        if not slot_id.isdigit():
            messagebox.showerror("Error", "Please enter a valid Slot ID.")
            return

        slot_id = int(slot_id)
        services = self.controller.get_doctor_services(self.controller.get_doctor_from_slot(slot_id))
        self.clear_frame()

        tk.Label(self.main_frame, text="Select Service", font=("Arial", 14)).pack(pady=10)

        columns = ["Service ID", "Service Name", "Price"]
        tree = ttk.Treeview(self.main_frame, columns=columns, show="headings")
        for col in columns:
            tree.heading(col, text=col.capitalize())
        for service in services:
            tree.insert("", tk.END, values=service)

        tree.pack(fill=tk.BOTH, expand=True, pady=10)

        self.service_var = tk.StringVar()
        tk.Label(self.main_frame, text="Select Service ID:").pack(pady=5)
        tk.Entry(self.main_frame, textvariable=self.service_var).pack(pady=5)

        tk.Button(self.main_frame, text="Confirm", command=lambda: self.confirm_appointment(slot_id), width=20).pack(pady=5)
        tk.Button(self.main_frame, text="Back", command=self.get_appointment, width=20).pack(pady=5)

    def confirm_appointment(self, slot_id):
        service_id = self.service_var.get()
        if not service_id.isdigit():
            messagebox.showerror("Error", "Please enter a valid Service ID.")
            return

        service_id = int(service_id)
        result1 = self.controller.create_appointment(slot_id, self.patient_id)
        app_id = self.controller.get_app_from_slot(slot_id)
        result2 = self.controller.create_appointment_service(app_id, service_id)

        messagebox.showinfo("Success", f"Appointment Created:\n{result1}\n{result2}")
        self.create_main_menu()

    def view_diagnoses(self):
        self.clear_frame()

        tk.Label(self.main_frame, text="My Diagnoses", font=("Arial", 14)).pack(pady=10)

        columns = ["Date of Diagnosis", "Diagnosis Name", "Diagnosis Code"]
        tree = ttk.Treeview(self.main_frame, columns=columns, show="headings")
        for col in columns:
            tree.heading(col, text=col.capitalize())

        diagnoses = self.controller.get_patient_diagnoses(self.patient_id)
        for diagnosis in diagnoses:
            tree.insert("", tk.END, values=diagnosis)

        tree.pack(fill=tk.BOTH, expand=True, pady=10)
        tk.Button(self.main_frame, text="Back", command=self.create_main_menu, width=20).pack(pady=5)

    def view_prescriptions(self):
        self.clear_frame()

        tk.Label(self.main_frame, text="My Prescriptions", font=("Arial", 14)).pack(pady=10)

        columns = ["Prescription", "Date", "Doctor"]
        tree = ttk.Treeview(self.main_frame, columns=columns, show="headings")
        for col in columns:
            tree.heading(col, text=col.capitalize())

        prescriptions = self.controller.get_patient_prescription(self.patient_id)
        for prescription in prescriptions:
            tree.insert("", tk.END, values=prescription)

        tree.pack(fill=tk.BOTH, expand=True, pady=10)
        tk.Button(self.main_frame, text="Back", command=self.create_main_menu, width=20).pack(pady=5)

    def clear_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()
