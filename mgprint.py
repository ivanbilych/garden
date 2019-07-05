verbosity = False

def gprint(message):
    if verbosity:
        print(message)

def set_verbosity(value):
    global verbosity

    verbosity = value
