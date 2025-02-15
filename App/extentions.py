from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_caching import Cache

db = SQLAlchemy()
migrate = Migrate()
cache = Cache(config={'CACHE_TYPE':'simple'})

def init_exts(app):
    db.init_app(app=app)
    migrate.init_app(app=app,db=db)
    cache.init_app(app=app)
