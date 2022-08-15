from flask import Blueprint, redirect, request, session, url_for
from app.controller.Contents import Contents
from app.controller.Search import Search
from app.controller.User import User
from app.controller.File import File
from app.controller.Login import Login
from app.controller.Console import Console

router = Blueprint('router', __name__)

@router.route('/', methods=['GET'])
def root():
    return redirect(url_for('router.get_all', proc='all', page='1'))
@router.route('/contents/<proc>', methods=['GET'])
def get_all(proc):
    return Contents.get(proc)

@router.route('/login', methods=['GET','POST'])
def login():
        return Login.proccess_login()

@router.route('/console/<proc>', methods=['GET'])
def console(proc):
        return Console.main_entrance(proc)

@router.route('/file/<proc>', methods=['POST'])
def file(proc):
        return File.main_entrance(proc)

@router.before_request
def confirmAuthorization():
        endpoint = request.endpoint
        if endpoint == 'router.console' or endpoint == 'router.file':
                if not 'user_id' in session:
                        return redirect(url_for('router.login'))
        