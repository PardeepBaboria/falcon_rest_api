users = [{'uid': '1', 'name': 'Pardeep Baboria'}]

def get_users(user_uid = None):

	if user_uid:

		for user in users:

			if(user['uid'] == user_uid):
				return [user]

		return []

	return users

def create_user(name):

	user_uid = str(len(users) + 1)

	users.append({'uid': user_uid, 'name': name})

	return get_users(user_uid)

def update_user(user_uid, name):

	user = get_users(user_uid)[0]

	user['name'] = name

	return get_users(user_uid)

def delete_user(user_uid):

	for i in range(len(users)):

		if users[i]['uid'] == user_uid:

			del users[i]

			break

	return get_users(user_uid)