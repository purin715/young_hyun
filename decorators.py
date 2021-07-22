def decorator(func):
    def decorated(width, height):
        if width >= 0 and height >= 0:
            res = func(width, height)
            print(res)
        else:
            print("False")

    return decorated

@decorator
def tri(width, height):
    return width * height / 2

@decorator
def reg(width, height):
    return width * height

tri(2, 3)
reg(-1, 3)