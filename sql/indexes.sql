CREATE INDEX idx_role_id ON role (id);
CLUSTER role USING idx_role_id;

CREATE INDEX idx_user_acc_id ON user_acc (id);
CREATE INDEX idx_user_acc_username ON user_acc (username);
CLUSTER user_acc USING idx_user_acc_id;

CREATE INDEX idx_user_activity_id ON user_activity (id);
CREATE INDEX idx_user_activity_user_id ON user_activity (user_id);
CLUSTER user_activity USING idx_user_activity_id;

CREATE INDEX idx_patient_id ON patient (id);
CREATE INDEX idx_patient_email ON patient (email);
CLUSTER patient USING idx_patient_id;

CREATE INDEX idx_doctor_id ON doctor (id);
CLUSTER doctor USING idx_doctor_id;

CREATE INDEX idx_schedule_slot_doctor_id ON schedule_slot (doctor_id);

CREATE INDEX idx_service_id ON service (id);
CLUSTER service USING idx_service_id;

CREATE INDEX idx_appointment_id ON appointment (id);
CLUSTER appointment USING idx_appointment_id;
