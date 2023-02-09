import pytest


@pytest.fixture()
def setup():
    print("Open URL")


def test_sending_mail():
    print("Sending email3")


def test_sending_mail2():
    print("Sending email4")