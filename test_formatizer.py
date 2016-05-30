import pytest

from formatizer import f


def test_literal_string():
    assert f('hello') == 'hello'


def test_expression_variables():
    name = 'Booboo'
    assert f('{name}') == name


def test_expression_variables_complex():
    name = 'Booboo'
    assert f('{name[0] + "ah"}') == 'Bah'


def test_format_spec():
    name = 'Boo'
    assert f('{name:>5}') == '  Boo'


def test_conversion_s():
    number = 123
    assert f('{number!s}') == '123'


def test_conversion_r():
    name = 'Booboo'
    assert f('{name!r}') == "'" + name + "'"


def test_conversion_invalid():
    name = 'Booboo'
    with pytest.raises(ValueError):
        f('{name!z}')


def test_full_example():
    name = 'Booboo'
    interests = {'being': 'cool'}
    assert (
        f('My name is {name!s:>8} and I like {interests!r} years old') ==
        "My name is   Booboo and I like {'being': 'cool'} years old"
    )
