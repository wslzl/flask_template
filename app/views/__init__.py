from .users import users


def init_app(app):
    app.register_blueprint(users)