from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# 读取配置文件
app.config.from_object('config')
db = SQLAlchemy(app)

migrate = Migrate(app, db)
login = LoginManager()
login.init_app(app)
login.login_view = 'login'

from app import views, models
