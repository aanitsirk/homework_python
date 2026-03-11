from sqlalchemy import text


class DB_Queries:
    subject = {
        "select_all": text("SELECT * from subject ORDER BY subject_id"),
        "select_by_id": text("SELECT * from subject "
                             "WHERE subject_id = :subject_id"),
        "insert": text(
            "INSERT INTO subject(\"subject_title\", \"subject_id\") "
            "VALUES (:title, :subject_id)"),
        "update": text("UPDATE subject SET subject_title = :new_title "
                       "WHERE subject_id = :subject_id"),
        "delete": text("DELETE from subject WHERE subject_id = :subject_id")
    }
    users = {
        "select_by_id": text("SELECT * FROM users WHERE user_id = :user_id"),
        "insert": text(
            "INSERT INTO users(\"user_id\", \"user_email\", \"subject_id\") "
            "VALUES (:user_id, :email, :subject_id)"),
        "update_email": text(
            "UPDATE users SET user_email = :new_email "
            "WHERE user_id = :user_id"),
        "delete": text("DELETE from users WHERE user_id = :user_id")
    }
    teacher = {
        "select_by_id": text("SELECT * from teacher "
                             "WHERE teacher_id = :teacher_id"),
        "insert": text(
            "INSERT INTO teacher(\"teacher_id\", \"email\", \"group_id\") "
            "VALUES (:teacher_id, :email, :group_id)"),
        "update_group_id": text(
            "UPDATE teacher SET group_id = :new_group_id "
            "WHERE teacher_id = :teacher_id"),
        "delete": text("DELETE from teacher WHERE teacher_id = :teacher_id")
    }
    student = {
        "select_by_id": text(
            "SELECT * FROM student "
            "WHERE user_id = :user_id"),
        "insert": text(
            "INSERT INTO student"
            "(\"user_id\", \"level\", \"education_form\", \"subject_id\") "
            "VALUES (:user_id, :level, :education_form, :subject_id)"),
        "update_level": text(
            "UPDATE student SET level = :new_level "
            "WHERE user_id = :user_id"),
        "delete_by_user_id": text(
            "DELETE FROM student "
            "WHERE user_id = :user_id"),
        "delete_by_subject_id": text(
            "DELETE FROM student "
            "WHERE subject_id = :subject_id")
    }
    group_student = {
        "delete_by_user_id": text(
            "DELETE FROM group_student WHERE user_id = :user_id")
    }
