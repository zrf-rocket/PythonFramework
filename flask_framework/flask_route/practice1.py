import global_settings_base
from flask import (Blueprint, Config, Flask, Request, Response, abort,
                   after_this_request, appcontext_popped, appcontext_pushed,
                   appcontext_tearing_down, before_render_template,
                   copy_current_request_context, current_app, flash, g,
                   get_flashed_messages, get_template_attribute, globals,
                   got_request_exception, has_app_context, has_request_context,
                   json, jsonify, make_response, message_flashed, redirect,
                   render_template, render_template_string, request,
                   request_finished, request_started, request_tearing_down,
                   send_file, send_from_directory, session, stream_template,
                   stream_template_string, stream_with_context,
                   template_rendered, url_for)

app = Flask(__name__)


@app.before_request
def log_request():
    print(f'请求之前：Request:{request.method} {request.url} {request.url_root} {request.url_charset}')


@app.route("/hello")
def hello():
    return 'hello steverocket'


@app.route("/index/<username>")
def index1(username):
    return f"hello {username}"


@app.route("/index/<int:age>/<string:name>")
def index2(age, name):
    return f"hello my name is{name} old is:{age} "



@app.route("/methods", methods=['POST'])
def index3():
    return jsonify({"name": global_settings_base.AUTHOR, "age": global_settings_base.AGE})


@app.after_request
def add_header(response):
    response.headers['X-My-Header'] = 'SteveRocket'
    return response


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(405)
def method_not_allowed(e):
    return render_template('405.html'), 405