

# На функциях
def decorator(old_f):
    def inner(*args, **kwargs):
        print('two')
        return old_f(*args, **kwargs)

    return inner


@decorator
def old():
    print('one')


old = decorator(old)
old()
