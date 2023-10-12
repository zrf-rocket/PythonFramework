from django.conf import settings
from django.template.context import Context
from django.http import HttpResponse, JsonResponse
from mako.template import Template
from mako.cache import *
import mako.util
import mako.lexer
import mako.compat
import mako.ast
import mako.cmd
import mako.filters
import mako.exceptions
from mako.lookup import TemplateLookup, Template as lookup_tmp
import mako.parsetree
import mako.runtime
import mako.pygen
# import mako.testing.config
# import mako.testing.helpers
# import mako.testing.fixtures
# import mako.testing.exclusions
import os
# path参数是模板所在的目录

def render_to_response(t, c=None, context_instance=None):
    path = settings.BASE_DIR / "templates/"
    mylookup = TemplateLookup(directories=[path], output_encoding='utf-8')
    mako_temp = mylookup.get_template(t)
    if context_instance:
        context_instance.update(c)
    else:
        context_instance = Context(c)
    data = {}
    for d in context_instance:data.update(d)
    return HttpResponse(mako_temp.render(**data))

def render_to_json():
    pass

def render_to_js():
    pass

def render_js():
    pass

def render_json():
    pass



