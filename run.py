from flask import Flask
app = Flask(__name__)

from flask.ext.pymongo import PyMongo
mongo = PyMongo(app)

from src.views.index import IndexView
IndexView.register(app)




if __name__ == '__main__':
    app.run(debug=True)