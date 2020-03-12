from Server.db import db, ma
from Server.Models.user import User


class Blog(db.Model):
    __tablename__ = 'blogs'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(200))
    author = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, title, description, author):
        self.title = title
        self.description = description
        self.author = author

# Product Schema


class BlogSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'description', 'author')


# Init schema
blog_schema = BlogSchema()
blogs_schema = BlogSchema(many=True,)
