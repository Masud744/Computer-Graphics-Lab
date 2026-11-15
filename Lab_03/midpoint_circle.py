import os
import matplotlib.pyplot as plt


def get_symmetry_points(xc, yc, x, y):
    # Generates all 8 symmetric points from the 1st octant point (x, y)
    return [
        (xc + x, yc + y),
        (xc - x, yc + y),
        (xc + x, yc - y),
        (xc - x, yc - y),
        (xc + y, yc + x),
        (xc - y, yc + x),
        (xc + y, yc - x),
        (xc - y, yc - x),
    ]


def midpoint_circle(xc, yc, r):
    x = 0
    y = r
    p = 1 - r

    all_points = set()

    print(
        f"\n{'Step':<6} {'p':<8} {'(x, y)':<10} {'8-Symmetric Points (Octants)':<40}"
    )
    print("-" * 65)

    step = 0
    while x <= y:
        sym_points = get_symmetry_points(xc, yc, x, y)
        for pt in sym_points:
            all_points.add(pt)

        pts_str = ", ".join([f"({px},{py})" for px, py in sym_points[:4]])
        print(f"{step:<6} {p:<8} ({x}, {y})     {pts_str} ...")

        x += 1
        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * (x - y) + 1

        step += 1

    x_points = [pt[0] for pt in all_points]
    y_points = [pt[1] for pt in all_points]
    return x_points, y_points


def plot_circle(x_points, y_points, xc, yc, r):
    plt.figure(figsize=(7, 7))

    ideal_circle = plt.Circle(
        (xc, yc),
        r,
        color="red",
        fill=False,
        linestyle="--",
        label="Ideal Circle",
    )
    plt.gca().add_patch(ideal_circle)

    plt.scatter(
        x_points,
        y_points,
        color="purple",
        s=40,
        zorder=5,
        label="Midpoint Pixels",
    )
    plt.scatter([xc], [yc], color="black", s=60, marker="x", label="Center")

    plt.title(f"Mid-Point Circle Drawing Algorithm (Center: {xc},{yc}, r={r})")
    plt.xlabel("X Coordinate")
    plt.ylabel("Y Coordinate")
    plt.gca().set_aspect("equal", adjustable="box")
    plt.grid(True, linestyle=":", alpha=0.6)
    plt.legend()
    plt.tight_layout()

    # Save output screenshot
    output_dir = os.path.join(os.path.dirname(__file__), "screenshots")
    os.makedirs(output_dir, exist_ok=True)
    save_path = os.path.join(output_dir, "midpoint_circle_output.png")
    plt.savefig(save_path)
    print(f"\nGraph saved as '{save_path}'!")
    plt.show()


if __name__ == "__main__":
    print("--- Mid-Point Circle Drawing Algorithm ---")
    try:
        xc = int(input("Enter Center X xc (default 0): ") or 0)
        yc = int(input("Enter Center Y yc (default 0): ") or 0)
        r = int(input("Enter Radius r (default 15): ") or 15)
    except ValueError:
        xc, yc, r = 0, 0, 15

    x_pts, y_pts = midpoint_circle(xc, yc, r)
    plot_circle(x_pts, y_pts, xc, yc, r)
