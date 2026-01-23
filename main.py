import os
import math
import imageio.v2 as imageio
from datetime import datetime
from classes.render.canvas import Canvas
from classes.render.viewport import Viewport
from classes.render.camera import Camera
from classes.render.tracer import Tracer
from scene_loader import load_scene_file, choose_scene

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600
VIEWPORT_WIDTH = 1
VIEWPORT_HEIGHT = 1
PROJECTION_PLANE_D = 1
RECURSION_DEPTH = 3

SCENE_TO_RENDER = choose_scene("scenes")

def save_ppm(canvas: Canvas, path: str ):
    with open(path, "w") as f:
        f.write(f"P3\n{canvas.width} {canvas.height}\n255\n")
        for col in canvas.pixels:
            for r, g, b in col: 
                f.write(f"{r} {g} {b} ")
            f.write("\n")

gif_enabled, scenes = load_scene_file(SCENE_TO_RENDER)
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

if not gif_enabled: 
    scene = scenes[0] 

    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT) 
    viewport = Viewport(VIEWPORT_WIDTH, VIEWPORT_HEIGHT, PROJECTION_PLANE_D)
    camera = Camera(scene["camera"], viewport) 
    tracer = Tracer(scene["spheres"], scene["lights"]) 

    for x in range(-CANVAS_WIDTH // 2, CANVAS_WIDTH // 2):  
        for y in range(-CANVAS_HEIGHT // 2, CANVAS_HEIGHT // 2): 
            ray = camera.recuperer_rayon(canvas, x, y) 
            color = tracer.trace_ray(ray, 1, float("inf"), RECURSION_DEPTH)
            canvas.colorier(x, y, color)
            if x % 100 == 0 and y == 0:
                print(f"Rendering line {x}")

    os.makedirs("outputs", exist_ok=True) 
    dir_output = f"outputs/dated/output_{timestamp}.ppm"
    save_ppm(canvas, dir_output) 

    print(f"Image generated in directory : {dir_output}")

else:
    dir_frames = f"frames/scene_{timestamp}"
    os.makedirs(dir_frames, exist_ok=True)

    frames =[]

    for i,scene in enumerate(scenes):
        print(f"Rendering the frame {i+1}/ {len(scenes)}")

        canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
        viewport = Viewport(VIEWPORT_WIDTH, VIEWPORT_HEIGHT, PROJECTION_PLANE_D)
        camera = Camera(scene["camera"], viewport)
        tracer = Tracer(scene["spheres"],scene["lights"])
        for x in range(-CANVAS_WIDTH // 2, CANVAS_WIDTH // 2):
            for y in range(-CANVAS_HEIGHT // 2, CANVAS_HEIGHT // 2):
                ray = camera.recuperer_rayon(canvas, x, y)
                color = tracer.trace_ray(ray, 1, float("inf"), RECURSION_DEPTH)
                canvas.colorier(x, y, color)
                if x % 100 == 0 and y == 0:
                    print(f"Frame {i+1}: line {x}")

        frame_path = f"{dir_frames}/frame_{i:03d}.ppm"
        save_ppm(canvas, frame_path)

        frames.append(imageio.imread(frame_path))
    os.makedirs("outputs", exist_ok=True)
    gif_path = f"outputs/dated/output_{timestamp}.gif"
    imageio.mimsave(gif_path, frames, duration=0.08)

    print(f"GIF was render in the directory : {gif_path}")

