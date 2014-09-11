from flask.ext.classy import FlaskView



class IndexView(FlaskView):
    route_base = '/'

    def index(self):
        return 'Hello world'