from db_methods import DB_Methods


db_connection_string = "postgresql://postgres:123@localhost:5432/postgres"
db = DB_Methods(db_connection_string)


def test_db_connection():
    result = db.get_all_subjects()
    assert result is not None


def test_subject_create():
    subject_id = 1
    while db.get_subject(subject_id):
        subject_id += 100
    title = 'Право'

    db.create_subject(subject_id, title)
    subject = db.get_subject(subject_id)

    assert subject is not None
    assert subject["subject_title"] == title

    db.delete_subject_by_subject_id(subject_id)


def test_subject_title_update():
    subject_id = 2
    while db.get_subject(subject_id):
        subject_id += 100
    title = 'Обществоведение'

    db.create_subject(subject_id, title)

    new_title = 'Обществознание и право'
    db.update_subject_title(subject_id, new_title)

    updated = db.get_subject(subject_id)
    assert updated["subject_title"] == new_title

    db.delete_subject_by_subject_id(subject_id)


def test_subject_delete():
    subject_id = 3
    while db.get_subject(subject_id):
        subject_id += 100

    title = 'Урок для удаления'
    db.create_subject(subject_id, title)

    db.delete_subject_by_subject_id(subject_id)

    assert db.get_subject(subject_id) is None


def test_student_create():
    user_id = 123456
    while db.get_user(user_id):
        user_id += 1000
    subject_id = 4
    while db.get_subject(subject_id):
        subject_id += 100

    db.create_user(user_id, "student_email_db_test@test.com")
    db.create_subject(subject_id, "Геометрия")
    db.create_student(user_id, "Beginner", "personal", subject_id)

    student = db.get_student(user_id)
    assert student is not None
    assert student["user_id"] == user_id
    assert student["level"] == "Beginner"
    assert student["education_form"] == "personal"
    assert student["subject_id"] == subject_id

    db.delete_student(user_id)
    db.delete_user(user_id)
    db.delete_subject_by_subject_id(subject_id)


def test_student_level_update():
    user_id = 123456
    while db.get_user(user_id):
        user_id += 1000
    subject_id = 5
    while db.get_subject(subject_id):
        subject_id += 100

    db.create_user(user_id, "student_email_db_test@test.com")
    db.create_subject(subject_id, "Высшая математика")
    db.create_student(user_id, "Pre-Intermediate", "personal", subject_id)

    new_level = "Upper-Intermediate"
    db.update_student_level(user_id, new_level)

    updated = db.get_student(user_id)
    assert updated["level"] == new_level

    db.delete_student(user_id)
    db.delete_user(user_id)
    db.delete_subject_by_subject_id(subject_id)


def test_student_delete():
    user_id = 123456
    while db.get_user(user_id):
        user_id += 1000
    subject_id = 6
    while db.get_subject(subject_id):
        subject_id += 100

    db.create_user(user_id, "student_email_db_test@test.com")
    db.create_subject(subject_id, "Русская литература")
    db.create_student(user_id, "Advanced", "group", subject_id)

    db.delete_student(user_id)

    assert db.get_student(user_id) is None

    db.delete_user(user_id)
    db.delete_subject_by_subject_id(subject_id)


def test_teacher_create():
    teacher_id = 777
    while db.get_teacher(teacher_id):
        teacher_id += 100

    email = f"teacher_{teacher_id}@example_test.com"
    group_id = 1

    db.create_teacher(teacher_id, email, group_id)

    teacher = db.get_teacher(teacher_id)
    assert teacher is not None
    assert teacher["email"] == email
    assert teacher["group_id"] == group_id

    db.delete_teacher(teacher_id)


def test_teacher_update_group():
    teacher_id = 1
    while db.get_teacher(teacher_id):
        teacher_id += 100

    email = f"teacher_{teacher_id}@yandex.ru"
    group_id = 1
    db.create_teacher(teacher_id, email, group_id)

    new_group_id = 123
    db.update_teacher_group_id(teacher_id, new_group_id)

    updated = db.get_teacher(teacher_id)
    assert updated["group_id"] == new_group_id

    db.delete_teacher(teacher_id)


def test_teacher_delete():
    teacher_id = 3472
    while db.get_teacher(teacher_id):
        teacher_id += 100

    email = "teacher@yandex.ru"
    group_id = 9
    db.create_teacher(teacher_id, email, group_id)

    db.delete_teacher(teacher_id)

    assert db.get_teacher(teacher_id) is None
