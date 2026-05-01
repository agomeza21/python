def detect_pandas():
    try:
        import pandas
        print(f"[OK] pandas {pandas.__version__} - Data manipulation ready")
    except:
        print("pandas NO está instalada.")
        print("Para instalarla:")
        print("  pip install pandas")

def detect_numpy():
    try:
        import numpy as np
        print(f"[OK] numpy {np.__version__} - Numerical computation ready")
    except ImportError:
        print("numpy NO está instalada.")
        print("Para instalarla:")
        print("  pip install numpy")