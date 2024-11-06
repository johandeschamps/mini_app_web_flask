from flask import Flask
from config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    @app.route('/index')
    def index():
        return 'Hello, World!'

    return app

if __name__ == "__main__":
    app = create_app('config')
    app.run()