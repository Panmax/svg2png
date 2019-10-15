# -*- coding: utf-8 -*-

from __future__ import unicode_literals, absolute_import

import io
import cairosvg
import imgkit
import logging

from flask import Blueprint, request, send_file


bp = Blueprint('home', __name__)


@bp.route('/convert', methods=['POST'])
def index():
    data = request.data
    ret = cairosvg.svg2png(bytestring=data)
    return send_file(io.BytesIO(ret), mimetype='image/png')


@bp.route('/html/convert', methods=['POST'])
def html_convert():
    data = request.data
    ret = imgkit.from_string(data.decode('utf-8'), False, options={'format': 'png', 'encoding': "UTF-8", })
    return send_file(io.BytesIO(ret), mimetype='image/png')


@bp.route('/html/convert', methods=['GET'])
def test_html_convert():
    html = '<h1>Hello World!</h1>'

    ret = imgkit.from_string(html.encode(""), False, options={'format': 'png', 'encoding': "UTF-8", })
    return send_file(io.BytesIO(ret), mimetype='image/png')
