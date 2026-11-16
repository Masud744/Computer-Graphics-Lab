#!/bin/bash
# ==============================================================================
# 1-Click Build Script for Computer Graphics Lab 4 Report
# ==============================================================================

set -e

cd "$(dirname "$0")"

echo "================================================="
echo " Building Computer Graphics Lab 4 Report PDF..."
echo "================================================="

# Compile LaTeX document with pdflatex
echo "[1/2] Compiling LaTeX document (main.tex)..."
pdflatex -interaction=nonstopmode main.tex > /dev/null
pdflatex -interaction=nonstopmode main.tex > /dev/null

# Copy to final report name and clean temporary build artifacts
echo "[2/2] Finalizing output PDF and cleaning artifacts..."
cp main.pdf 2201032_Report_4.pdf
rm -f *.aux *.log *.out

echo "================================================="
echo " SUCCESS! Output generated:"
echo " -> $(pwd)/2201032_Report_4.pdf"
echo "================================================="
