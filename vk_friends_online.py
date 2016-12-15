import vk
import getpass


APP_ID = 5761423


def get_user_login():
    return input("Enter your login: ")


def get_user_password():
    return getpass.getpass(prompt="Enter your password: ")


def get_online_friends(login, password):
    try:
        session = vk.AuthSession(
            app_id=APP_ID,
            user_login=login,
            user_password=password,
            scope='friends'
        )
        api = vk.API(session)
        online_friends_ids = api.friends.getOnline()
        return online_friends_ids
    except vk.exceptions.VkAuthError:
        print("Incorrect Login and/or Password")
        exit()


def output_friends_to_console(friends_online):
    session = vk.Session()
    api = vk.API(session)
    for friend in friends_online:
        friend_info = api.users.get(user_ids=friend)
        print(friend_info[0]['first_name'], friend_info[0]['last_name'])


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    print("List of your online friends: ")
    output_friends_to_console(friends_online)
