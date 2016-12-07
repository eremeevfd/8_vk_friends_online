import vk


APP_ID = 5761423  # чтобы получить app_id, нужно зарегистрировать своё приложение на https://vk.com/dev


def get_user_login():
    return input()


def get_user_password():
    return input()


def get_online_friends(login, password):
    try:
        session = vk.AuthSession(
            app_id=APP_ID,
            user_login=login,
            user_password=password,
            scope='friends'
        )
        api = vk.API(session)
        return api.friends.get(fields='name')
    except vk.exceptions.VkAuthError:
        print("Incorrect Login and/or Password")
        exit()


def output_friends_to_console(friends_online):
    for friend in friends_online:
        if friend.get('online'):
            print(friend.get('first_name'), friend.get('last_name'))


if __name__ == '__main__':
    print("Enter your login: ")
    login = get_user_login()
    print("Enter your password: ")
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    print("List of your online friends: ")
    output_friends_to_console(friends_online)
