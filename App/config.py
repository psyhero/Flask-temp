import datetime

# session config
SECRET_KEY = 'happydays'
PERMANENT_SESSION_LIFETIME = datetime.timedelta(days=10)

# DB config
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:mm546896@localhost:3306/demo0'
SQLALCHEMY_TRACK_MODIFICATIONS = False

