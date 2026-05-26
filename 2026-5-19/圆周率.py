import math
import warnings
warnings.filterwarnings("ignore", message="Could not import the lzma module")

import numpy as np
import matplotlib.pyplot as plt

def pi_approx(n):
    """π_n = n * sin(π/n)"""
    return n * math.sin(math.pi / n)

def main():
    k_values = range(9)
    n_values = [2**k for k in k_values]
    h_values = [1.0 / n for n in n_values]
    exact_pi = math.pi

    print("=" * 70)
    print("Approximation of π using π_n = n·sin(π/n)  (n = 2^k)")
    print("=" * 70)
    print(f"{'k':<3} {'n':<8} {'h=1/n':<12} {'π_n':<22} {'Absolute error':<12}")
    print("-" * 70)

    errors = []
    for k, n, h in zip(k_values, n_values, h_values):
        pi_n = pi_approx(n)
        err = abs(pi_n - exact_pi)
        errors.append(err)
        print(f"{k:<3} {n:<8} {h:<12.6e} {pi_n:<22.15f} {err:<12.2e}")

    # Fit convergence order: log(error) ~ slope * log(h) + intercept
    coeffs = np.polyfit(np.log(h_values[1:]), np.log(errors[1:]), 1)
    slope = coeffs[0]
    intercept = coeffs[1]
    conv_order = abs(slope)

    # Plot
    plt.figure(figsize=(8, 5))
    plt.loglog(h_values, errors, 'o-', linewidth=2, markersize=8, label='Numerical error')

    # Theoretical error line: e_n ≈ (π^3/6) * h^2
    C_theory = math.pi**3 / 6.0
    theory_errors = [C_theory * (h**2) for h in h_values]
    plt.loglog(h_values, theory_errors, '--', linewidth=1.5,
               label=r'Theoretical: $e_n \approx \frac{\pi^3}{3!} h^2$', alpha=0.8)

    # Add text box with fitted convergence order
    text_str = f'Fitted convergence order ≈ {conv_order:.3f}\n(Theoretical = 2)'
    plt.text(0.05, 0.9, text_str, transform=plt.gca().transAxes,
             fontsize=12, bbox=dict(facecolor='white', alpha=0.8, edgecolor='gray'))

    plt.xlabel(r'$h = 1/n$', fontsize=12)
    plt.ylabel('Absolute error $|\pi_n - \pi|$', fontsize=12)

    plt.grid(True, which='both', linestyle='--', alpha=0.5)
    plt.legend()

    plt.tight_layout()
    plt.savefig('pi_errors_h.png', dpi=150)
    print("\nFigure saved as pi_errors_h.png")
    plt.show()

    print(f"\nFitted log(error) ≈ {intercept:.2f} + {slope:.2f}·log(h)")
    print(f"Convergence order ≈ {conv_order:.3f} (theoretical = 2)")

if __name__ == "__main__":
    main()