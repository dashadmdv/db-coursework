INSERT INTO role (role_name)
VALUES ('admin'),
       ('patient'),
       ('doctor');

INSERT INTO user_acc (username, password, role_id)
VALUES ('admin', 'admin', 1),
       ('dashadmdv', '12345678', 1),
       ('patient', 'patient', 2),
       ('doctor', 'doctor', 3),
       ('amattiazzow', 'dX3{GLa,F', 3),
       ('ldriverx', 'kP5~<jv(f3', 2),
       ('cbrowsey', 'fH9}YoOO$', 3),
       ('gmunneryz', 'qK9'')6I=.n@s', 2),
       ('hmacia10', 'fB4,Od22/}', 3),
       ('btschierse11', 'tQ9<%qU~I)', 2),
       ('mflewitt12', 'aG8(Xf{6Uaz', 2),
       ('cgurton13', 'eM3)gzm#<R''EO#5', 3),
       ('aiacovides14', 'mS4?KAf>GB_"', 2);

INSERT INTO patient (user_id, first_name, last_name, date_of_birth, gender, phone_number, email)
VALUES (3, 'Ivan', 'Ivanov', '1970-01-01', 'Male', '+375291111111', 'aboba@gmail.com'),
       (6, 'Anna', 'Annova', '1980-01-01', 'Female', '+375292222222', 'aboba1@gmail.com'),
       (8, 'Petr', 'Petrov', '1990-01-01', 'Male', '+375293333333', 'aboba2@gmail.com'),
       (10, 'Anastasia', 'Anastasieva', '2000-01-01', 'Female', '+375294444444', 'aboba3@gmail.com'),
       (11, 'Oleg', 'Olegov', '2010-01-01', 'Male', '+375295555555', 'aboba4@gmail.com'),
       (13, 'Olga', 'Olgova', '2020-01-01', 'Female', '+375296666666', 'aboba5@gmail.com');

INSERT INTO doctor_category (category_name)
VALUES ('Pediatrician'),
       ('Cardiologist'),
       ('Endocrinologist'),
       ('Ophthalmologist'),
       ('Dermatologist'),
       ('Psychiatrist'),
       ('Neurologist'),
       ('Gynecologist');

INSERT INTO doctor_specialization (specialization_name, category_id)
VALUES ('Cardiologist', 1),
       ('Endocrinologist', 1),
       ('Electrophysiologist', 2),
       ('Cardiac rehabilitation specialist', 2),
       ('Heart failure specialist', 2),
       ('Heart surgeon', 2);

INSERT INTO department (department_name)
VALUES ('Children Center'),
       ('Cardiovascular Surgery'),
       ('Pediatric Surgery');

INSERT INTO doctor (user_id, first_name, last_name, gender, specialization_id, department_id)
VALUES (4, 'Ivan', 'Ivanov', 'Male', 1, 3),
       (5, 'Anna', 'Annova', 'Female', 2, 1),
       (7, 'Petr', 'Petrov', 'Male', 3, 2),
       (9, 'Anastasia', 'Anastasieva', 'Female', 4, 2),
       (12, 'Oleg', 'Olegov', 'Male', 5, 2);

INSERT INTO schedule_slot (date_of_slot, time_of_slot, doctor_id)
VALUES ('2024-12-11', '16:00:00', 5), ('2024-12-12', '16:00:00', 1),
       ('2024-12-13', '16:00:00', 4), ('2024-12-14', '16:00:00', 2),
       ('2024-12-15', '16:00:00', 3), ('2024-12-16', '16:00:00', 3),
       ('2024-12-17', '16:00:00', 2), ('2024-12-18', '16:00:00', 4),
       ('2024-12-19', '16:00:00', 1), ('2024-12-20', '16:00:00', 5);

INSERT INTO service (service_name, price, doctor_id)
VALUES ('Consultation', 200.00, 1), ('Consultation', 200.00, 2),
       ('Consultation', 200.00, 3), ('Consultation', 200.00, 4),
       ('Consultation', 200.00, 5);

INSERT INTO appointment (slot_id, patient_id)
VALUES (2, 3), (4, 2), (1, 1), (3, 5), (5, 6),
       (6, 4), (7, 5), (8, 1), (9, 3), (10, 4);

INSERT INTO appointment_service (appointment_id, service_id)
VALUES (1, 1), (2, 2), (3, 3), (4, 4), (5, 5),
       (6, 1), (7, 2), (8, 3), (9, 4), (10, 5);

INSERT INTO diagnosis (diagnosis_name, diagnosis_code)
VALUES ('COVID-19', 'U071'), ('Chest pain, unspecified', 'R079'),
       ('Contact with and (suspected) exposure to COVID-19', 'Z20822'),
       ('Vitamin D deficiency, unspecified', 'E55.9'), ('Cough', 'R05');

INSERT INTO prescription (note, appointment_id)
VALUES ('Rest until 23.12. Ibuprofen twice a day', 2),
       ('Rest until 30.12. Vitamin D twice a day', 7),
       ('Hospitalization until 10.12', 10);

INSERT INTO patient_diagnosis (patient_id, diagnosis_id)
VALUES (4, 5), (2, 3), (1, 1), (1, 2), (1, 3), (6, 4);