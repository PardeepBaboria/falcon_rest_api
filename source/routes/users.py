import falcon
from ..controllers import users as users_controller

class Users(object):

	def on_get(self, _request, response):

		users = users_controller.get_users()

		response.status = falcon.HTTP_200
		response.media = users