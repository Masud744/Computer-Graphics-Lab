import os
import matplotlib.pyplot as plt


def bresenham(x1, y1, x2, y2):
    # 1. Calculate differences and step directions
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    sx = 1 if x2 >= x1 else -1
    sy = 1 if y2 >= y1 else -1

    x, y = x1, y1
    x_points = []
    y_points = []

    # Case 1: Slope |m| <= 1 (gentle slope, stepping along x)
    if dx >= dy:
        p = 2 * dy - dx

        print(f"\n{'Step':<6} {'p':<8} {'Plotted Pixel (x, y)':<22}")
        print("-" * 40)

        for step in range(dx + 1):
            x_points.append(x)
            y_points.append(y)
            print(f"{step:<6} {p:<8} ({x}, {y})")

            x += sx
            if p < 0:
                p += 2 * dy
            else:
                y += sy
                p += 2 * dy - 2 * dx

    # Case 2: Slope |m| > 1 (steep slope, stepping along y)
    else:
        p = 2 * dx - dy

        print(f"\n{'Step':<6} {'p':<8} {'Plotted Pixel (x, y)':<22}")
        print("-" * 40)

        for step in range(dy + 1):
            x_points.append(x)
            y_points.append(y)
            print(f"{step:<6} {p:<8} ({x}, {y})")

            y += sy
            if p < 0:
                p += 2 * dx
            else:
                x += sx
                p += 2 * dx - 2 * dy

    return x_points, y_points


def plot_line(x_points, y_points, x1, y1, x2, y2):
    plt.figure(figsize=(8, 6))

    # Continuous ideal line
    plt.plot([x1, x2], [y1, y2], color="red", linestyle="--", label="Ideal Line")

    # Rasterized pixels
    plt.scatter(
        x_points,
        y_points,
        color="green",
        s=70,
        zorder=5,
        label="Bresenham Pixels",
    )

    plt.title(f"Bresenham's Line Algorithm: ({x1}, {y1}) to ({x2}, {y2})")
    plt.xlabel("X Coordinate")
    plt.ylabel("Y Coordinate")
    plt.grid(True, linestyle=":", alpha=0.6)
    plt.legend()
    plt.tight_layout()

    # Save output screenshot
    output_dir = os.path.join(os.path.dirname(__file__), "screenshots")
    os.makedirs(output_dir, exist_ok=True)
    save_path = os.path.join(output_dir, "bresenham_output.png")
    plt.savefig(save_path)
    print(f"\nGraph saved as '{save_path}'!")
    plt.show()


if __name__ == "__main__":
    print("--- Bresenham's Line Algorithm ---")
    try:
        x1 = int(input("Enter x1 (default 2): ") or 2)
        y1 = int(input("Enter y1 (default 3): ") or 3)
        x2 = int(input("Enter x2 (default 12): ") or 12)
        y2 = int(input("Enter y2 (default 8): ") or 8)
    except ValueError:
        x1, y1, x2, y2 = 2, 3, 12, 8

    x_pts, y_pts = bresenham(x1, y1, x2, y2)
    plot_line(x_pts, y_pts, x1, y1, x2, y2)
