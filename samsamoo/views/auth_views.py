from flask import Blueprint, render_template, url_for, request, flash
from werkzeug.security import generate_password_hash
from werkzeug.utils import redirect

from samsamoo import db
from samsamoo.forms import UserCreateForm
from samsamoo.models import User

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/signup/', methods=['GET', 'POST'])
def signup():
    form = UserCreateForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = User(username=form.username.data, password=generate_password_hash(form.password1.data), email=form.email.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('main.index'))

    else: flash('이미 존재하는 사용자입니다')

    return render_template('auth/signup.html', form=form)
