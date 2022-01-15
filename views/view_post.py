"""
Module contains all functions working on post page.

Functions:
    post_list()
    post_create()
    post_detail(slug)
    tag_detail(slug)
    post_update(slug)
    delete_post(slug)
"""

from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import *
from service.service_forms import PostForm
from service.service_post import post_create_from_db, post_update_from_db, post_delete_from_db
from flask_security import login_required, current_user

posts = Blueprint('posts', __name__)


@posts.route('/')
def post_list():
    """
    Function showing list of post.
        1) search result for one of the parameters
        2) creating paginated list
    :return: template of the list
    """
    q = request.args.get('q')
    if q and q is not None:
        posted = Posts.query.filter(Posts.title.contains(q) | Posts.body.contains(q))
        if posted.first() is None:
            posted = Posts.query.order_by(Posts.created.desc())
    else:
        posted = Posts.query.order_by(Posts.created.desc())
    page = request.args.get('page')
    if page and page.isdigit():
        page = int(page)
    else:
        page = 1
    pages = posted.paginate(page=page, per_page=1)
    return render_template("post/posts.html", posted=posted, pages=pages)


@posts.route('/create', methods=['POST', 'GET'])
@login_required
def post_create():
    """
    Function working on create new post:
        1) adding new post in database if method "POST".
        2) showing the fields for create post
    :return: redirect post_detail or post_list, if there are no privileges, or post creation page
    """
    form = PostForm()
    if current_user.has_role('manager'):
        if request.method == "POST":
            title = request.form.get('title')
            body = request.form.get('body')
            post = Posts(title=title, body=body)
            post_create_from_db(post)
            return redirect(url_for('posts.post_detail', slug=post.slug)), flash('Successful create post!')
        return render_template('post/post_create.html', form=form)
    return redirect(url_for("posts.post_list")), flash("Use the admin panel!") if current_user.has_role(
        "admin") else flash('You have no privileges!')


@posts.route('/<slug>')
def post_detail(slug):
    """
    Function showing all information of post
    :param slug: identifier of post page
    :return: template posts_slug
    """
    posted = Posts.query.filter(Posts.slug == slug).first_or_404()
    return render_template('post/posts_slug.html', posted=posted)


@posts.route('/tags/<slug>')
def tag_detail(slug):
    """
    Function that shows all the information about the found posts
    :param slug: identifier of post pages
    :return: template tag_detail
    """
    tag = Tag.query.filter(Tag.slug == slug).first_or_404()
    return render_template('post/tag_detail.html', tag=tag)


@posts.route('/<slug>/update', methods=['POST', 'GET'])
@login_required
def post_update(slug):
    """
    Function working on updating post:
        1) adding updating  parameters in database if method "POST".
        2) showing the fields for update post
    :param slug: identifier of post pages
    :return: redirect post_detail or template of update post page
    """
    post = Posts.query.filter(Posts.slug == slug).first_or_404()
    if current_user.has_role('manager'):
        if request.method == 'POST':
            post_update_from_db(post)
            return redirect(url_for('posts.post_detail', slug=post.slug)), flash("Update successful!")
        form = PostForm(obj=post)
        return render_template('post/update_post.html', post=post, form=form)
    return redirect(url_for("posts.post_detail", slug=post.slug)), flash(
        "Use the admin panel!") if current_user.has_role("admin") else flash('You have no privileges!')


@posts.route('/<slug>/delete')
@login_required
def delete_post(slug):
    """
    Function for deleting a post
    :param slug: identifier of post pages
    :return: redirect post_detail or post_list
    """
    post = Posts.query.filter(Posts.slug == slug).first_or_404()
    if current_user.has_role('manager'):
        if post and current_user.has_role('manager'):
            post_delete_from_db(post)
        else:
            flash('Use the admin panel!')
        return redirect(url_for('posts.post_list')), flash(f'Successful delete {post.title} post!')
    return redirect(url_for("posts.post_detail", slug=post.slug)), \
           flash("Use the admin panel!") if current_user.has_role("admin") else flash('You have no privileges!')
