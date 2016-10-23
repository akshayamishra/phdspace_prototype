from flask import Flask

app = Flask(__name__)

app.secret_key = 'development key'

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config["MAIL_USERNAME"] = 'akshaya.ku.mishra@gmail.com'
app.config["MAIL_PASSWORD"] = 'tms54321'

from routes import mail
mail.init_app(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:tms54321@localhost/development'

from models import db
db.init_app(app)

import basic_app.routes
