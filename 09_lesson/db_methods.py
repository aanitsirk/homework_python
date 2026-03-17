from sqlalchemy import create_engine
from db_queries import DB_Queries


class DB_Methods:
    def __init__(self, connection_string):
        self.engine = create_engine(connection_string)
        self.q = DB_Queries()

    def get_all_subjects(self):
        with self.engine.begin() as conn:
            result = conn.execute(self.q.subject["select_all"])
            return result.mappings().all()

    def get_subject(self, subject_id):
        with self.engine.begin() as conn:
            result = conn.execute(self.q.subject["select_by_id"],
                                  {"subject_id": subject_id})
            return result.mappings().first()

    def create_subject(self, subject_id, title):
        with self.engine.begin() as conn:
            conn.execute(
                self.q.subject["insert"],
                {"subject_id": subject_id, "title": title})

    def update_subject_title(self, subject_id, new_title):
        with self.engine.begin() as conn:
            conn.execute(
                self.q.subject["update"],
                {"subject_id": subject_id, "new_title": new_title})

    def delete_subject_by_subject_id(self, subject_id):
        with self.engine.begin() as conn:
            conn.execute(self.q.student["delete_by_subject_id"],
                         {"subject_id": subject_id})
            conn.execute(self.q.subject["delete"], {"subject_id": subject_id})

    def get_user(self, user_id):
        with self.engine.begin() as conn:
            result = conn.execute(self.q.users["select_by_id"],
                                  {"user_id": user_id})
            return result.mappings().first()

    def create_user(self, user_id, email, subject_id=None):
        with self.engine.begin() as conn:
            conn.execute(self.q.users["insert"],
                         {"user_id": user_id,
                          "email": email,
                          "subject_id": subject_id})

    def update_user_email(self, user_id, new_email):
        with self.engine.begin() as conn:
            conn.execute(self.q.users["update_email"],
                         {"user_id": user_id,
                          "user_email": new_email})

    def delete_user(self, user_id):
        with self.engine.begin() as conn:
            conn.execute(self.q.group_student["delete_by_user_id"],
                         {"user_id": user_id})
            conn.execute(self.q.student["delete_by_user_id"],
                         {"user_id": user_id})
            conn.execute(self.q.users["delete"], {"user_id": user_id})

    def get_student(self, user_id):
        with self.engine.begin() as conn:
            result = conn.execute(self.q.student["select_by_id"],
                                  {"user_id": user_id})
            return result.mappings().first()

    def create_student(self, user_id, level, education_form, subject_id):
        with self.engine.begin() as conn:
            conn.execute(
                self.q.student["insert"],
                {"user_id": user_id,
                 "level": level,
                 "education_form": education_form,
                 "subject_id": subject_id})

    def update_student_level(self, user_id, new_level):
        with self.engine.begin() as conn:
            conn.execute(self.q.student["update_level"],
                         {"user_id": user_id, "new_level": new_level})

    def delete_student(self, user_id):
        with self.engine.begin() as conn:
            conn.execute(self.q.group_student["delete_by_user_id"],
                         {"user_id": user_id})
            conn.execute(self.q.student["delete_by_user_id"],
                         {"user_id": user_id})

    def get_teacher(self, teacher_id):
        with self.engine.begin() as conn:
            result = conn.execute(self.q.teacher["select_by_id"],
                                  {"teacher_id": teacher_id})
        return result.mappings().first()

    def create_teacher(self, teacher_id, email, group_id):
        with self.engine.begin() as conn:
            conn.execute(self.q.teacher["insert"],
                         {"teacher_id": teacher_id,
                          "email": email,
                          "group_id": group_id})

    def update_teacher_group_id(self, teacher_id, new_group_id):
        with self.engine.begin() as conn:
            conn.execute(self.q.teacher["update_group_id"],
                         {"teacher_id": teacher_id,
                          "new_group_id": new_group_id})

    def delete_teacher(self, teacher_id):
        with self.engine.begin() as conn:
            conn.execute(self.q.teacher["delete"],
                         {"teacher_id": teacher_id})
