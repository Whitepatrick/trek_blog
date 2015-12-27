from flask import Flask
from flask.ext.mongoengine import MongoEngine
# credentials file .gitignored
from secret import SECRET_KEY as sk

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {'DB': "trek_blog"}
app.config["SECRET_KEY"] = sk

db = MongoEngine(app)


def register_blueprints(app):
    # Prevents circular imports
    from trek_blog.views import posts
    from trek_blog.admin import admin
    app.register_blueprint(posts)
    app.register_blueprint(admin)

register_blueprints(app)

if __name__ == '__main__':
    app.run()
