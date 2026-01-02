class Canvas:
    """
    Represents the image plane where the image is stored

    The canvas is basically a 2D grid of pixels, width and height are expressed in pixel and each pixel
    stores an RGB color.

    The canvas coordinate system is centered, meaning (0,0) is the center of the canvas.
    +x increases to the right
    +y increases upward
    """
    def __init__(self, width : int, height: int):
        """
        Create a canvas.

        Args:
            width (int): canvas width in px
            height (int): canvas width in px
        """
        self.width = width
        self.height = height
        self.pixels = [[(0,0,0) for i in range(width)] for j in range (height)]


    def put_pixel(self, x : int, y : int, color : tuple[int, int, int]): 
        """
        Sets the color of a pixel in the canvas.

        Args:
            x (int): x coordinate
            y (int): y coordinate
            color( tuple[int, int, int]): RGB color (0-255)
        """
        canvas_x = x + self.width//2
        canvas_y = self.height // 2 - y - 1

        if 0 <= canvas_x < self.width and 0 <= canvas_y < self.height :
            self.pixels[canvas_y][canvas_x] = color
