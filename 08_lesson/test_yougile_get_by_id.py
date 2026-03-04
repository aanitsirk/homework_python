import pytest
from yougile_API import YouGileAPI

api = YouGileAPI()


@pytest.fixture
def project_id():
    create_resp = api.create_project('Проверка получения проекта по ID')
    assert create_resp.status_code == 201
    project_id = create_resp.json()['id']
    return project_id


def test_positive_get_project_by_id(project_id):
    get_resp = api.get_project(project_id)
    assert get_resp.status_code == 200
    assert get_resp.json()['id'] == project_id
    assert 'title' in get_resp.json()
    assert 'timestamp' in get_resp.json()


def test_positive_get_project_all_required_fields(project_id):
    get_resp = api.get_project(project_id)
    assert get_resp.status_code == 200
    assert 'id' in get_resp.json()
    assert 'title' in get_resp.json()
    assert 'timestamp' in get_resp.json()


def test_negative_get_project_by_invalid_id():
    invalid_id = 'буквы вместо цифр'
    get_resp = api.get_project(invalid_id)
    assert get_resp.status_code == 404


def test_negative_get_real_project_without_token():
    import requests
    url = api.base_url + '/projects/' + 'a360b3e5-45c7-4058-b0c7-32fade5a367c'
    get_resp = requests.get(url)
    assert get_resp.status_code == 401
