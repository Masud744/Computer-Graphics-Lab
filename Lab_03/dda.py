import os
import matplotlib.pyplot as plt


def dda(x1, y1, x2, y2):
    # 1. Calculate coordinate differences
    dx = x2 - x1
    dy = y2 - y1

    # 2. Number of steps needed
    steps = max(abs(dx), abs(dy))

    if steps == 0:
        return [x1], [y1]

    # 3. Calculate increment per step
    x_inc = dx / steps
    y_inc = dy / steps

    # 4. Starting coordinates
    x = x1
    y = y1

    x_points = []
    y_points = []

    print(f"\n{'Step':<6} {'x':<10} {'y':<10} {'Plotted Pixel (x, y)':<20}")
    print("-" * 50)

    for step in range(steps + 1):
        plot_x = round(x)
        plot_y = round(y)

        x_points.append(plot_x)
        y_points.append(plot_y)

        print(f"{step:<6} {x:<10.2f} {y:<10.2f} ({plot_x}, {plot_y})")

        x += x_inc
        y += y_inc

    return x_points, y_points


def plot_line(x_points, y_points, x1, y1, x2, y2):
    plt.figure(figsize=(8, 6))

    # Continuous ideal line
    plt.plot([x1, x2], [y1, y2], color="red", linestyle="--", label="Ideal Line")

    # Rasterized pixels
    plt.scatter(x_points, y_points, color="blue", s=70, zorder=5, label="Rasterized Pixels")

    # Labels and grid
    plt.title(f"DDA Line Drawing Algorithm: ({x1}, {y1}) to ({x2}, {y2})")
    plt.xlabel("X Coordinate")
    plt.ylabel("Y Coordinate")
    plt.grid(True, linestyle=":", alpha=0.6)
    plt.legend()
    plt.tight_layout()

    # Save output screenshot
    output_dir = os.path.join(os.path.dirname(__file__), "screenshots")
    os.makedirs(output_dir, exist_ok=True)
    save_path = os.path.join(output_dir, "dda_output.png")
    plt.savefig(save_path)
    print(f"\nGraph saved as '{save_path}'!")
    plt.show()


if __name__ == "__main__":
    print("--- DDA Line Drawing Algorithm ---")
    try:
        x1 = int(input("Enter x1 (default 2): ") or 2)
        y1 = int(input("Enter y1 (default 3): ") or 3)
        x2 = int(input("Enter x2 (default 12): ") or 12)
        y2 = int(input("Enter y2 (default 8): ") or 8)
    except ValueError:
        x1, y1, x2, y2 = 2, 3, 12, 8

    x_pts, y_pts = dda(x1, y1, x2, y2)
    plot_line(x_pts, y_pts, x1, y1, x2, y2)
