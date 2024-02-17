import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/walking_through_door_slowly.csv")

sns.lineplot(data=df, x="Time (s)", y="Distance (mm)")
plt.savefig("walking_through_door_slowly.png", dpi=300)