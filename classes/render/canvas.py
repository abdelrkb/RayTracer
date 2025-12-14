class Canvas:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pixels = [[(0,0,0) for i in range(width)] for j in range (height)]


    def put_pixel(self, x, y, color): 

        canvas_x = x + self.width//2
        canvas_y = y + self.height//(2-y-1)

        if 0 <= canvas_x < self.width and 0 <= canvas_y < self.height :
            self.pixels[canvas_x][canvas_y] = color
