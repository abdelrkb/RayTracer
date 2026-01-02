# 🟢 RayTracer — Educational Ray Tracing Engine (Python)

This project is a **simple educational ray tracing engine written in Python**, inspired by  
**Gabriel Gambetta – _Computer Graphics from Scratch_**.

The goal of this project is to **understand ray tracing fundamentals step by step**, focusing on clarity and architecture rather than performance or real-time rendering.

---

## ✨ Features

The engine currently supports:

- Ray casting from a camera through a viewport
- Spheres as renderable objects
- Ambient, point, and directional lights
- Diffuse lighting
- Specular reflections
- Hard shadows using shadow rays
- Clean object-oriented architecture
- PPM image output

---

## 🧠 Architecture Overview

The project is structured to clearly separate responsibilities:

### math3d
- `Vector`: 3D vector mathematics
- `Ray`: parametric ray representation

### render
- `Canvas`: pixel buffer
- `Viewport`: projection plane
- `Camera`: ray generation
- `Light`: lighting models
- `Tracer`: core ray tracing logic

### objects
- `Sphere`: geometric primitives
- `Color`: RGB Color
---

## 📸 Output

The renderer generates a **PPM image** (`output.ppm`).

## 🚀 How to Run

```bash
python main.py
```

## 📖 Reference
- Computer Graphics from Scratch — Gabriel Gambetta
https://gabrielgambetta.com/computer-graphics-from-scratch/

## 👤 Author
Made by REKKAB Abdelnour and ZEROUAL Ilyes.
