"""This blueprint takes care of rendering static pages outside of the other
blueprints.
"""
from flask import Blueprint, render_template, send_file, jsonify, redirect, \
    url_for

core = Blueprint("core", __name__, url_prefix="/")


# homepage
@core.route('')
def home():
    """Display the homepage."""
    return render_template('core/index.html',
                           is_home=True)
