class Size:
    """ Object size, specifiy either height and width, or square """
    def __init__(self, height=1, width=1, square=1):
        self.height = height
        self.width = width
        self.square = square