from classes.math3d.vector import Vector
from classes.render.canvas import Canvas
from classes.render.viewport import Viewport
from classes.render.camera import Camera
from classes.render.tracer import Tracer
from classes.objects.sphere import Sphere
from classes.render.light import AmbientLight, PointLight, DirectionalLight


#config gambetta

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600

VIEWPORT_WIDTH = 1
VIEWPORT_HEIGHT = 1
PROJECTION_PLANE_D = 1

BACKGROUND_COLOR = (255, 255, 255)


#scene

spheres = [
    Sphere(Vector(0, -1, 3), 1, (255, 0, 0), specular=500),   # Rouge
    Sphere(Vector(2, 0, 4), 1, (0, 0, 255), specular=500),    # Bleu
    Sphere(Vector(-2, 0, 4), 1, (0, 255, 0), specular=10),   # Vert
    Sphere(Vector(0, -5001, 0), 5000, (255, 255, 0), specular=1000), #Sphere jaune "sol"
]

lights = [
    AmbientLight(0.2),
    PointLight(0.6, Vector(2, 1, 0),),
    DirectionalLight(0.2, Vector(1, 4, 4)),
]


#composants

canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
viewport = Viewport(VIEWPORT_WIDTH, VIEWPORT_HEIGHT, PROJECTION_PLANE_D)
camera = Camera(Vector(0, 0, 0), viewport)
tracer = Tracer(spheres,lights, BACKGROUND_COLOR)

#boucle

for x in range(-CANVAS_WIDTH // 2, CANVAS_WIDTH // 2):
    for y in range(-CANVAS_HEIGHT // 2, CANVAS_HEIGHT // 2):

        ray = camera.get_ray(canvas, x, y)
        color = tracer.trace_ray(ray, t_min=1, t_max=float('inf'))
        canvas.put_pixel(x, y, color)


#image ppm
def save_ppm(canvas, filename="output.ppm"):
    with open(filename, "w") as f:
        f.write(f"P3\n{canvas.width} {canvas.height}\n255\n")
        for row in canvas.pixels:
            for (r, g, b) in row:
                f.write(f"{r} {g} {b} ")
            f.write("\n")


save_ppm(canvas)