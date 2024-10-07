from classes import jogador, times
from flask import Flask, request
from sqlite3 import connect
from sqlalchemy import String
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column

app = Flask(__name__)

class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///main.db'
db = sqlalchemy.SQLAlchemy(app)
db.init_app(app)

@app.route('/')
def home():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True)