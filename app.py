from flask import Flask
from wsgiref.simple_server import make_server
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from config import DATABASE_URI
from flask_migrate import Migrate
from user import user
from car import car
from order import order


from blueprint import api

app = Flask(__name__)

db = SQLAlchemy()
engine = create_engine(DATABASE_URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:123456@localhost:5432/lab6'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
ma = Marshmallow(engine)
Session = sessionmaker(bind=engine)
bcrypt = Bcrypt(app)
migrate = Migrate(app, db)
app.register_blueprint(user)
app.register_blueprint(order)
app.register_blueprint(car)
JSONIFY_PRETTYPRINT_REGULAR = False

@app.route('/')
def hello_world():
    return 'Hello World! - 15'



if __name__ == '__main__':
    app.run(debug=True)

# curl -v -XGET http://localhost:5000/api/v1/hello-world-30
# http://127.0.0.1:5000/api/v1/hello-world-30

#alembic stamp head
#alembic revision --autogenerate
#alembic upgrade head