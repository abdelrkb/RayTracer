from classes.math3d.vector import Vector
from classes.objects.sphere import Sphere
from classes.objects.color import Color
from classes.render.light import AmbientLight, PointLight, DirectionalLight

def load_scene_file(path: str):
    scenes = []
    gif = False

    scene_en_cours_de_rendu = {"camera": None,"lights": [],"spheres": []
    }

    with open(path) as f:
        for ligne in f:
            ligne = ligne.strip()
            if not ligne or ligne.startswith("#"):
                continue

            if ligne.startswith("GIF="):
                gif = ligne.split("=")[1].upper() == "TRUE"
                continue

            if ligne.startswith("---"):
                if scene_en_cours_de_rendu["camera"] is not None:
                    scenes.append(scene_en_cours_de_rendu)

                scene_en_cours_de_rendu = {"camera": None,"lights": [],"spheres": [] }
                continue

            tokens = ligne.split()
            kind = tokens[0].lower()

            if kind == "camera":
                scene_en_cours_de_rendu["camera"] = Vector(float(tokens[1]), float(tokens[2]), float(tokens[3]))

            elif kind == "ambient":
                scene_en_cours_de_rendu["lights"].append(AmbientLight(float(tokens[1])))

            elif kind == "point":
                scene_en_cours_de_rendu["lights"].append(
                    PointLight(float(tokens[1]),
                               Vector(float(tokens[2]), float(tokens[3]), float(tokens[4])))
                )

            elif kind == "directional":
                scene_en_cours_de_rendu["lights"].append(
                    DirectionalLight(float(tokens[1]),
                                     Vector(float(tokens[2]), float(tokens[3]), float(tokens[4])))
                )

            elif kind == "sphere":
                scene_en_cours_de_rendu["spheres"].append(
                    Sphere(
                        Vector(float(tokens[1]), float(tokens[2]), float(tokens[3])),
                        float(tokens[4]),
                        Color(int(tokens[5]), int(tokens[6]), int(tokens[7])),
                        specular=int(tokens[8]),
                        reflective=float(tokens[9])
                    )
                )

        if scene_en_cours_de_rendu["camera"] is not None:
            scenes.append(scene_en_cours_de_rendu)

    return gif, scenes

import os

def choose_scene(scene_dir="scenes") -> str:
    scenes = [
        f for f in os.listdir(scene_dir)
        if f.endswith(".txt")
    ]

    if not scenes:
        raise RuntimeError("No scene files found in 'scenes/'")

    print("\nAvailable scenes:\n")
    for i, scene in enumerate(scenes):
        print(f"  [{i}] {scene}")

    print()

    while True:
        try:
            choice = int(input("Select a scene number: "))
            if 0 <= choice < len(scenes):
                return os.path.join(scene_dir, scenes[choice])
        except ValueError:
            pass

        print("Invalid choice, try again.\n")
