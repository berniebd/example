# encoding=utf-8
# Created by bernie on 5/21/16.
import inspect


def check_is_admin(f):
    def wrapper(*args, **kwargs):
        func_args = inspect.getcallargs(f, *args, **kwargs)
        if func_args.get('username') != 'admin':
            return 'This user is not Admin'
        return f(*args, **kwargs)

    return wrapper


class Store:
    _storage = dict()

    @check_is_admin
    def get_food(self, username, food):
        return 'successful get food'

    @check_is_admin
    def put_food(self, username, food):
        return 'successful put food'


if __name__ == '__main__':
    store = Store()
    print (store.put_food(username='admin', food='apple'))
    print (store.put_food(username='user', food='banana'))
    print (store.get_food(username='admin', food='apple'))
    print (store.get_food(username='user', food='apple'))

    print(store.get_food.__doc__)
