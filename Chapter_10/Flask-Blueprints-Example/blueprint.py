# blueprint.py

from flask import Blueprint
from html_docstrings import home_html, user_html, admin_html, about_html

bp = Blueprint("blueprint", __name__)
 
@bp.route("/")
def home():
    return home_html
 
@bp.route("/user/")
def user_home():
    return user_html

@bp.route("/admin/")
def admin_home():
    return admin_html

@bp.route("/about/")
def about():
    return about_html




