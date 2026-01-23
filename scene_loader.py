from classes.math3d.vector import Vector
from classes.objects.sphere import Sphere
from classes.objects.color import Color
from classes.render.light import AmbientLight, PointLight, DirectionalLight
import os

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

            objets_scenes = ligne.split()
            types = objets_scenes[0].lower() 

            if types == "camera":
                scene_en_cours_de_rendu["camera"] = Vector(float(objets_scenes[1]), float(objets_scenes[2]), float(objets_scenes[3]))
            elif types == "ambient":
                scene_en_cours_de_rendu["lights"].append(AmbientLight(float(objets_scenes[1])))
            elif types == "point":
                scene_en_cours_de_rendu["lights"].append(PointLight(float(objets_scenes[1]),Vector(float(objets_scenes[2]), float(objets_scenes[3]), float(objets_scenes[4]))))
            elif types == "directional":
                scene_en_cours_de_rendu["lights"].append(DirectionalLight(float(objets_scenes[1]),Vector(float(objets_scenes[2]), float(objets_scenes[3]), float(objets_scenes[4]))))
            elif types == "sphere":
                scene_en_cours_de_rendu["spheres"].append(
                    Sphere(Vector(float(objets_scenes[1]), float(objets_scenes[2]), float(objets_scenes[3])),float(objets_scenes[4]),Color(int(objets_scenes[5]), int(objets_scenes[6]), int(objets_scenes[7])),specular=int(objets_scenes[8]),reflective=float(objets_scenes[9]) ) )

        if scene_en_cours_de_rendu["camera"] is not None: 
            scenes.append(scene_en_cours_de_rendu) 
    return gif, scenes

def choose_scene(scene_dir="scenes") -> str: 
    scenes = [ f for f in os.listdir(scene_dir) if f.endswith(".txt")]
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

        print("Invalidtry again.\n")
