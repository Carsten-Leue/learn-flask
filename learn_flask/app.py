from typing import Callable
from flask import Flask, jsonify, request
from .encoder import CustomJSONEncoder
from .models import DeviceAttributes
from .iplink import IpLink
from .controllers import show_devices, show_device
from logging import Logger


def create_app(fct: Callable[[Logger], IpLink]):
    app = Flask(__name__)
    app.json_encoder = CustomJSONEncoder

    iplink = fct(app.logger)

    @app.route('/')
    def app_show_devices():
        return jsonify(show_devices(iplink))

    @app.route('/<string:name>')
    def app_show_device(name: str):
        return jsonify(show_device(iplink, name))

    @app.route('/<string:name>', methods=['POST'])
    def app_add_device(name: str):
        print(request)
        return jsonify(show_device(iplink, name))

    return app
