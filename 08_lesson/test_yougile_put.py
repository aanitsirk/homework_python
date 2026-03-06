import pytest
from yougile_API import YouGileAPI

api = YouGileAPI()


@pytest.fixture
def project_id():
    create_resp = api.create_project('Это мой проект для метода put')
    assert create_resp.status_code == 201
    project_id = create_resp.json()['id']
    return project_id


def test_positive_update_project_title(project_id):
    new_title = 'Это мой проект 1 для метода PUT'
    update_resp = api.update_project(project_id, new_title)
    assert update_resp.status_code == 200
    assert update_resp.json()['id'] == project_id


def test_positive_update_project_long_title(project_id):
    new_title = ('Это очень длинное название для проекта для метода PUT,'
                 'но кто мне запретит, ведь в документации ничего не сказано'
                 'про количество символов в названии')
    update_resp = api.update_project(project_id, new_title)
    assert update_resp.status_code == 200
    assert update_resp.json()['id'] == project_id


def test_negative_update_project_invalid_id():
    invalid_id = '000000000000000000000000000000000000000'
    new_title = 'Вряд ли получится'
    update_resp = api.update_project(invalid_id, new_title)
    assert update_resp.status_code == 404


def test_negative_update_project_empty_title(project_id):
    new_title = ''
    update_resp = api.update_project(project_id, new_title)
    assert update_resp.status_code == 400
