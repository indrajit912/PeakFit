# run_analysis.py
# Author: Indrajit Ghosh
# Created On: May 21, 2025
# 
from peakfit.io import load_csv
from peakfit.analyzer import find_local_maxima
from peakfit.fitter import fit_spline
from peakfit.plotter import plot_maxima_and_fit

files = {
    "Normal Pile": "data/normal_pile.csv",
    "Under-reamed Pile": "data/under_reamed_pile.csv"
}

def main():
    label = ["Normal Pile", "Under-reamed Pile"]
    filename = ["normal_pile", "reamed_pile.png"]
    i = 0
    path = files[label[i]]

    df = load_csv(path)
    x_max, y_max = find_local_maxima(df, x_min=0.3)  # Adjust as needed

    fit_func = fit_spline(x_max, y_max, smooth_factor=1e-7)

    df = df[df['time'] >= 0.3].reset_index(drop=True)
    plot_maxima_and_fit(df, x_max, y_max, fit_func=fit_func, label=label[i], filename=filename[i])

if __name__ == '__main__':
    main()