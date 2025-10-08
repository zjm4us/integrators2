import numpy as np
import matplotlib.pyplot as plt
import subprocess

def run_ndcrescent(d, N, r1, r2, a):
    cmd = f"python ndcrescent.py {d} {N} {r1} {r2} {a}"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    lines = result.stdout.split('\n')
    vol_line = [line for line in lines if "Estimated Crescent Volume" in line]
    err_line = [line for line in lines if "Statistical Uncertainty" in line]
    if vol_line and err_line:
        vol = float(vol_line[0].split('=')[1])
        err = float(err_line[0].split('=')[1])
        return vol, err
    else:
        print(f"Error parsing output for d={d}, N={N}")
        print(result.stdout)
        return None, None

def main():
    dims = [3, 5, 10]  # Now includes d = 10
    N_vals = [10**i for i in range(2, 7)]  # N = 1e2 to 1e6
    r1, r2, a = 1.0, 1.0, 0.5

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

    for d in dims:
        vols, errs, sqrtNs = [], [], []
        for N in N_vals:
            vol, err = run_ndcrescent(d, N, r1, r2, a)
            if vol is not None:
                vols.append(vol)
                errs.append(err)
                sqrtNs.append(np.sqrt(N))
        ax1.errorbar(sqrtNs, vols, yerr=errs, label=f'd={d}', marker='o', capsize=3)
        ax2.plot(sqrtNs, errs, label=f'd={d}', marker='o')

    ax1.set_ylabel('Volume ± Error')
    ax2.set_ylabel('Statistical Uncertainty')
    ax2.set_xlabel(r'$\sqrt{N}$')
    ax1.legend()
    ax2.legend()
    ax1.set_title('Crescent Volume Convergence')
    ax1.grid(True)
    ax2.grid(True)
    plt.tight_layout()
    plt.savefig("convergence.png")
    plt.show()

if __name__ == "__main__":
    main()

