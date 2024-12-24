import tkinter as tk
from tkinter import messagebox

from gui.admin_gui import AdminGUI
from gui.doctor_gui import DoctorGUI
from gui.patient_gui import PatientGUI
from src.controller.controller import Controller
from tkcalendar import Calendar, DateEntry

class GUI:
    def __init__(self, root):
        self.controller = Controller()
        self.current_user_id = None
        self.current_username = None
        self.current_user_role = None
        self.root = root
        self.root.title("Medical Center")

        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(padx=20, pady=20)

        self.setup_login_screen()

    def setup_login_screen(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        tk.Label(self.main_frame, text="Welcome to the Medical Center!", font=("Arial", 16)).pack(pady=10)
        tk.Button(self.main_frame, text="Register", command=self.registration).pack(pady=5)
        tk.Button(self.main_frame, text="Login", command=self.login).pack(pady=5)

    def registration(self):
        self.clear_screen()
        tk.Label(self.main_frame, text="Registration", font=("Arial", 14)).pack(pady=10)

        tk.Label(self.main_frame, text="Username:").pack()
        username_entry = tk.Entry(self.main_frame)
        username_entry.pack()

        tk.Label(self.main_frame, text="Password:").pack()
        password_entry = tk.Entry(self.main_frame, show="*")
        password_entry.pack()

        tk.Label(self.main_frame, text="Role (2 - Patient, 3 - Doctor):").pack()
        role_entry = tk.Entry(self.main_frame)
        role_entry.pack()

        def submit_registration():
            username = username_entry.get()
            password = password_entry.get()
            role_id = role_entry.get()

            if not username or not password or role_id not in ["2", "3"]:
                messagebox.showerror("Error", "Invalid input")
                return

            if username in self.controller.get_usernames():
                messagebox.showerror("Error", "This username exists!")
                return

            role_id = int(role_id)
            self.controller.create_user(username, password, role_id)
            user_id = self.controller.get_user_by_username(username)[0]

            if role_id == 2:
                self.create_patient(user_id)
            elif role_id == 3:
                self.create_doctor(user_id)

        tk.Button(self.main_frame, text="Submit", command=submit_registration).pack(pady=10)
        tk.Button(self.main_frame, text="Back", command=self.setup_login_screen).pack()

    def create_patient(self, user_id):
        self.clear_screen()
        tk.Label(self.main_frame, text="Create Patient", font=("Arial", 14)).pack(pady=10)

        tk.Label(self.main_frame, text="First Name:").pack()
        first_name_entry = tk.Entry(self.main_frame)
        first_name_entry.pack()

        tk.Label(self.main_frame, text="Last Name:").pack()
        last_name_entry = tk.Entry(self.main_frame)
        last_name_entry.pack()

        tk.Label(self.main_frame, text="Date of Birth (yyyy-mm-dd):").pack()
        dob_entry = DateEntry(self.main_frame, width=12, background='darkblue',
                  foreground='white', borderwidth=2, year=2000)
        dob_entry.pack(padx=10, pady=10)

        tk.Label(self.main_frame, text="Gender (1 - Male, 2 - Female, 3 - Other):").pack()
        gender_entry = tk.Entry(self.main_frame)
        gender_entry.pack()

        tk.Label(self.main_frame, text="Phone Number (+375xxxxxxxxxx):").pack()
        phone_entry = tk.Entry(self.main_frame)
        phone_entry.pack()

        tk.Label(self.main_frame, text="Email:").pack()
        email_entry = tk.Entry(self.main_frame)
        email_entry.pack()

        def submit_patient():
            first_name = first_name_entry.get()
            last_name = last_name_entry.get()
            dob = dob_entry.get()
            gender = gender_entry.get()
            phone = phone_entry.get()
            email = email_entry.get()

            if not first_name or not last_name or not dob or not phone or not email:
                messagebox.showerror("Error", "All fields are required")
                return

            if gender == "1":
                gender = "Male"
            elif gender == "2":
                gender = "Female"
            elif gender == "3":
                gender = "Other"
            else:
                messagebox.showerror("Error", "Invalid gender")
                return

            self.controller.create_patient(user_id, first_name, last_name, dob, gender, phone, email)
            user_info = self.controller.get_item_by_id(user_id, 'user_acc')[0]
            self.update_current_user(user_info[0], user_info[1], user_info[3])
            self.setup_login_screen()

        tk.Button(self.main_frame, text="Submit", command=submit_patient).pack(pady=10)
        tk.Button(self.main_frame, text="Back", command=self.registration).pack()

    def create_doctor(self, user_id):
        self.clear_screen()
        tk.Label(self.main_frame, text="Create Doctor", font=("Arial", 14)).pack(pady=10)

        tk.Label(self.main_frame, text="First Name:").pack()
        first_name_entry = tk.Entry(self.main_frame)
        first_name_entry.pack()

        tk.Label(self.main_frame, text="Last Name:").pack()
        last_name_entry = tk.Entry(self.main_frame)
        last_name_entry.pack()

        tk.Label(self.main_frame, text="Gender (1 - Male, 2 - Female, 3 - Other):").pack()
        gender_entry = tk.Entry(self.main_frame)
        gender_entry.pack()

        def submit_doctor():
            first_name = first_name_entry.get()
            last_name = last_name_entry.get()
            gender = gender_entry.get()

            if not first_name or not last_name:
                messagebox.showerror("Error", "All fields are required")
                return

            if gender == "1":
                gender = "Male"
            elif gender == "2":
                gender = "Female"
            elif gender == "3":
                gender = "Other"
            else:
                messagebox.showerror("Error", "Invalid gender")
                return

            self.controller.create_doctor_min(user_id, first_name, last_name, gender)
            user_info = self.controller.get_item_by_id(user_id, 'user_acc')[0]
            self.update_current_user(user_info[0], user_info[1], user_info[3])
            self.setup_login_screen()

        tk.Button(self.main_frame, text="Submit", command=submit_doctor).pack(pady=10)
        tk.Button(self.main_frame, text="Back", command=self.registration).pack()

    def login(self):
        self.clear_screen()
        tk.Label(self.main_frame, text="Login", font=("Arial", 14)).pack(pady=10)

        tk.Label(self.main_frame, text="Username:").pack()
        username_entry = tk.Entry(self.main_frame)
        username_entry.pack()

        tk.Label(self.main_frame, text="Password:").pack()
        password_entry = tk.Entry(self.main_frame, show="*")
        password_entry.pack()

        def submit_login():
            username = username_entry.get()
            password = password_entry.get()

            if username not in self.controller.get_usernames():
                messagebox.showerror("Error", "This user doesn't exist!")
                return

            user_info = self.controller.get_item_by_id(self.controller.get_user_by_username(username)[0], 'user_acc')[0]
            if password != user_info[2]:
                messagebox.showerror("Error", "Incorrect password!")
                return

            self.update_current_user(user_info[0], user_info[1], user_info[3])

            if self.current_user_role == 1:
                print("admin")
                AdminGUI(self.controller)
            elif self.current_user_role == 2:
                pat_id = self.controller.get_patient_by_user_id(self.current_user_id)
                print("patient", pat_id)
                PatientGUI(self.controller, pat_id)
            elif self.current_user_role == 3:
                doc_id = self.controller.get_doctor_by_user_id(self.current_user_id)
                print("doctor", doc_id)
                DoctorGUI(self.controller, doc_id)

        tk.Button(self.main_frame, text="Submit", command=submit_login).pack(pady=10)
        tk.Button(self.main_frame, text="Back", command=self.setup_login_screen).pack()

    def update_current_user(self, user_id=None, username=None, role=None):
        self.current_user_id = user_id
        self.current_username = username
        self.current_user_role = role
        if user_id:
            messagebox.showinfo("Welcome", f"Hello, {username}!")

    def clear_screen(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()
