import falcon
from ..controllers import users as users_controller

class Users(object):

	def on_get(self, _request, response, user_uid = None):

		users = users_controller.get_users(user_uid)

		response.status = falcon.HTTP_200
		response.media = {'message': None, 'data': users}

	def on_post(self, request, response, user_uid = None):

		user_name = request.media['name']

		new_user = users_controller.create_user(user_name)

		response.status = falcon.HTTP_201
		response.media = {'message': 'User Created Successfully', 'data': new_user}

	def on_put(self, request, response, user_uid):

		user_name = request.media['name']

		updated_user = users_controller.update_user(user_uid, user_name)

		response.status = falcon.HTTP_200
		response.media = {'message': 'User Updated Successfully', 'data': updated_user}

	def on_delete(self, _request, response, user_uid):

		user = users_controller.delete_user(user_uid)

		response.status = falcon.HTTP_200
		response.media = {'message': 'User Deleted Successfully', 'data': user}