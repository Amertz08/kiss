from functools import wraps


def config_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        ctx = args[0]
        if not ctx.obj['CONFIG_FILE']:
            print('Missing .kiss.yml or not in a project directory')
            exit(0)
        return f(*args, **kwargs)
    return decorator
