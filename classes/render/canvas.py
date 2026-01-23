class Canvas:
    def __init__(self, width : int, height: int):
        self.width = width
        self.height = height
        self.pixels = [[(0,0,0) for i in range(width)] for j in range (height)]


    def put_pixel(self, x : int, y : int, color : tuple[int, int, int]): 
        canvas_x = x + self.width//2 
        canvas_y = self.height // 2 - y - 1

        if 0 <= canvas_x < self.width and 0 <= canvas_y < self.height :
            self.pixels[canvas_y][canvas_x] = color
