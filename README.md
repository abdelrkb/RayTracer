# 🟢 RayTracer — Educational Ray Tracing Engine (Python)

This project is a **fully educational ray tracing engine written in Python**, inspired by  
**Gabriel Gambetta – _Computer Graphics from Scratch_**.

The goal is to **build a ray tracer step by step**, focusing on:
- mathematical correctness
- clean architecture
- readability
- extensibility

This is **not** a real-time renderer and **not optimized for performance** on purpose.

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
- Hard shadows using shadow rays
- Proper handling of self-shadowing using ε offset

### 🪞 Reflections
- Recursive reflections
- Per-object reflectivity
- Configurable recursion depth

### 🎬 Scenes & Animation
- Scenes described in **external `.txt` files**
- Support for:
  - **Static scenes**
  - **Multi-scene animations**
- Automatic **GIF generation** from multiple frames
- Frame-by-frame rendering pipeline

### 🎨 Output
- PPM image output
- Optional animated GIF output
- Timestamped outputs

---

## 🧠 Architecture Overview

The project is structured to clearly separate responsibilities.

### `math3d/`
- **Vector**  
  3D vector math (dot product, normalization, reflection, etc.)
- **Ray**  
  Parametric ray representation

### `objects/`
- **Sphere**  
  Renderable primitive with material properties
- **Color**  
  RGB color abstraction with clamping and scaling

### `render/`
- **Canvas**  
  Pixel buffer abstraction
- **Viewport**  
  Projection plane definition
- **Camera**  
  Ray generation logic
- **Light**
  - AmbientLight
  - PointLight
  - DirectionalLight
- **Tracer**  
  Core ray tracing engine:
  - intersections
  - lighting
  - shadows
  - reflections

### `scenes/`
- Human-readable scene description files (`.txt`)
- Support for:
  - static scenes
  - animated sequences using multiple scene blocks

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
ambient intensity
point intensity x y z
directional intensity dx dy dz
```

### Spheres
```txt
sphere x y z radius R G B specular reflective
```

## 🚀 How to Run

```bash
python main.py
```

## ⏱️ Performance Notes

- This renderer is CPU-only and written in pure Python

- Rendering may take tens of seconds depending on:

    - resolution
    - number of spheres
    - reflection depth
    - number of scenes (GIF)

This is expected behavior for an educational ray tracer.

## 📖 Reference
- Computer Graphics from Scratch — Gabriel Gambetta
https://gabrielgambetta.com/computer-graphics-from-scratch/

## 👤 Author
Made by REKKAB Abdelnour and ZEROUAL Ilyes.