# Lab 03: Line and Circle Drawing Algorithms

Course Code: IRE 404  
Course Title: Computer Graphics and Animation Sessional  
Department: Department of Internet of Things and Robotics Engineering (IRE)  
Faculty: Faculty of Cyber Physical System Engineering  
Institution: University of Frontier Technology, Bangladesh (UFTB)  

Author: Shahriar Alom Masud  
Student ID: 2201032  
Session: 2022-2023  
Instructor: Farzana Akter, Assistant Professor, Dept. of IRE, UFTB  

---

## Problem Statement & Objectives

In computer graphics, screen displays consist of a discrete grid of integer pixels. Continuous primitive geometry (such as straight lines and circles) must undergo scan conversion (rasterization) to determine the optimal set of discrete pixels to illuminate.

### Objectives:
1. Implement **DDA (Digital Differential Analyzer)** line drawing algorithm based on differential slope increments.
2. Implement **Bresenham's Line Drawing Algorithm** using pure integer arithmetic and incremental decision parameters ($p$).
3. Implement **Mid-Point Circle Drawing Algorithm** utilizing 8-way octant symmetry and midpoint error evaluation.
4. Visualize discrete pixel rasterization alongside continuous ideal shapes using `matplotlib`.

---

## Implemented Algorithms

| Algorithm | Source Script | Mathematical Basis | Output Preview |
| :--- | :---: | :--- | :---: |
| **DDA Line Drawing** | [`dda.py`](dda.py) | $\Delta x, \Delta y$, $\text{steps} = \max(\|\Delta x\|, \|\Delta y\|)$, float increments with $\text{round}()$ | [View](screenshots/dda_output.png) |
| **Bresenham's Line** | [`bresenham.py`](bresenham.py) | Decision parameter $p_0 = 2\Delta y - \Delta x$, pure integer additions and bit-shifts | [View](screenshots/bresenham_output.png) |
| **Mid-Point Circle** | [`midpoint_circle.py`](midpoint_circle.py) | Decision parameter $p_0 = 1 - r$, 8-way octant symmetry reflection | [View](screenshots/midpoint_circle_output.png) |

---

## Project Structure

```text
Lab_03/
├── dda.py                    # DDA Line Drawing implementation
├── bresenham.py              # Bresenham's Line Drawing implementation
├── midpoint_circle.py        # Mid-Point Circle Drawing implementation
├── screenshots/              # Generated rasterization plots
│   ├── dda_output.png
│   ├── bresenham_output.png
│   └── midpoint_circle_output.png
└── README.md
```

---

## Running the Code

Execute any algorithm script using Python:

```bash
# 1. DDA Line Drawing
python3 dda.py

# 2. Bresenham's Line Drawing
python3 bresenham.py

# 3. Mid-Point Circle Drawing
python3 midpoint_circle.py
```
> Each script prompts for custom coordinate / radius inputs or falls back to default demonstration values if Enter is pressed.
