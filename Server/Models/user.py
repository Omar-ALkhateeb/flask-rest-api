from Server.db import db, ma


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(200))
    db.relationship("Blog", viewonly=False, back_populates="author")

    def __init__(self, name, password):
        self.name = name
        self.password = password

# Product Schema


class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'password', 'posts')


# Init schema
user_schema = UserSchema()
users_schema = UserSchema(many=True, )
