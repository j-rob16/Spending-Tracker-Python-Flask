from flask import Flask, request, render_template, redirect
from flask import Blueprint
from models.user import User
import repositories.user_repository as user_repo

users_blueprint = Blueprint('users', __name__)

@users_blueprint.route('/users')
def users():
    all_users = user_repo.select_all()
    return render_template('users/index.html', users=all_users)

@users_blueprint.route('/users/<id>')
def show_account(id):
    user = user_repo.select(id)
    return render_template('users/account.html', user=user)