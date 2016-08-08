"""Handle creating the app and configuring it.
"""
from quizApp import config
from flask import Flask


def create_app(config_name, overrides=None):
    """Create and return an instance of this application.
    """
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(config.configs[config_name])
    app.config.from_pyfile("instance_config.py", silent=True)
    if overrides:
        app.config.from_mapping(overrides)

    print "Using config: " + config_name

    from quizApp.views.core import core
    app.register_blueprint(core)

    return app
