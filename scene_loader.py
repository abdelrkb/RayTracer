from classes.math3d.vector import Vector
from classes.objects.sphere import Sphere
from classes.objects.color import Color
from classes.render.light import AmbientLight, PointLight, DirectionalLight
import os

def charger_scene(chemin):
    scenes = []
    gif = False

    scene_actuelle = {
        "camera": None,
        "lights": [],
        "spheres": []
    }

    with open(chemin) as f:
        for ligne in f:
            ligne = ligne.strip()
            if not ligne or ligne.startswith("#"):
                continue

            if ligne.startswith("GIF="):
                gif = ligne.split("=")[1].upper() == "TRUE"
                continue

            if ligne.startswith("---"):
                if scene_actuelle["camera"] is not None:
                    scenes.append(scene_actuelle)
                scene_actuelle = {"camera": None, "lights": [], "spheres": []}
                continue

            elements = ligne.split()
            type_objet = elements[0].lower()

            if type_objet == "camera":
                scene_actuelle["camera"] = Vector(float(elements[1]), float(elements[2]), float(elements[3]))
            elif type_objet == "ambient":
                scene_actuelle["lights"].append(AmbientLight(float(elements[1])))
            elif type_objet == "point":
                scene_actuelle["lights"].append(
                    PointLight(float(elements[1]), Vector(float(elements[2]), float(elements[3]), float(elements[4])))
                )
            elif type_objet == "directional":
                scene_actuelle["lights"].append(
                    DirectionalLight(float(elements[1]), Vector(float(elements[2]), float(elements[3]), float(elements[4])))
                )
            elif type_objet == "sphere":
                scene_actuelle["spheres"].append(
                    Sphere(
                        Vector(float(elements[1]), float(elements[2]), float(elements[3])),
                        float(elements[4]),
                        Color(int(elements[5]), int(elements[6]), int(elements[7])),
                        specular=int(elements[8]),
                        reflective=float(elements[9])
                    )
                )

        if scene_actuelle["camera"] is not None:
            scenes.append(scene_actuelle)

    return gif, scenes

def choisir_scene(dossier_scenes="scenes"):
    scenes = [f for f in os.listdir(dossier_scenes) if f.endswith(".txt")]
    if not scenes:
        raise RuntimeError("Aucune scene trouvée  dans 'scenes/'")

    print("\nScenes  dispos:\n")
    for i, scene in enumerate(scenes):
        print(f"  [{i}]  {scene}")
    print()

    while True:
        try:
            choix = int(input("Choisis  une scene: "))
            if 0 <= choix < len(scenes):
                return os.path.join(dossier_scenes, scenes[choix])
        except ValueError:
            pass
        print("Invalide.\n")