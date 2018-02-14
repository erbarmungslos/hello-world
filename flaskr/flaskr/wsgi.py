from flask import Flask

app = Flask('flaskr')#__name__)
app.config.from_pyfile('config.cfg')
