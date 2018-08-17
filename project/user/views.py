# !/usr/bin/python
# -*- coding: utf-8 -*-
""" Created by andresilva on 2/19/16"""
from flask import redirect, render_template, request, url_for, Blueprint
from flask_login import login_required, current_user

from project.user.handlers.user_handler import UserHandler
from project.user.forms import LoginForm, RegisterForm
from project.utils import flash


user_blueprint = Blueprint('user', __name__)


@user_blueprint.route('/settings/', methods=['GET'])
@login_required
def settings():
    flash.info('Welcome to your dashboard "{}".'.format(str(current_user)))
    return render_template('user/settings.html')


@user_blueprint.route('/sign-in/', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)

    if request.method == "POST":
        user = UserHandler.register(form)
        if user:
            flash.info('Welcome "{}".'.format(str(user)))
            return redirect(request.args.get('next', url_for('app.home')))

    return render_template('user/register.html', form=form)


@user_blueprint.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)

    if request.method == "POST":
        user = UserHandler.login(form)
        if user:
            flash.info('Welcome "{}".'.format(str(user)))
            return redirect(request.args.get('next', url_for('app.home')))

    return render_template('user/login.html', form=form)


@user_blueprint.route('/logout/')
def logout():
    UserHandler.logout()
    flash.info(u'You were logged out.')
    return redirect(url_for('app.home'))
