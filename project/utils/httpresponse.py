# !/usr/bin/python
# -*- coding: utf-8 -*-
import json
from bson import json_util
from flask import Response


def MyResponse(response, status, mimetype="application/json", **kwargs):
    return Response(json.dumps(response, default=json_util.default), status=status, mimetype=mimetype, **kwargs)


def OkResponse(response):
    response.update({'success': True})
    return MyResponse(response, 200)


def NotOkResponse(response):
    response.update({'success': False})
    return MyResponse(response, 400)
