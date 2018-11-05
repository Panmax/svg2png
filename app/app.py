# -*- coding: utf-8 -*-

from __future__ import unicode_literals, absolute_import

from flask import Flask
from werkzeug.utils import import_string, find_modules


extensions = [
]


def register_blueprints(root, app):
    for name in find_modules(root, recursive=True):
        mod = import_string(name)
        if hasattr(mod, 'bp'):
            app.register_blueprint(mod.bp)


def create_app():
    app = Flask(__name__)

    for extension_qualname in extensions:
        extension = import_string(extension_qualname)
        extension.init_app(app)

    register_blueprints('app.web', app)
    return app
