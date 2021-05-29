from django.conf import settings

from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
User = get_user_model()



class EmailOrUsernameModelBackend(ModelBackend):
    """
    This is a ModelBacked that allows authentication with either a username or an email address.

    """


    def authenticate(self, request, username=None, password=None):
        # the username could be either one of the two

        print('1')

        if '@' in username:
            print('2')

            kwargs = {'email': username}
        else:
            print('3')

            kwargs = {'mobile_number': username}
        try:
            print('4')

            user = User.objects.get(**kwargs)
            if user.check_password(password):
                print('5')

                return user
        except User.DoesNotExist:
            print('6')

            return None

    def get_user(self, username):
        try:
            print('7')

            return User.objects.get(pk=username)
        except User.DoesNotExist:
            print('8')

            return None