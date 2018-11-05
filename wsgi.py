# -*- coding: utf-8 -*-

from __future__ import unicode_literals, absolute_import

from app.app import create_app

app = create_app()

if __name__ == '__main__':
    app.run()
