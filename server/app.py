from flask import Flask
from flask_migrate import Migrate
from models import db

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)
    migrate = Migrate(app, db)
    
    return app

app = create_app()

@app.route('/')
def index():
    return 'Welcome to the Flask-SQLAlchemy Lab!'

if __name__ == '__main__':
    app.run(port=5555, debug=True)