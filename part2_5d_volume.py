import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import qmc
import math


def in_5d_sphere(points):
    return np.sum(points**2, axis=1) <= 1.0

def fixed_grid_volume(m):
    axes = np.linspace(-1, 1, m)
    grid = np.array(np.meshgrid(*([axes]*5), indexing='ij')).reshape(5, -1).T
    inside = in_5d_sphere(grid)
    vol_cube = (2)**5
    return vol_cube * np.sum(inside)/len(grid)

def pseudo_random_volume(N):
    points = np.random.uniform(-1, 1, size=(N, 5))
    inside = in_5d_sphere(points)
    vol_cube = 2**5
    return vol_cube * np.sum(inside)/N

def sobol_volume(N):
    sampler = qmc.Sobol(d=5, scramble=True)
    m = int(np.log2(N))
    points = sampler.random_base2(m=m)
    points = 2 * points - 1  # scale to [-1, 1]^5
    inside = in_5d_sphere(points)
    vol_cube = 2**5
    return vol_cube * np.sum(inside)/len(points)

def main():
    true_vol = (np.pi**(5/2)) / (math.gamma(5/2 + 1))
    print(f"True 5D Sphere Volume = {true_vol:.8f}")

    N_values = [2**i for i in range(5, 17)]  # N from 32 to 65536
    sqrtN = np.sqrt(N_values)

    fixed_errors, pseudo_errors, sobol_errors = [], [], []

    for N in N_values:
        m = int(round(N ** (1/5)))
        vol_fixed = fixed_grid_volume(m)
        vol_pseudo = pseudo_random_volume(N)
        vol_sobol = sobol_volume(N)

        fixed_errors.append(abs(vol_fixed - true_vol) / true_vol)
        pseudo_errors.append(abs(vol_pseudo - true_vol) / true_vol)
        sobol_errors.append(abs(vol_sobol - true_vol) / true_vol)

    # Plot
    plt.figure(figsize=(8, 6))
    plt.plot(sqrtN, fixed_errors, 'o-', label='Fixed Grid')
    plt.plot(sqrtN, pseudo_errors, 's-', label='Pseudo-random')
    plt.plot(sqrtN, sobol_errors, '^-', label='Sobol Quasi-random')
    plt.xlabel(r'$\sqrt{N}$')
    plt.ylabel('Relative Error')
    plt.title('Relative Error vs sqrt(N) for 5D Sphere Volume')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("methods.png")
    plt.show()

if __name__ == "__main__":
    main()

