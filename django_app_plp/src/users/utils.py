
def user_directory_path(instance, filename):
    return 'user_{}/{}'.format(instance.user.id, filename)