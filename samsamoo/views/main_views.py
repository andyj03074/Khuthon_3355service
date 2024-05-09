from flask import Blueprint, render_template, url_for
from werkzeug.utils import redirect


bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/home')
def hello():
    return 'Hello!'


@bp.route('/signup', methods=['GET', 'POST'])
def signup():
    return redirect(url_for('auth.signup'))


@bp.route('/', methods=['GET', 'POST'])
def login():
    return redirect(url_for('auth.login'))