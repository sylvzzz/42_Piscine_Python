"""
loading.py - Matrix dependency loader and data analyser.
"""

import sys
import importlib


PACKAGES: dict[str, str] = {
    "pandas": "Data manipulation ready",
    "numpy": "Numerical computations ready",
    "matplotlib": "Visualization ready",
    "requests": "Network access ready",
}


def check_dependencies() -> dict[str, object]:
    """Check required packages and return loaded modules."""
    print("Checking dependencies:")
    loaded: dict[str, object] = {}
    missing: list[str] = []

    for name, role in PACKAGES.items():
        try:
            mod = importlib.import_module(name)
            version = getattr(mod, "__version__", "unknown")
            print(f"  [OK] {name} ({version}) - {role}")
            loaded[name] = mod
        except ImportError:
            print(f"  [MISSING] {name} - Install required")
            missing.append(name)

    if missing:
        print("\nInstall with pip:    pip install -r requirements.txt")
        print("Install with Poetry: poetry install")
        sys.exit(1)

    return loaded


def run_analysis(modules: dict[str, object]) -> None:
    """Generate matrix data, print stats, and save a plot."""
    np = modules["numpy"]
    pd = modules["pandas"]
    plt = importlib.import_module("matplotlib.pyplot")

    # simulate matrix data
    rng = np.random.default_rng(42)
    n = 1000
    signal = np.sin(np.linspace(0, 4 * np.pi, n)) + rng.normal(0, 0.2, n)
    df = pd.DataFrame({"cycle": np.arange(n), "signal": signal})

    print("\nAnalyzing Matrix data...")
    print(f"Processing {n} data points...")
    print(f"Average signal: {df['signal'].mean():.4f}")
    print(f"Max signal:     {df['signal'].max():.4f}")

    print("Generating visualization...")
    plt.figure(figsize=(10, 4))
    plt.plot(df["cycle"], df["signal"], color="green", linewidth=1.0)
    plt.title("Matrix Signal Analysis")
    plt.xlabel("Cycle")
    plt.ylabel("Signal")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("matrix_analysis.png", dpi=130)
    plt.close()
    print("Analysis complete! Results saved to: matrix_analysis.png")


def main() -> None:
    """Entry point."""
    print("LOADING STATUS: Loading programs...\n")
    modules = check_dependencies()
    print("\nDependency manager:")
    print("  pip    -> requirements.txt")
    print("  Poetry -> pyproject.toml (with lock file)")
    run_analysis(modules)


if __name__ == "__main__":
    main()
