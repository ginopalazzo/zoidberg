#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `zoidberg` package."""

import pytest

from click.testing import CliRunner

from zoidberg import zoidberg
from zoidberg import cli





@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert 'zoidberg.cli.main' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output


def test_command_line_interface_required_arguments():
    """Test the CLI."""
    pass


def test_zoidberg_create_object_no_arguments():
    """Test create new zoidberg object"""
    pass


# country parameter
def test_zoidberg_create_object_country_not_iso_alpha_2():
    with pytest.raises(ValueError):
        zoidberg.Zoidberg(country='USA')


def test_zoidberg_create_object_country_raises_value_error_if_not_str():
    with pytest.raises(ValueError):
        zoidberg.Zoidberg(country=12)


"""
def test_zoidberg_create_object_country_raises_value_error_if_not_defined():
    with pytest.raises(ValueError):
        zoidberg.Zoidberg(country='xx')
"""


def test_zoidberg_create_object_country_is_defined():
    z = zoidberg.Zoidberg(country='es', doctor="xxx", area="xxx", illness="xxx")
    assert z.country == 'es'


# doctor parameter
def test_zoidberg_create_object_doctor_raises_value_error_if_none():
    with pytest.raises(ValueError):
        zoidberg.Zoidberg(country='es', area="xxx", illness="xxx")


def test_zoidberg_create_object_doctor_raises_value_error_if_not_str():
    with pytest.raises(ValueError):
        zoidberg.Zoidberg(country='es', doctor=1, area="xxx", illness="xxx")


# area parameter
def test_zoidberg_create_object_area_raises_value_error_if_none():
    with pytest.raises(ValueError):
        zoidberg.Zoidberg(country='es', doctor="xxx", illness="xxx")


def test_zoidberg_create_object_area_raises_value_error_if_not_str():
    with pytest.raises(ValueError):
        zoidberg.Zoidberg(country='es', doctor="xxx", area=1, illness="xxx")


# illness parameter
def test_zoidberg_create_object_illness_raises_value_error_if_none():
    with pytest.raises(ValueError):
        zoidberg.Zoidberg(country='es', doctor="xxx", area="xxx")


def test_zoidberg_create_object_illness_raises_value_error_if_not_str():
    with pytest.raises(ValueError):
        zoidberg.Zoidberg(country='es', doctor="xxx", area="xxx", illness=1)


# output parameter
def test_zoidberg_create_object_output_default_csv():
    z = zoidberg.Zoidberg(country='es', doctor="xxx", area="xxx", illness="xxx")
    assert z.output == 'csv'


def test_zoidberg_create_object_output_csv():
    z = zoidberg.Zoidberg(country='es', doctor="xxx", area="xxx", illness="xxx", output="csv")
    assert z.output == 'csv'


def test_zoidberg_create_object_output_json():
    z = zoidberg.Zoidberg(country='es', doctor="xxx", area="xxx", illness="xxx", output="json")
    assert z.output == 'json'


def test_zoidberg_create_object_output_raises_value_error_if_not_csv_or_json():
    with pytest.raises(ValueError):
        zoidberg.Zoidberg(country='es', doctor="xxx", area="xxx", illness="xxx", output="xml")



"""
def test_zoidberg_create_object_country():


def test_zoidberg_create_object_doctor():


def test_zoidberg_create_object_area():


def test_zoidberg_create_object_illness():


def test_zoidberg_create_object_path():


def test_zoidberg_create_object_output():
"""
