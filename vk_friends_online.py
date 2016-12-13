import vk


APP_ID = 5761423


def get_user_login():
    return input("Enter your login: ")


def get_user_password():
    return input("Enter your password: ")


def get_online_friends(login, password):
    try:
        session = vk.AuthSession(
            app_id=APP_ID,
            user_login=login,
            user_password=password,
            scope='friends'
        )
        api = vk.API(session)
        friends = api.friends.get(fields='online')
        return [friend for friend in friends if friend['online']==1]
    except vk.exceptions.VkAuthError:
        print("Incorrect Login and/or Password")
        exit()


def output_friends_to_console(friends_online):
    for friend in friends_online:
        print(friend['first_name'], friend['last_name'])


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    print("List of your online friends: ")
    output_friends_to_console(friends_online)
