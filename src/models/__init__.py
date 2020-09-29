from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

# initialize our db
db = SQLAlchemy()

#######
# existing code remains #
#######
bcrypt = Bcrypt()

from .BlogPostModel import BlogPostModel, BlogPostSchema
from .UserModel import UserModel, UserSchema