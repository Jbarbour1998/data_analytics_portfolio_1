# %%

import matplotlib.pyplot as plt
import pandas as pd

# %% 

df = pd.read_excel("Data_for_EDA.xlsx", sheet_name="continent")
df
# %%
df.head(5)

# %%
dupes = df[df.duplicated()]
dupes

# %%
summary_stats = df.describe(include= "all")
summary_stats
# %%
