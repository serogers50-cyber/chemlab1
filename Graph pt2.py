# This code produces the other bar graph for the measurements lab
import numpy as np
import matplotlib.pyplot as plt

# Density data (g/mL)
densities = np.array([0.9900, 0.9920, 0.9920, 0.9915, 0.9914])

# Labels
labels = [
    "Measurement 1",
    "Measurement 2",
    "Measurement 3",
    "Measurement 4",
    "Measurement 5"
]

# Calculate mean and sample standard deviation
mean = np.mean(densities)
sd = np.std(densities, ddof=1)

# Values displayed in legend using appropriate significant figures
mean_display = round(mean, 4)      # 0.9914
sd_display = round(sd, 4)          # 0.0008

# Create figure
plt.figure(figsize=(8, 5))

x = np.arange(len(densities))

# Purple color palette
purple_shades = [
    "#e9d5ff",
    "#d8b4fe",
    "#c084fc",
    "#a855f7",
    "#7e22ce"
]

# Bar graph with error bars
plt.bar(
    x,
    densities,
    color=purple_shades,
    yerr=[sd] * len(densities),
    capsize=5
)

# Average density line (dotted)
plt.axhline(
    mean,
    linestyle=":",
    linewidth=2,
    label=f"Average ± SD = {mean_display:.4f} ± {sd_display:.4f} g/mL"
)

# Reference density line (solid)
plt.axhline(
    1.000,
    linestyle="-",
    linewidth=2,
    label="Reference Density = 1.000 g/mL"
)

# Axis labels and title
plt.xticks(x, labels)
plt.xlabel("Measurements")
plt.ylabel("Density (g/mL)")
plt.title("Density of Water at 22 °C Obtained with Volumetric Pipette")

# Axis limits
plt.ylim(0.988, 1.003)

# Legend
plt.legend(loc="best")

# Improve spacing
plt.tight_layout()

# Save figure (optional)
plt.savefig("density_water_volumetric_pipette.png", dpi=300)

# Display graph
plt.show()