import importlib
import importlib.metadata
import sys


def check_package(name: str, description: str) -> bool:
    try:
        importlib.import_module(name)
        version = importlib.metadata.version(name)
        print(f"[OK] {name} {version} - {description}")
        return True
    except ImportError:
        print(f"[MISSING] {name} - Not installed")
        return False


def check_dependencies() -> bool:
    packages = [
        ("pandas", "Data manipulation ready"),
        ("numpy", "Numerical computation ready"),
        ("matplotlib", "Visualization ready")
    ]
    all_ok = True
    for name, description in packages:
        if not check_package(name, description):
            all_ok = False
    return all_ok


if __name__ == "__main__":
    print("")
    print("LOADING STATUS: Loading programs...")
    print("")
    print("Checking dependencies:")

    if not check_dependencies():
        print("")
        print("To install it whit pip:")
        print("  pip install -r requirements.txt")
        print("To install it whith Poetry:")
        print("  poetry install")
        sys.exit(1)

    print("")
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as mpl

    data = np.random.rand(1000)
    print("Analyzing Matrix data...")
    df = pd.DataFrame(data, columns=["matrix_signal"])
    print(f"Processing {len(df)} data points...")
    mpl.figure(figsize=(10, 6))
    mpl.plot(df["matrix_signal"])
    mpl.title("Matrix Signal Anaalysis")
    mpl.savefig("matrix_analysis.png")
    print("Generating visualization...")
    print("")
    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")
