from yougile_API import YouGileAPI

api = YouGileAPI()


def test_positive_create_project_with_only_required_title():
    title = 'Домашнее задание по библиотеке Requests'
    resp = api.create_project(title)
    assert resp.status_code == 201
    assert 'id' in resp.json()


def test_positive_create_project_with_symbols_in_title():
    title = '!ReQ*!es&t$'
    resp = api.create_project(title)
    assert resp.status_code == 201
    assert 'id' in resp.json()


def test_negative_create_project_with_integer_in_title():
    title = 88005553535
    resp = api.create_project(title)
    assert resp.status_code == 400
    assert 'message' in resp.json() or 'error' in resp.json()
    assert 'id' not in resp.json()


def test_negative_create_project_with_empty_title():
    title = ''
    resp = api.create_project(title)
    assert resp.status_code == 400
    assert 'message' in resp.json() or 'error' in resp.json()
    assert 'id' not in resp.json()
