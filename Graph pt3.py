#This code produces the 3rd bar graph for the measurements lab
import numpy as np
import matplotlib.pyplot as plt

# Density data (g/cm^3)
densities = np.array([8.767, 8.732, 8.732, 8.767])

# Labels
labels = [
    "Measurement 1",
    "Measurement 2",
    "Measurement 3",
    "Measurement 4"
]

# Calculate mean and sample standard deviation
mean = np.mean(densities)
sd = np.std(densities, ddof=1)

# Display values using appropriate significant figures
mean_display = round(mean, 2)
sd_display = round(sd, 2)

# Create figure
plt.figure(figsize=(8, 5))

x = np.arange(len(densities))

# Pink color palette
pink_shades = [
    "#fbcfe8",
    "#f9a8d4",
    "#f472b6",
    "#ec4899"
]

# Bar graph with error bars
plt.bar(
    x,
    densities,
    color=pink_shades,
    yerr=[sd] * len(densities),
    capsize=5
)

# Average density line (dotted)
plt.axhline(
    mean,
    linestyle=":",
    linewidth=2,
    label=f"Average ± SD = {mean_display:.2f} ± {sd_display:.2f} g/cm³"
)

# Reference density line (solid)
plt.axhline(
    7.15,
    linestyle="-",
    linewidth=2,
    label="Reference Density = 7.15 g/cm³"
)

# Axis labels and title
plt.xticks(x, labels)
plt.xlabel("Measurements")
plt.ylabel("Density (g/cm³)")
plt.title("Density of a Penny Obtained with a Ruler")

# Legend
plt.legend(loc="best")

# Improve spacing
plt.tight_layout()

# Save figure (optional)
plt.savefig("density_penny_ruler.png", dpi=300)

# Display graph
plt.show()