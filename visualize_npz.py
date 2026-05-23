import numpy as np
import matplotlib
matplotlib.use('TkAgg')   # Prevents Qt backend freezing

import matplotlib.pyplot as plt

# =========================================================
# CONFIGURATION
# =========================================================

# Path to NPZ file
FILE_PATH = "MI(1).npz"

# Set lead name like "I", "II", "aVR", "V1"
# Set to None to plot all leads
TARGET_LEAD = "II"

# Number of samples to display
MAX_SAMPLES = 5000


# =========================================================
# ECG PLOTTING FUNCTION
# =========================================================

def plot_ecg_npz():

    # -----------------------------
    # Load NPZ file
    # -----------------------------
    try:
        data = np.load(FILE_PATH)
    except FileNotFoundError:
        print(f"Error: '{FILE_PATH}' not found.")
        return
    except Exception as e:
        print("Error loading file:", e)
        return

    # -----------------------------
    # Get sampling rate
    # -----------------------------
    sampling_rate = data.get('sampling_rate', 500.0)

    # -----------------------------
    # Get lead names
    # -----------------------------
    lead_names = [k for k in data.keys() if k != 'sampling_rate']

    print(f"\nLoaded {len(lead_names)} leads from NPZ:")
    print(", ".join(lead_names))

    # -----------------------------
    # Create plot
    # -----------------------------
    fig, ax = plt.subplots(figsize=(15, 6))

    plotted_any = False

    # -----------------------------
    # Plot leads
    # -----------------------------
    for lead in lead_names:

        # Skip unwanted leads
        if TARGET_LEAD is not None and lead != TARGET_LEAD:
            continue

        signal = data[lead]

        # Keep only finite values
        signal = np.array(signal, dtype=np.float32)

        # Limit samples for smooth plotting
        signal = signal[:MAX_SAMPLES]

        # Create time axis
        time_array = np.arange(len(signal)) / sampling_rate

        # Plot signal
        ax.plot(
            time_array,
            signal,
            linewidth=1.2,
            label=f"Lead {lead}"
        )

        plotted_any = True

    # -----------------------------
    # Handle no lead found
    # -----------------------------
    if not plotted_any:
        print(f"\nLead '{TARGET_LEAD}' not found.")
        return

    # -----------------------------
    # Plot styling
    # -----------------------------
    ax.set_title(f"ECG Signal Plot ({TARGET_LEAD})")
    ax.set_xlabel("Time (seconds)")
    ax.set_ylabel("Amplitude")

    ax.grid(True, linestyle='--', alpha=0.5)

    ax.legend(loc="upper right")

    plt.tight_layout()

    # -----------------------------
    # Save image
    # -----------------------------
    output_file = "ecg_plot.png"

    plt.savefig(output_file, dpi=300)

    print(f"\nPlot saved as: {output_file}")

    # -----------------------------
    # Display plot
    # -----------------------------
    plt.show()


# =========================================================
# MAIN
# =========================================================

if __name__ == "__main__":
    plot_ecg_npz()