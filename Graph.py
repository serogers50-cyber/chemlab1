#This code produces the bar graph for the measurements lab
import matplotlib.pyplot as plt
import numpy as np

# -----------------------------
# DATA
# -----------------------------

masses = np.array([10.01, 19.71, 29.71, 39.19, 49.32])

# Volumes recorded to the tenths place for correct significant figures
volumes = np.array([10.0, 20.0, 30.0, 40.0, 50.0])

# Calculate density = mass / volume
densities = masses / volumes

# Values displayed above the bars
density_labels = ["1.001", "0.986", "0.991", "0.980", "0.986"]


# -----------------------------
# CALCULATE AVERAGE & STANDARD DEVIATION
# -----------------------------

average = densities.mean()

# Sample standard deviation
standard_deviation = densities.std(ddof=1)


# -----------------------------
# CREATE BAR GRAPH
# -----------------------------

measurements = [
    "Measurement 1",
    "Measurement 2",
    "Measurement 3",
    "Measurement 4",
    "Measurement 5"
]

x = np.arange(len(measurements))

# Different shades of blue
blue_shades = [
    "#B7D7F0",
    "#8FC1E3",
    "#6FAED6",
    "#4F96C6",
    "#2F7FB8"
]

fig, ax = plt.subplots(figsize=(11, 7))

bars = ax.bar(
    x,
    densities,
    width=0.65,
    color=blue_shades,
    edgecolor="#174A7E",
    linewidth=1.0,

    # Error bars = standard deviation
    yerr=standard_deviation,
    capsize=6,

    error_kw={
        "ecolor": "#17324D",
        "elinewidth": 1.3,
        "capthick": 1.3
    }
)


# -----------------------------
# AVERAGE DENSITY LINE
# -----------------------------

# ONE dotted line at the average density
ax.axhline(
    average,
    color="#1976D2",
    linestyle=":",
    linewidth=2.2,
    label=f"Average density = {average:.3f} ± "
          f"{standard_deviation:.3f} g/mL"
)


# -----------------------------
# REFERENCE DENSITY LINE
# -----------------------------

# Reference density of water
ax.axhline(
    1.00,
    color="#0B2E4F",
    linestyle="-",
    linewidth=2.2,
    label="Reference density = 1.00 g/mL"
)


# -----------------------------
# VALUES ABOVE EACH BAR
# -----------------------------

for bar, label in zip(bars, density_labels):

    ax.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + standard_deviation + 0.001,
        label,
        ha="center",
        va="bottom",
        fontsize=11
    )


# -----------------------------
# TITLES & AXIS LABELS
# -----------------------------

ax.set_title(
    "Density of water at 21°C obtained with a graduate cylinder.",
    fontsize=17,
    fontweight="bold",
    loc="center",
    pad=15
)

ax.set_xlabel(
    "Measurement",
    fontsize=13
)

ax.set_ylabel(
    "Density (g/mL)",
    fontsize=13
)


# -----------------------------
# X-AXIS LABELS
# -----------------------------

ax.set_xticks(x)

ax.set_xticklabels(
    measurements,
    fontsize=11
)


# -----------------------------
# Y-AXIS SETTINGS
# -----------------------------

ax.set_ylim(0.94, 1.045)

ax.set_yticks(
    np.arange(0.94, 1.041, 0.02)
)


# -----------------------------
# GRID
# -----------------------------

ax.grid(
    axis="y",
    alpha=0.25
)


# -----------------------------
# LEGEND
# -----------------------------

ax.legend(
    loc="upper right",
    fontsize=10,
    frameon=True
)


# -----------------------------
# DISPLAY GRAPH
# -----------------------------

plt.tight_layout()

plt.show()


# -----------------------------
# PRINT CALCULATIONS
# -----------------------------

print("Average density:", round(average, 3), "g/mL")
print(
    "Standard deviation:",
    round(standard_deviation, 3),
    "g/mL"
)