# -*- coding: utf-8 -*-

from __future__ import unicode_literals, absolute_import

import io
import cairosvg
import imgkit

from flask import Blueprint, request, send_file

bp = Blueprint('home', __name__)


@bp.route('/convert', methods=['POST'])
def index():
    data = request.data
    ret = cairosvg.svg2png(bytestring=data)
    return send_file(io.BytesIO(ret), mimetype='image/png')


@bp.route('/html/convert', methods=['GET'])
def test_html_convert():
    url = request.args.get("url")
    h = request.args.get('h')
    w = request.args.get('w')

    options = {'format': 'png', 'encoding': "UTF-8", 'crop-h': h, 'crop-w': w, }
    ret = imgkit.from_url(url, False, options=options)
    return send_file(io.BytesIO(ret), mimetype='image/png')
