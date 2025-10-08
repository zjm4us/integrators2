import numpy as np
import sys

def volume_hypercube(d, r1, r2, a):
    # Determine bounding box (hypercube) that contains both spheres
    min_corner = min(0, a) - max(r1, r2)
    max_corner = max(0, a) + max(r1, r2)
    length = max_corner - min_corner
    return length ** d, min_corner, length

def is_in_sphere(point, center, radius):
    return np.sum((point - center)**2) <= radius**2

def main():
    if len(sys.argv) != 6:
        print("Usage: python ndcrescent.py d N r1 r2 a")
        sys.exit(1)

    d = int(sys.argv[1])
    N = int(sys.argv[2])
    r1 = float(sys.argv[3])
    r2 = float(sys.argv[4])
    a = float(sys.argv[5])

    if abs(a) >= min(r1, r2):
        print("Error: |a| must be less than min(r1, r2)")
        sys.exit(1)

    vol_cube, min_corner, length = volume_hypercube(d, r1, r2, a)

    # Generate N random points in the hypercube
    points = np.random.uniform(min_corner, min_corner + length, size=(N, d))

    center1 = np.zeros(d)
    center2 = np.zeros(d)
    center2[0] = a

    count_inside = 0
    for p in points:
        if is_in_sphere(p, center1, r1) and is_in_sphere(p, center2, r2):
            count_inside += 1

    p = count_inside / N
    volume_estimate = vol_cube * p
    uncertainty = vol_cube * np.sqrt(p * (1 - p) / N)

    print(f"Estimated Crescent Volume = {volume_estimate:.8f}")
    print(f"Statistical Uncertainty = {uncertainty:.8f}")

if __name__ == "__main__":
    main()

