from crypt import methods
from flask import Flask, request, render_template, redirect
from flask import Blueprint

from models.tag import Tag
import repositories.tag_repository as tag_repo

tags_blueprint = Blueprint('tags', __name__)

@tags_blueprint.route('/categories')
def categories():
    all_tags = tag_repo.select_all()
    return render_template('categories/index.html', tags=all_tags)

@tags_blueprint.route('/categories/<id>')
def show_category(id):
    tag = tag_repo.select(id)
    return render_template('/categories/shop.html', tag=tag)

@tags_blueprint.route('/categories/new')
def new_category():
    return render_template('/categories/new.html')

@tags_blueprint.route('/categories', methods=['POST'])
def create_merchant():
    name = request.form['category']
    tag = Tag(name)
    tag_repo.save(tag)
    return redirect('/categories')