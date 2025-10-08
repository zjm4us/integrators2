# integrators2

Starter code and examples for MC integration exercise.

See also:

  * https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.qmc.Sobol.html
  * https://root.cern.ch/doc/master/quasirandom_8C_source.html


# Monte Carlo Integration – PHYS 5630

This repo contains my code for Part 1 (5630 version) and Part 2 of the Monte Carlo integration assignment.

## Part 1 – Crescent Volume

- `ndcrescent.py` calculates the volume of the overlapping region (crescent) between two d-dimensional spheres using the stone-throwing method.
- The two spheres have radii r1 and r2, and centers offset by a along one axis.
- I used d = 3, 5, and 10 with r1 = r2 = 1.0 and a = 0.5.


## Convergence Plot

- `plot_convergence.py` runs the crescent volume calculation for different values of N and plots:
  - Volume vs sqrt(N)
  - Uncertainty vs sqrt(N)


## Part 2 – 5D Sphere Volume (3 Methods)

- `part2_5d_volume.py` estimates the volume of a 5D unit sphere using:
  1. Grid method
  2. Pseudo-random sampling
  3. Sobol quasi-random sampling


## Notes

- N goes from 1e2 to 1e6
- All radii are set to 1.0 and a = 0.5
- Sobol sequence is from `scipy.stats.qmc.Sobol`

