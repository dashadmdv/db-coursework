import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class DoctorGUI:
    def __init__(self, controller, doc_id):
        self.root = tk.Tk()
        self.controller = controller
        self.doctor_id = doc_id
        self.current_appointment = None
        self.current_patient = None

        self.root.title("Doctor Panel")

        self.main_frame = self.root
        # self.main_frame.pack(fill=tk.BOTH, expand=True)

        self.create_main_menu()

    def create_main_menu(self):
        self.clear_frame()

        tk.Label(self.main_frame, text="Doctor Panel", font=("Arial", 16)).pack(pady=10)

        tk.Button(self.main_frame, text="See My Appointments", command=self.view_appointments, width=25).pack(pady=5)
        tk.Button(self.main_frame, text="Select Appointment", command=self.select_appointment, width=25).pack(pady=5)
        tk.Button(self.main_frame, text="Exit", command=self.root.quit, width=25).pack(pady=20)

    def view_appointments(self):
        self.clear_frame()

        tk.Label(self.main_frame, text="My Appointments", font=("Arial", 14)).pack(pady=10)

        columns = ["appointment_id", "service", "patient", "doctor", "date", "time"]
        tree = ttk.Treeview(self.main_frame, columns=columns, show="headings")

        for col in columns:
            tree.heading(col, text=col.capitalize())

        appointments = self.controller.get_doctor_appointments(self.doctor_id)
        print(appointments)
        for app_id in appointments:
            info = self.controller.get_doctor_app_info(app_id)
            print(info)
            tree.insert("", tk.END, values=info)

        tree.pack(fill=tk.BOTH, expand=True, pady=10)

        tk.Button(self.main_frame, text="Back", command=self.create_main_menu, width=20).pack(pady=5)

    def select_appointment(self):
        self.clear_frame()

        tk.Label(self.main_frame, text="Select Appointment", font=("Arial", 14)).pack(pady=10)

        appointments = self.controller.get_doctor_appointments(self.doctor_id)
        if not appointments:
            tk.Label(self.main_frame, text="No Appointments Available.").pack(pady=10)
            tk.Button(self.main_frame, text="Back", command=self.create_main_menu, width=20).pack(pady=5)
            return

        self.appointment_var = tk.StringVar()
        options = [str(app_id) for app_id in appointments]
        tk.OptionMenu(self.main_frame, self.appointment_var, *options).pack(pady=5)

        tk.Button(self.main_frame, text="Select", command=self.handle_appointment_selection, width=20).pack(pady=5)
        tk.Button(self.main_frame, text="Back", command=self.create_main_menu, width=20).pack(pady=5)

    def handle_appointment_selection(self):
        selected_id = self.appointment_var.get()
        if not selected_id:
            messagebox.showerror("Error", "Please select an appointment.")
            return

        self.current_appointment = int(selected_id)
        self.current_patient = self.controller.get_patient_by_app(self.current_appointment)
        self.appointment_dialogue()

    def appointment_dialogue(self):
        self.clear_frame()

        tk.Label(self.main_frame, text=f"Appointment #{self.current_appointment}", font=("Arial", 14)).pack(pady=10)

        tk.Button(self.main_frame, text="See Appointment Details", command=self.view_appointment_details, width=25).pack(pady=5)
        tk.Button(self.main_frame, text="Add Diagnosis", command=self.add_diagnosis, width=25).pack(pady=5)
        tk.Button(self.main_frame, text="Add Prescription", command=self.add_prescription, width=25).pack(pady=5)
        tk.Button(self.main_frame, text="End Appointment", command=self.end_appointment, width=25).pack(pady=20)

    def view_appointment_details(self):
        info = self.controller.get_doctor_app_info(self.current_appointment)
        details = "\n".join(f"{key}: {value}" for key, value in zip(
            ["Appointment ID", "Service", "Patient", "Doctor", "Date", "Time", "Price"], info
        ))
        messagebox.showinfo("Appointment Details", details)

    def add_diagnosis(self):
        self.clear_frame()

        tk.Label(self.main_frame, text="Add Diagnosis", font=("Arial", 14)).pack(pady=10)

        diagnoses = self.controller.get_table('diagnosis')
        columns = ["id", "name", "code"]
        tree = ttk.Treeview(self.main_frame, columns=columns, show="headings")

        for col in columns:
            tree.heading(col, text=col.capitalize())

        for diagnosis in diagnoses:
            tree.insert("", tk.END, values=diagnosis)

        tree.pack(fill=tk.BOTH, expand=True, pady=10)

        self.diagnosis_var = tk.StringVar()
        diagnosis_ids = self.controller.get_ids('diagnosis')
        options = [str(d_id) for d_id in diagnosis_ids]
        tk.OptionMenu(self.main_frame, self.diagnosis_var, *options).pack(pady=5)

        tk.Button(self.main_frame, text="Add", command=self.handle_add_diagnosis, width=20).pack(pady=5)
        tk.Button(self.main_frame, text="Back", command=self.appointment_dialogue, width=20).pack(pady=5)

    def handle_add_diagnosis(self):
        selected_id = self.diagnosis_var.get()
        if not selected_id:
            messagebox.showerror("Error", "Please select a diagnosis.")
            return

        result = self.controller.create_patient_diagnosis(self.current_patient, int(selected_id))
        messagebox.showinfo("Success", result)
        self.appointment_dialogue()

    def add_prescription(self):
        self.clear_frame()

        tk.Label(self.main_frame, text="Add Prescription", font=("Arial", 14)).pack(pady=10)

        tk.Label(self.main_frame, text="Note:").pack(pady=5)
        note_entry = tk.Entry(self.main_frame, width=40)
        note_entry.pack(pady=5)

        def save_prescription():
            note = note_entry.get()
            if not note:
                messagebox.showerror("Error", "Note cannot be empty.")
                return

            result = self.controller.create_prescription(note, self.current_appointment)
            messagebox.showinfo("Success", result)
            self.appointment_dialogue()

        tk.Button(self.main_frame, text="Add", command=save_prescription, width=20).pack(pady=5)
        tk.Button(self.main_frame, text="Back", command=self.appointment_dialogue, width=20).pack(pady=5)

    def end_appointment(self):
        self.current_appointment = None
        self.current_patient = None
        self.create_main_menu()

    def clear_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    from src.controller.controller import Controller

    controller = Controller()
    doctor_id = 1  # Example doctor ID

    root = tk.Tk()
    app = DoctorGUI(root, controller, doctor_id)
    root.mainloop()
