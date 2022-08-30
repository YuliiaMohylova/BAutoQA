import os


class UsersProvider:

    @staticmethod
    def fake_user():
        return {
            'login': 'kashekfjhkajsdhfkjhsdaf',
            'id': 789216,
            'password': 'fake_password'
        }

    @staticmethod
    def existing_user():
        return {
            'login': 'defunkt',
            'id': 2,
            'password': 'password'
        }

    @staticmethod
    def existing_user_from_env():
        return {
            'login': os.environ["EXISTING_GITHUB_USER_LOGIN"],
            'password': os.environ["EXISTING_GITHUB_USER_PASSWORD"]
            
        }


    @staticmethod
    def wordpress_existing_user():
        return {
            'name': 'Alex Wilhelm',
            'id': 428363,
            'password': 'password'
        }

    @staticmethod
    def wordpress_existing_user_from_env():
        return {
            'name': os.environ["EXISTING_WORDPRESS_USER_NAME"],
            'id': int(os.environ.get("EXISTING_WORDPRESS_USER_ID"))
        }

    @staticmethod
    def wordpress_my_user_from_env():
        return {
            'login': os.environ["MY_WORDPRESS_LOGIN"],
            'password': os.environ["MY_WORDPRESS_PASSWORD"],
            #'name': os.environ["MY_WORDPRESS_NAME"],
            #'id': int(os.environ.get("MY_WORDPRESS_USER_ID"))
        }