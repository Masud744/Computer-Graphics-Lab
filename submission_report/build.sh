#!/bin/bash
# ==============================================================================
# 1-Click Build Script for Computer Graphics Lab Report
# ==============================================================================

set -e

# Change directory to where this script is located
cd "$(dirname "$0")"

echo "================================================="
echo " Building Computer Graphics Lab Report PDF..."
echo "================================================="

# Step 1: Update screenshots if needed (optional)
if [ "$1" == "--regen-screenshots" ]; then
    echo "[1/3] Re-generating task output screenshots..."
    python3 generate_screenshots.py
else
    echo "[1/3] Using existing screenshots in screenshots/ (pass --regen-screenshots to redraw)"
fi

# Step 2: Compile LaTeX with pdflatex
echo "[2/3] Compiling LaTeX document (main.tex)..."
pdflatex -interaction=nonstopmode main.tex > /dev/null
pdflatex -interaction=nonstopmode main.tex > /dev/null

# Step 3: Copy to final output and clean auxiliary files
cp main.pdf Lab_Report_2.pdf
rm -f *.aux *.log *.out

echo "[3/3] Done!"
echo "================================================="
echo " SUCCESS! Output generated:"
echo " -> $(pwd)/Lab_Report_2.pdf"
echo "================================================="
