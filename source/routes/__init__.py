import falcon
from .users import Users

class Ping(object):

	def on_get(self, _request, response):

		response.status = falcon.HTTP_200
		response.media = {"message": "pong"}

# Method to add routes to falcon app
def add(falcon_app, prefix = '/'):

	falcon_app.add_route(prefix + 'ping', Ping())
	falcon_app.add_route(prefix + 'users', Users())