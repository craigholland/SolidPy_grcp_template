import os

from flask import Flask
from dataclasses import fields

from solidpy_domain.common.dataclass.person import Person, Organization

app = Flask(__name__)


@app.route("/")
def hello_world():
    """Example Hello World route."""
    name = os.environ.get("USERNAME", "World")
    dc_str = "Dataclass: {0}; fields: {1}"
    hello_str = "Hello {0}!".format(name)
    hello_str += "<br><br>" + dc_str.format(Person.__name__, fields(Person))
    hello_str += "<br><br>" + dc_str.format(Organization.__name__, fields(Organization))
    return hello_str


if __name__ == "__main__":
    APP_HOST = os.environ.get("APP_HOST", "8.8.8.8")    # 8.8.8.8 shouldn't work; APP_HOST should pull from .env
    APP_PORT = int(os.environ.get("APP_PORT", 5000))
    app.run(debug=True, host=APP_HOST, port=APP_PORT)
