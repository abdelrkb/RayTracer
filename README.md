# RayTracer

Projet RayTracer inspiré par le livre de Gabriel Gambetta

## Architecture

Architecture modulaire.

### `math3d/`
- Vector 
  Vecteur 3D multiplication, scalaire ect...
- Ray  
  Representation de Ray

### `objects/`
- Sphere  
  Objets raytracing
- Color 
  Couleur RGB

### `render/`
- Canvas
  Canvas ou l'on dessine la scene
- Viewport
  Projection de ce que l'on voit
- Camera
  Position de la camera
- Light
  - AmbientLight
  - PointLight
  - DirectionalLight
- Tracer
  Algo principal gerant:
  - les intersections
  - les lumieres
  - les ombres
  - les reflexions

### `scenes/`
-  scene décris en txt

### `scene_loader.py`
- Charge les scenes


## 📝 Scenes

On decrit les scene en txt

Conventions  
```txt
GIF = FALSE

#sphere x y z radius R G B specular reflective

#lights : 
#point intensity x y z
#directional intensity dx dy dz
#ambient intensity

# Camera
camera x y z
```

## Comment lancer

```bash
#create a venv env 
python -m venv venv
source venv/bin/activate
pip install - requirements.txt
python main.py
```

## References
- Computer Graphics from Scratch — Gabriel Gambetta
https://gabrielgambetta.com/computer-graphics-from-scratch/

##  Auteurs
Fait par  REKKAB Abdelnour et ZEROUAL Ilyes.

##  Dependances

ImageIO==2.37.2
numpy==2.4.1
pillow==12.1.0