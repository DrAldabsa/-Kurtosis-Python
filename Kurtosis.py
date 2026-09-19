import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import kurtosis

# Set seed
np.random.seed(42)

n_samples = 1000

# Normal distribution

normal_data = np.random.normal(loc= 0, scale = 1, size= n_samples)

# Heavy_Tail
heavy_tail_data = np.random.standard_t(df = 3, size = n_samples)

# Light Tail
light_tail_data = np.random.uniform(low = -2, high = 2, size = n_samples)

# Combine into a DataFrame

df = pd.DataFrame(
    {
        "Normal_Distribution": normal_data,
        "Heavy_Tail": heavy_tail_data,
        "Light_Tail": light_tail_data
    }
)

# Calculate Kurtosis
kurt_normal = kurtosis(df["Normal_Distribution"], fisher = True)
kurt_heavy = kurtosis (df["Heavy_Tail"], fisher = True)
kurt_light = kurtosis (df["Light_Tail"], fisher = True)

print(f"Calculated Kurtosis")
print(f"1- Normal distribution: {kurt_normal: 4f} (Expect ~ 0)")
print(f"1- Heavy distribution: {kurt_heavy: 4f} (Expect > 0)")
print(f"1- Light distribution: {kurt_light: 4f} (Expect < 0)")

plt.figure(figsize= (12, 6))
sns.kdeplot(df["Normal_Distribution"], label= f"Normal", color = "green", linewidth = 2.5)
sns.kdeplot(df["Heavy_Tail"], label= f"Heavy", color = "red", linewidth = 2.5)
sns.kdeplot(df["Light_Tail"], label= f"Light", color = "blue", linewidth = 2.5)


# Styling the plot
plt.title("Visualizing Kurtosis: Tails and Peakedness ", fontsize = 14, fontweight= "bold")
plt.xlabel("Values")
plt.ylabel("Density")
plt.xlim(-5, 5)
plt.legend(fontsize = 10)
plt.grid(axis= "y", alpha= 0.3)

plt.tight_layout()
plt.show()
