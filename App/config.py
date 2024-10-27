import datetime

# session config
SECRET_KEY = 'happydays'
PERMANENT_SESSION_LIFETIME = datetime.timedelta(days=10)

# DB config
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:password@localhost:3306/db'
SQLALCHEMY_TRACK_MODIFICATIONS = False

