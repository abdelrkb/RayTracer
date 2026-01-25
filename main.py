import os
import math
import imageio.v2 as imageio
from classes.render.canvas import Canvas
from classes.render.viewport import Viewport
from classes.render.camera import Camera
from classes.render.tracer import Tracer
from scene_loader import charger_scene, choisir_scene

# Config de base
LARGEUR_CANVAS = 800
HAUTEUR_CANVAS = 600
LARGEUR_VIEWPORT = 1
HAUTEUR_VIEWPORT = 1
PROJECTION_PLANE_D = 1
PROFONDEUR_RECURSION = 3

SCENE_A_RENDER = choisir_scene("scenes")

def sauvegarder_ppm(canvas, chemin):
    with open(chemin, "w") as f:
        f.write(f"P3\n{canvas.width} {canvas.height}\n255\n")
        for col in canvas.pixels:
            for r, g, b in col:
                f.write(f"{r} {g} {b} ")
            f.write("\n")

gif_actif, scenes = charger_scene(SCENE_A_RENDER)

nom_scene = os.path.splitext(os.path.basename(SCENE_A_RENDER))[0]

if not gif_actif:
    scene = scenes[0]

    print("Image entrain d'être  générée...")

    canvas = Canvas(LARGEUR_CANVAS, HAUTEUR_CANVAS)
    viewport = Viewport(LARGEUR_VIEWPORT, HAUTEUR_VIEWPORT, PROJECTION_PLANE_D)
    camera = Camera(scene["camera"], viewport)
    tracer = Tracer(scene["spheres"], scene["lights"])

    for x in range(-LARGEUR_CANVAS // 2, LARGEUR_CANVAS // 2):
        for y in range(-HAUTEUR_CANVAS // 2, HAUTEUR_CANVAS // 2):
            rayon = camera.recuperer_rayon(canvas, x, y)
            couleur = tracer.trace_ray(rayon, 1, float("inf"), PROFONDEUR_RECURSION)
            canvas.colorier(x, y, couleur)

    os.makedirs("outputs", exist_ok=True)
    chemin_sortie = f"outputs/{nom_scene}.ppm"
    sauvegarder_ppm(canvas, chemin_sortie)
    print(f"Image générée: {chemin_sortie}")

else:
    print("GIF entrain d'être  généré...")

    os.makedirs("images", exist_ok=True)
    images  = []

    for i, scene in enumerate(scenes):
        print(f"  Image  {i+1}/{len(scenes)}")

        canvas = Canvas(LARGEUR_CANVAS, HAUTEUR_CANVAS)
        viewport = Viewport(LARGEUR_VIEWPORT, HAUTEUR_VIEWPORT, PROJECTION_PLANE_D)
        camera = Camera(scene["camera"], viewport)
        tracer = Tracer(scene["spheres"], scene["lights"])

        for x in range(-LARGEUR_CANVAS // 2, LARGEUR_CANVAS // 2):
            for y in range(-HAUTEUR_CANVAS // 2, HAUTEUR_CANVAS // 2):
                rayon = camera.recuperer_rayon(canvas, x, y)
                couleur = tracer.trace_ray(rayon, 1, float("inf"), PROFONDEUR_RECURSION)
                canvas.colorier(x, y, couleur)

        chemin_image  = f"images/{nom_scene}_image_{i:03d}.ppm"
        sauvegarder_ppm(canvas, chemin_image)
        images.append(imageio.imread(chemin_image))

    os.makedirs("outputs", exist_ok=True)
    chemin_sortie = f"outputs/{nom_scene}.gif"
    imageio.mimsave(chemin_sortie, images, duration=0.08)
    print(f"GIF  créé: {chemin_sortie}")