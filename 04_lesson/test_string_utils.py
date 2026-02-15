import pytest
from string_utils import StringUtils

string_utils = StringUtils()


@pytest.mark.capitalize_positive
@pytest.mark.parametrize('input_str, expected', [
        ('test', 'Test'),
        ('first test', 'First test'),
        ('PYTHON', 'Python'),
        ('kRiStInA', 'Kristina'),
        ('first_test', 'First_test'),
        ('a', 'A')
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.capitalize_negative
@pytest.mark.parametrize('input_str, expected', [
    ('123abc', '123abc'),
    ('', ''),
    ('   ', '   '),
    ('  test', '  test'),
    ('@$?', '@$?')
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.trim_positive
@pytest.mark.parametrize('input_str, expected', [
        ('test', 'test'),
        (' Kristina', 'Kristina'),
        ('  second test', 'second test'),
        ('   123test', '123test'),
        (' &$@', '&$@'),
        (' a b c ', 'a b c '),
        (' ' * 100 + 'python', 'python')
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.trim_negative
@pytest.mark.parametrize('input_str, expected', [
    ('', ''),
    ('   ', '')
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.contains_positive
@pytest.mark.parametrize('string, symbol, expected', [
    ('Test', 'T', True),
    ('test123', '2', True),
    ('mail.ru', '.', True),
    ('Kristina Maslova', ' ', True),
    ('PythonIsHard', 'Is', True)
])
def test_contains_positive(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected


@pytest.mark.contains_negative
@pytest.mark.parametrize('string, symbol, expected', [
    ('kristina', 'P', False),
    ('', ' ', False),
    ('empty', '', False),
    ('123', 'abc', False)
])
def test_contains_negative(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected


@pytest.mark.delete_symbol_positive
@pytest.mark.parametrize('string, symbol, expected', [
    ('Python', 'P', 'ython'),
    ('Kristina Maslova', 'Maslova', 'Kristina '),
    ('Kristina Maslova', ' ', 'KristinaMaslova'),
    ('SkyPro', 'Pro', 'Sky'),
    ('empty', 'empty', ''),
    ('abc123', 'c1', 'ab23'),
    ('mail@ru', '@', 'mailru'),
    ('three green trees', 'e', 'thr grn trs')
])
def test_delete_symbol_positive(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected


@pytest.mark.delete_symbol_negative
@pytest.mark.parametrize('string, symbol, expected', [
    ('PythonIsHard', 'F', 'PythonIsHard'),
    ('', ' ', ''),
    ('SkyPro', '', 'SkyPro'),
    ('123', 'a', '123')
])
def test_delete_symbol_negative(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected
