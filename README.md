# 🟢 RayTracer — Educational Ray Tracing Engine (Python)

This project is a **fully educational ray tracing engine written in Python**, inspired by  
**Gabriel Gambetta – _Computer Graphics from Scratch_**.

The goal is to **build a ray tracer step by step**.

---

## ✨ Features

The engine currently supports:

### 🧩 Geometry
- Spheres as geometric primitives
- Infinite planes approximated using large spheres (floor, walls, ceiling)

### 📷 Camera & Projection
- Perspective camera
- Viewport-based ray generation
- Configurable canvas resolution

### 💡 Lighting
- Ambient light
- Point lights
- Directional lights
- Diffuse (Lambertian) lighting
- Specular highlights (Phong model)

### 🌑 Shadows
- Shadows 

### 🪞 Reflections
- Recursive reflections
- Configurable recursion depth

### 🎬 Scenes & Animation
- Scenes described in txt files
- Support for:
  - Static scene
  - Multiple scene for animated gif

### 🎨 Output
- PPPM Ilage
- Animated gif
---

## 🧠 Architecture Overview

Structured in seperated responsabilities

### `math3d/`
- **Vector**  
  3D vector math (scalaire product, normalization, etc.)
- **Ray**  
  Parametric ray representation

### `objects/`
- **Sphere**  
  Principal objects in raytracing
- **Color**  
  RGB color object

### `render/`
- **Canvas**  
  Canvas where we draw the scene
- **Viewport**  
  Projection of what we saw through the canvas
- **Camera**  
  Ray generation logic from the camera
- **Light**
  - AmbientLight
  - PointLight
  - DirectionalLight
- **Tracer**  
  Core engine:
  - intersections
  - lighting
  - shadows
  - reflections

### `scenes/`
-  scene description files (`.txt`)

### `scene_loader.py`
- Scene file parser
- Handles:
  - camera
  - lights
  - spheres
  - GIF/static mode

---

## 📝 Scene File Format (`.txt`)

Scenes are defined in plain text.

### Global flags
```txt
GIF=TRUE
SCENES=5
```

### Scene separator
```txt
--- SCENE 0 ---
```

### Camera
```txt
camera x y z
```

### Lights
```txt
ambient intensite_lumiere
point intensite_lumiere x y z
directional intensite_lumiere dx dy dz
```

### Spheres
```txt
sphere x y z radius R G B specular reflective
```

## 🚀 How to Run

```bash
#create a venv env 
python -m venv venv
source venv/bin/activate
pip install - requirements.txt
python main.py
```

## 📖 Reference
- Computer Graphics from Scratch — Gabriel Gambetta
https://gabrielgambetta.com/computer-graphics-from-scratch/

## 👤 Author
Made by REKKAB Abdelnour and ZEROUAL Ilyes.