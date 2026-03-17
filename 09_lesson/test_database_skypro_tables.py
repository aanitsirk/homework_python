import pytest
from db_methods import DB_Methods


db_connection_string = "postgresql://postgres:123@localhost:5432/postgres"
db = DB_Methods(db_connection_string)


@pytest.fixture
def subject():
    subject_id = 9999
    db.create_subject(subject_id, "Тестовый предмет")
    yield subject_id
    db.delete_subject_by_subject_id(subject_id)


@pytest.fixture
def user():
    user_id = 777777777
    db.create_user(user_id, "student_email_db_test@test.com")
    yield user_id
    db.delete_user(user_id)


@pytest.fixture
def teacher():
    teacher_id = 888888888
    db.create_teacher(teacher_id, "teacher_email_db_test@test.com", 1)
    yield teacher_id
    db.delete_teacher(teacher_id)


def test_db_connection():
    result = db.get_all_subjects()
    assert isinstance(result, list)


def test_subject_create(subject):
    subject_data = db.get_subject(subject)

    assert subject_data is not None
    assert subject_data["subject_title"] == "Тестовый предмет"


def test_subject_title_update(subject):
    new_title = 'Новое название предмета'
    db.update_subject_title(subject, new_title)

    assert db.get_subject(subject)["subject_title"] == new_title


def test_subject_delete():
    subject_id = 1111111
    db.create_subject(subject_id, "Предмет для удаления")

    db.delete_subject_by_subject_id(subject_id)

    assert db.get_subject(subject_id) is None


def test_student_create(user, subject):
    level = "Beginner"
    education_form = "personal"

    db.create_student(user, level, education_form, subject)

    student = db.get_student(user)
    assert student is not None
    assert student["user_id"] == user
    assert student["level"] == level
    assert student["education_form"] == education_form
    assert student["subject_id"] == subject

    db.delete_student(user)


def test_student_level_update(user, subject):
    db.create_student(user, "Pre-Intermediate", "personal", subject)

    new_level = "Upper-Intermediate"
    db.update_student_level(user, new_level)

    assert db.get_student(user)["level"] == new_level

    db.delete_student(user)


def test_student_delete(user, subject):
    db.create_student(user, "Advanced", "group", subject)

    db.delete_student(user)

    assert db.get_student(user) is None


def test_teacher_create(teacher):
    teacher_data = db.get_teacher(teacher)

    assert teacher_data is not None
    assert teacher_data["email"] == "teacher_email_db_test@test.com"
    assert teacher_data["group_id"] == 1


def test_teacher_update_group(teacher):
    new_group_id = 12345
    db.update_teacher_group_id(teacher, new_group_id)

    assert db.get_teacher(teacher)["group_id"] == new_group_id


def test_teacher_delete():
    teacher_id = 3472568
    db.create_teacher(teacher_id, "teacher@yandex.ru", 8)

    db.delete_teacher(teacher_id)

    assert db.get_teacher(teacher_id) is None
