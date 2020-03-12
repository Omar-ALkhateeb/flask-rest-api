from dotenv import load_dotenv
import os
from flask import request, Flask, send_file, jsonify
from flask_jwt_extended import jwt_required, JWTManager, create_access_token, get_jwt_identity
from flask_cors import CORS, cross_origin
import datetime
import flask_bcrypt
from Server.db import db
from Server.Models import user, blog


app = Flask(__name__)
load_dotenv()

# OR, the same with increased verbosity
load_dotenv(verbose=True)
app.config['JWT_SECRET_KEY'] = os.environ.get('SECRET')
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(days=1)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
with app.app_context():
    db.create_all()

jwt = JWTManager(app)

# db.init(app)
CORS(app)


@app.route('/')
def hello():
    res = user.User.query.all()
    return user.users_schema.dumps(res)


app.run(debug=True)
