mydict = {};


def to_up(name):
    return name.upper()


def cached(func):
    def in_func(*args, **kwargs):
        value = mydict.get(args+tuple(sorted(kwargs.items())), "no value")
        if value == "no value":
            value = func(*args+tuple(sorted(kwargs.items())))
            mydict.update({args+tuple(sorted(kwargs.items())): value})
        return value

    return in_func


decorator = cached(to_up)
