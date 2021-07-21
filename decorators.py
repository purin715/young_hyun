def decorator(func):
    def decorated(width, height):
        if width >= 0 and height >= 0:
            return func(width, height)
        else:
            print("False")

    return decorated


def tri(width, height):
    return width * height / 2

def reg(width, height):
    return width * height