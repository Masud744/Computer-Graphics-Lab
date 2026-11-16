# Computer Graphics and Animation Lab (IRE 404)

Course: IRE 404 - Computer Graphics and Animation Sessional  
Department: Department of Internet of Things and Robotics Engineering (IRE)  
Faculty: Faculty of Cyber Physical System Engineering  
Institution: University of Frontier Technology, Bangladesh (UFTB)  

Student Name: Shahriar Alom Masud  
Student ID: 2201032  
Session: 2022-2023  
Instructor: Farzana Akter, Assistant Professor, Dept. of IRE, UFTB  

---

## Laboratory Modules

| Lab No. | Topic / Problem Statement | Technique / Implementation | Status | Report Link |
| :---: | :--- | :--- | :---: | :---: |
| Lab 02 | [Basic 2D Drawing with Turtle Graphics](#lab-02---basic-2d-drawing-with-turtle-graphics) | Python Turtle (2D Primitives, Color Occlusion, Rotational Transformations) | Completed | [2201032_Report_2.pdf](submission_report/2201032_Report_2.pdf) |
| Lab 03 | [Line & Circle Drawing Algorithms](Lab_03/) | DDA, Bresenham's Line, Mid-Point Circle Algorithm | Completed | - |
| Lab 04 | [3D Wireframe Modeling & Transformation](Lab_04/) | PyOpenGL, Pygame (3D Transformations, Perspective Projection) | Completed | [2201032_Report_4.pdf](Lab_04/submission_report/2201032_Report_4.pdf) |

---

## Lab 02 - Basic 2D Drawing with Turtle Graphics

| Task No. | Topic / Description | Source Code | Output Preview |
| :---: | :--- | :---: | :---: |
| Task 1 | **Smiling Face**: Face contour in black circle, eye blots, triangular nose, and red crescent smile via white-on-red color occlusion | [`task1.py`](task1.py) | [View](submission_report/screenshots/task1_output.png) |
| Task 2 | **Flag with 10:6 Ratio**: Green rectangular canvas with red circle shifted horizontally to $1/5$ of total length from left border | [`task2.py`](task2.py) | [View](submission_report/screenshots/task2_output.png) |
| Task 3 | **Overlapping Concentric Squares**: 8-pointed star shape synthesized by upright square and $45^\circ$ rotated concentric square | [`task3.py`](task3.py) | [View](submission_report/screenshots/task3_output.png) |
| Task 4 | **Rotated Squares Pattern**: 5 squares pivoted at a common corner vertex using $72^\circ$ angular increments ($C_5$ rotational symmetry) | [`task4.py`](task4.py) | [View](submission_report/screenshots/task4_output.png) |

---

## Environment & Requirements

- Python 3.10+
- Libraries & Packages:
  - `pygame` (`pip install pygame`)
  - `PyOpenGL` (`pip install PyOpenGL PyOpenGL_accelerate`)
  - `matplotlib` (`pip install matplotlib`)
  - `turtle` (Standard Library)
  - `tkinter` (`sudo apt install python3-tk`)
- LaTeX (for report generation):
  - `pdflatex` (`texlive-latex-base`, `texlive-latex-extra`, `texlive-pictures`)
  - `ghostscript` (`sudo apt install ghostscript`)

---

## How to Run

### Execute Individual Tasks
```bash
python3 task1.py
python3 task2.py
python3 task3.py
python3 task4.py
```

### Build Submission Report
```bash
cd submission_report
./build.sh
```

