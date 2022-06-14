from crypt import methods
from flask import Flask, request, render_template, redirect
from flask import Blueprint

from models.tag import Tag
import repositories.tag_repository as tag_repo
import repositories.transaction_repository as transaction_repo

tags_blueprint = Blueprint('tags', __name__)

@tags_blueprint.route('/categories')
def categories():
    all_tags = tag_repo.select_all()
    return render_template('categories/index.html', tags=all_tags)

@tags_blueprint.route('/categories/<id>')
def show_category(id):
    tag = tag_repo.select(id)
    total = transaction_repo.get_tag_total(id)
    return render_template('/categories/category.html', tag=tag, total=total)

@tags_blueprint.route('/categories/new')
def new_category():
    return render_template('/categories/new.html')

@tags_blueprint.route('/categories', methods=['POST'])
def create_category():
    name = request.form['category']
    tag = Tag(name)
    tag_repo.save(tag)
    return redirect('/merchants')

@tags_blueprint.route('/categories/<id>/edit')
def edit_tag(id):
    tag = tag_repo.select(id)
    return render_template('/categories/edit.html', tag=tag)

@tags_blueprint.route('/categories/<id>', methods=['post'])
def update_tag(id):
    category = request.form['category']
    tag = Tag(category, id)
    tag_repo.update(tag)
    return redirect('/merchants')

@tags_blueprint.route('/categories/<id>/delete')
def delete_category(id):
    tag_repo.delete(id)
    return redirect('/merchants')