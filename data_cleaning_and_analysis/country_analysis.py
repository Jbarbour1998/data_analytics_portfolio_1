# %%

import matplotlib.pyplot as plt
import pandas as pd

# %% 

df = pd.read_excel("Data_for_EDA.xlsx", sheet_name="continent")
df
# %%
df.head(5)


# %%
subset = df[df["continent"].isin(["Asia", "Europe"])]

# %%

subset.head(5)

# %%

subset.to_excel("asia_euro_subset.xlsx", index=False)

# %%
# plot: GDP per capita vs life_expectancy

for region, data in subset.groupby("continent"):
    plt.scatter(data["gdp_per_Capita"], data["life_expectancy"], label=region)

plt.xlabel("GDP per Capita")
plt.ylabel("Life Expectancy")
plt.legend()
plt.show()
# %%
# plot: GDP per capita vs infant_mortality
for region, data in subset.groupby("continent"):
    plt.scatter(data["gdp_per_Capita"], data["infant_mortality"], label=region)

plt.xlabel("GDP per Capita")
plt.ylabel("Infant Mortality")
plt.legend()
plt.show()

# %%
# plot: gdp_growth vs gdp_per_Capita
for region, data in subset.groupby("continent"):
    plt.scatter(data["gdp_growth"], data["gdp_per_Capita"], label=region)

plt.xlabel("GDP growth")
plt.ylabel("GDP per Capita")
plt.legend()
plt.show()

# %%
# plot: population_growth vs urban_population_growth
for region, data in subset.groupby("continent"):
    plt.scatter(data["population_growth"], data["urban_population_growth"], label=region)

plt.xlabel("population growth")
plt.ylabel("urban_population_growth")
plt.legend()
plt.show()

# %%
# plot: export vs imports
for region, data in subset.groupby("continent"):
    plt.scatter(data["exp"], data["imp"], label=region)

plt.xlabel("export")
plt.ylabel("imports")
plt.legend()
plt.show()
# %%
