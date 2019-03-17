from flask import Blueprint

from .views import *

# router register blueprint
indiawyn_router = Blueprint('indiawyn_router', __name__)

# # register views
indiawyn_router.add_url_rule('/movies/<int:title_id>/',view_func=movies,methods=['GET'])
indiawyn_router.add_url_rule('/',view_func=movies,methods=['GET'])
indiawyn_router.add_url_rule('/search/', defaults={'title_id': None}, view_func=movies, methods=['GET'])


# # register apis
indiawyn_router.add_url_rule('/api/v1/title/', defaults={'title_id': None}, view_func=movie_setup_api, methods=['GET'])

indiawyn_router.add_url_rule('/api/v1/title/<int:title_id>/',view_func=movie_setup_api, methods=['GET'])

