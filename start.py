# coding: utf8
import os
from bottle import Bottle, run, view, static_file, url

app = Bottle()
#bottle.debug(True)
# Define dirs
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, 'static')

# Static files route
@app.get('/static/<filename:path>')
def get_static_files(filename):
        """Get Static files"""
        return static_file(filename, root=STATIC_DIR)


@app.route('/')
@view('views/index.tpl')
def hello():
    context = {'content': 'Hello Bottle.py'}
    return context


run(app, host='localhost', port=8080, reloader=True)
