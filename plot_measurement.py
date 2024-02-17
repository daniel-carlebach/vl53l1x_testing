import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

for file in os.listdir("data"):
    if file.endswith(".csv"):
        df = pd.read_csv("data/" + file)
        sns.lineplot(data=df, x="Time (s)", y="Distance (mm)")
        plt.savefig("figures/" + file.removesuffix(".csv") + ".png", dpi=300)
        plt.clf()
