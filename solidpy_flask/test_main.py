import os

from flask import Flask
from dataclasses import fields

from solidpy_domain.common.dataclass.person import Person, Organization
from solidpy_flask.__main__ import app


def test_hello_world():
    """Test the hello world route."""
    with app.test_client() as client:
        response = client.get("/")
        assert response.status_code == 200
        assert b"Hello World!" in response.data
        assert b"Dataclass: Person; fields: " in response.data
        assert b"Dataclass: Organization; fields: " in response.data
        assert b"Dataclass: Survey; fields: " not in response.data