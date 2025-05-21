# plotter.py
# Author: Indrajit Ghosh
# Created On: May 21, 2025
# 
import matplotlib.pyplot as plt
import numpy as np
import os

def plot_maxima_and_fit(df, x_max, y_max, fit_func=None, label='', filename="peak_fit_result.png", show=False):
    # Make sure output directory exists
    os.makedirs("output", exist_ok=True)

    # Create a larger figure
    plt.figure(figsize=(8, 5))

    # Plot original signal
    plt.plot(df['time'], df['amplitude'], color='steelblue', linewidth=1.2,
             label=f'Original ({label})', alpha=0.9)

    # Plot local maxima
    plt.plot(x_max, y_max, 'o', color='crimson', markersize=4,
             label=f'Local Maxima ({label})', alpha=0.8)

    # Draw vertical line at x = 0.3
    plt.axvline(x=0.3, color='black', linestyle='--', linewidth=1, label='x = 0.3 sec')

    # Optional fitted curve
    if fit_func:
        x_fit = np.linspace(min(x_max), max(x_max), 500)
        y_fit = fit_func(x_fit)
        plt.plot(x_fit, y_fit, color='darkgreen', linestyle='--', linewidth=1.2,
                 label=f'Fitted Curve ({label})', alpha=0.8)

    # Labels and legend
    plt.xlabel('Time (s)', fontsize=10)
    plt.ylabel('Amplitude', fontsize=10)
    plt.title(f'Local Maxima and Fitted Curve — {label}', fontsize=12)
    plt.legend(fontsize=8)
    plt.grid(True, linestyle=':', alpha=0.6)

    # Save the figure
    saved_path = f"output/{filename}"
    plt.tight_layout()
    plt.savefig(saved_path, dpi=300)
    print(f"✅ Plot saved to {saved_path}")

    if show:
        plt.show()

    plt.close()

