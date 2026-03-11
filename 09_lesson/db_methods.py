from sqlalchemy import create_engine
from db_queries import DB_Queries


class DB_Methods:
    def __init__(self, connection_string):
        self.engine = create_engine(connection_string)
        self.q = DB_Queries()

    def get_all_subjects(self):
        conn = self.engine.connect()
        result = conn.execute(self.q.subject["select_all"])
        rows = result.mappings().all()
        conn.close()
        return rows

    def get_subject(self, subject_id):
        conn = self.engine.connect()
        result = conn.execute(self.q.subject["select_by_id"],
                              {"subject_id": subject_id})
        row = result.mappings().first()
        conn.close()
        return row

    def create_subject(self, subject_id, title):
        conn = self.engine.connect()
        conn.execute(
            self.q.subject["insert"],
            {"subject_id": subject_id, "title": title}
            )
        conn.commit()
        conn.close()

    def update_subject_title(self, subject_id, new_title):
        conn = self.engine.connect()
        conn.execute(
            self.q.subject["update"],
            {"subject_id": subject_id, "new_title": new_title}
            )
        conn.commit()
        conn.close()

    def delete_subject_by_subject_id(self, subject_id):
        conn = self.engine.connect()
        conn.execute(self.q.student["delete_by_subject_id"],
                     {"subject_id": subject_id})
        conn.execute(self.q.subject["delete"], {"subject_id": subject_id})
        conn.commit()
        conn.close()

    def get_user(self, user_id):
        conn = self.engine.connect()
        result = conn.execute(self.q.users["select_by_id"],
                              {"user_id": user_id})
        row = result.mappings().first()
        conn.close()
        return row

    def create_user(self, user_id, email, subject_id=None):
        conn = self.engine.connect()
        conn.execute(
            self.q.users["insert"],
            {"user_id": user_id, "email": email, "subject_id": subject_id}
            )
        conn.commit()
        conn.close()

    def update_user_email(self, user_id, new_email):
        conn = self.engine.connect()
        conn.execute(
            self.q.users["update"],
            {"user_id": user_id, "user_email": new_email}
            )
        conn.commit()
        conn.close()

    def delete_user(self, user_id):
        conn = self.engine.connect()
        conn.execute(self.q.group_student["delete_by_user_id"],
                     {"user_id": user_id})
        conn.execute(self.q.student["delete_by_user_id"], {"user_id": user_id})
        conn.execute(self.q.users["delete"], {"user_id": user_id})
        conn.commit()
        conn.close()

    def get_student(self, user_id):
        conn = self.engine.connect()
        result = conn.execute(self.q.student["select_by_id"], {
            "user_id": user_id
            })
        row = result.mappings().first()
        conn.close()
        return row

    def create_student(self, user_id, level, education_form, subject_id):
        conn = self.engine.connect()
        conn.execute(
            self.q.student["insert"],
            {
                "user_id": user_id,
                "level": level,
                "education_form": education_form,
                "subject_id": subject_id
            })
        conn.commit()
        conn.close()

    def update_student_level(self, user_id, new_level):
        conn = self.engine.connect()
        conn.execute(
            self.q.student["update_level"],
            {"user_id": user_id, "new_level": new_level})
        conn.commit()
        conn.close()

    def delete_student(self, user_id):
        conn = self.engine.connect()
        conn.execute(self.q.group_student["delete_by_user_id"],
                     {"user_id": user_id})
        conn.execute(self.q.student["delete_by_user_id"],
                     {"user_id": user_id})
        conn.commit()
        conn.close()

    def get_teacher(self, teacher_id):
        conn = self.engine.connect()
        result = conn.execute(self.q.teacher["select_by_id"],
                              {"teacher_id": teacher_id})
        row = result.mappings().first()
        conn.close()
        return row

    def create_teacher(self, teacher_id, email, group_id):
        conn = self.engine.connect()
        conn.execute(
            self.q.teacher["insert"],
            {
                "teacher_id": teacher_id,
                "email": email,
                "group_id": group_id
            })
        conn.commit()
        conn.close()

    def update_teacher_group_id(self, teacher_id, new_group_id):
        conn = self.engine.connect()
        conn.execute(
            self.q.teacher["update_group_id"],
            {
                "teacher_id": teacher_id,
                "new_group_id": new_group_id
            })
        conn.commit()
        conn.close()

    def delete_teacher(self, teacher_id):
        conn = self.engine.connect()
        conn.execute(self.q.teacher["delete"],
                     {"teacher_id": teacher_id})
        conn.commit()
        conn.close()
