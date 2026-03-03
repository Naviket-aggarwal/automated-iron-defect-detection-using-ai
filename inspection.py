from config import MIN_WIDTH, MAX_WIDTH, MIN_HEIGHT, MAX_HEIGHT

def check_dimensions(width, height):
    if width is None or height is None:
        return "ERROR"

    if MIN_WIDTH <= width <= MAX_WIDTH and MIN_HEIGHT <= height <= MAX_HEIGHT:
        return "OK"
    else:
        return "NOT OK"