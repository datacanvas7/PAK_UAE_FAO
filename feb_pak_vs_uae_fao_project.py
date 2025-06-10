# %% [markdown]
# ## Food and Agriculture Organization of United Nations
# ### This project analyzes various parameters comparing Pakistan and UAE data.
# ### i- Demographics - Rural vs Urban Population

# %%
#import libraries
import pandas as pd
import numpy as np
import plotly.express as px

# %%
#load dataset
uae_data = pd.read_csv(r"F:\Courses-Learning\Codanics-Data Science\datasets_practice\uae_ruralvsurban_FAOSTAT_data_en_2-25-2025.csv")
pak_data = pd.read_csv(r"F:\Courses-Learning\Codanics-Data Science\datasets_practice\pak_ruralvsurban_FAOSTAT_data_en_2-25-2025.csv")

# %%
#Preview the dataset
print("UAE Data Preview:")
display(uae_data.head())

print("\nPakistan Data Preview:")
display(pak_data.head())

# %%
#Check column name and data types
print("UAE Columns:", uae_data.columns)
print("\nPakistan Columns:", pak_data.columns)

print("\nUAE Data Types:\n", uae_data.dtypes)
print("\nPakistan Data Types:\n", pak_data.dtypes)

# %%
#Check for missing values
print("Missing Values in UAE Data:\n", uae_data.isnull().sum())
print("\nMissing Values in Pakistan Data:\n", pak_data.isnull().sum())

# %%
#Summary Statistics
print("UAE Data Summary:")
display(uae_data.describe())

print("\nPakistan Data Summary:")
display(pak_data.describe())

# %% [markdown]
# ---
# ## Combining datasets

# %%
# Combine datasets for comparison
pak_data["Country"] = "Pakistan"
uae_data["Country"] = "UAE"
df = pd.concat([pak_data, uae_data])

# %% [markdown]
# ## 1-Line Chart: Urban vs. Rural Population Trends Over Time

# %%
# Create interactive line chart
fig = px.line(df, x="Year", y="Value", color="Element",
              line_dash="Country", markers=True,
              title="Urban vs. Rural Population Growth (Pakistan vs UAE)",
              labels={"Value": "Population (Thousands)", "Year": "Year"},
              hover_data=["Country", "Element"])
fig.show()

# %% [markdown]
# ## 2-Stacked Area Chart: Urbanization Trends

# %%
fig = px.area(df, x="Year", y="Value", color="Element", facet_col="Country",
              title="Urbanization Trends in Pakistan & UAE",
              labels={"Value": "Population (Thousands)", "Year": "Year"})

fig.show()

# %% [markdown]
# ## 3- Bar Chart: Rural vs Urban Population for a Given Year

# %%
year_selected = 2016  # Change to any year you want
df_selected = df[df["Year"] == year_selected]

fig = px.bar(df_selected, x="Element", y="Value", color="Country",
             barmode="group",
             title=f"Rural vs. Urban Population in {year_selected}",
             labels={"Value": "Population (Thousands)", "Element": "Population Type"})

fig.show()


# %% [markdown]
# ## 4-Line Chart: Population Growth Rate Over Time

# %%
df["Growth_Rate"] = df.groupby(["Country", "Element"])["Value"].pct_change() * 100

fig = px.line(df, x="Year", y="Growth_Rate", color="Element",
              line_dash="Country", markers=True,
              title="Annual Population Growth Rate (Pakistan vs UAE)",
              labels={"Growth_Rate": "Growth Rate (%)", "Year": "Year"})

fig.show()


# %% [markdown]
# ---

# %% [markdown]
# ## ii- Inputs - Fertilizers consumption in nutrients. 

# %%
#load dataset
uae_data = pd.read_csv(r"F:\Courses-Learning\Codanics-Data Science\datasets_practice\uae_fertilizers_FAOSTAT_data_en_2-25-2025.csv")
pak_data = pd.read_csv(r"F:\Courses-Learning\Codanics-Data Science\datasets_practice\pak_fertilizers_FAOSTAT_data_en_2-25-2025.csv")

# %%
#Preview the dataset
print("UAE Data Preview:")
display(uae_data.head())

print("\nPakistan Data Preview:")
display(pak_data.head())

# %%
#Check column name and data types
print("UAE Columns:", uae_data.columns)
print("\nPakistan Columns:", pak_data.columns)

print("\nUAE Data Types:\n", uae_data.dtypes)
print("\nPakistan Data Types:\n", pak_data.dtypes)

# %%
#Check for missing values
print("Missing Values in UAE Data:\n", uae_data.isnull().sum())
print("\nMissing Values in Pakistan Data:\n", pak_data.isnull().sum())

# %%
#Summary Statistics
print("UAE Data Summary:")
display(uae_data.describe())

print("\nPakistan Data Summary:")
display(pak_data.describe())

# %% [markdown]
# ## Combining datasets

# %%
# Combine datasets for comparison
pak_data["Country"] = "Pakistan"
uae_data["Country"] = "UAE"
df = pd.concat([pak_data, uae_data])

# %% [markdown]
# ### 1-Interactive Bar Chart – Fertilizer Consumption

# %%
fig = px.bar(df, x="Year", y="Value", color="Country",
             title="Total Fertilizer Consumption (Pakistan vs UAE)",
             labels={"Value": "Fertilizer Use (Tonnes)", "Year": "Year"},
             barmode="group")

fig.show()


# %% [markdown]
# # iii- Hunger and Food Security - No. of people undernourished (Millions) (3 year average)

# %%
#load dataset
uae_data = pd.read_csv(r"F:\Courses-Learning\Codanics-Data Science\datasets_practice\uae_hunger_FAOSTAT_data_en_2-25-2025.csv")
pak_data = pd.read_csv(r"F:\Courses-Learning\Codanics-Data Science\datasets_practice\pak_hunger_FAOSTAT_data_en_2-25-2025.csv")

# %%
#Preview the dataset
print("UAE Data Preview:")
display(uae_data.head())

print("\nPakistan Data Preview:")
display(pak_data.head())

# %%
#Check column name and data types
print("UAE Columns:", uae_data.columns)
print("\nPakistan Columns:", pak_data.columns)

print("\nUAE Data Types:\n", uae_data.dtypes)
print("\nPakistan Data Types:\n", pak_data.dtypes)

# %%
#Check for missing values
print("Missing Values in UAE Data:\n", uae_data.isnull().sum())
print("\nMissing Values in Pakistan Data:\n", pak_data.isnull().sum())

# %%
#Summary Statistics
print("UAE Data Summary:")
display(uae_data.describe())

print("\nPakistan Data Summary:")
display(pak_data.describe())

# %% [markdown]
# # Combining datasets

# %%
# Combine datasets for comparison
pak_data["Country"] = "Pakistan"
uae_data["Country"] = "UAE"
df = pd.concat([pak_data, uae_data])

# %% [markdown]
# # 01- Time Series Line Chart – Undernourishment Trend Over Time

# %%
import plotly.express as px

# Filter for a specific indicator (Modify as needed)
df_filtered = df[df['Item'].str.contains('undernourished', case=False, na=False)]

# Convert Year to string for proper plotting
df_filtered['Year'] = df_filtered['Year'].astype(str)

# Line Chart
fig = px.line(df_filtered, x='Year', y='Value', 
              title='Undernourishment Trend Over Time',
              labels={'Value': df_filtered['Unit'].iloc[0]},
              markers=True)

fig.show()

# %% [markdown]
# # 02- Bar Chart – Comparing Food Security Indicators in a Specific Year

# %%
# Select a specific year (Modify as needed)
year_selected = '2015-2017'
df_year = df[df['Year'] == year_selected]

# Bar Chart
fig = px.bar(df_year, x='Item', y='Value', 
             title=f'Food Security Indicators in {year_selected}',
             labels={'Value': 'Measurement'},
             text_auto=True)

fig.update_layout(xaxis_tickangle=-45)
fig.show()

# %% [markdown]
# # 03-Multi-Line Chart – Comparison of Multiple Indicators

# %%
fig = px.line(df, x='Year', y='Value', color='Item', 
              title='Comparison of Food Security Indicators Over Time',
              labels={'Value': 'Measurement'},
              markers=True)

fig.show()

# %% [markdown]
# # 04-Scatter Plot – Relationship Between Two Indicators

# %%
# Select two indicators (Modify as needed)
indicator_x = 'Number of people undernourished'
indicator_y = 'Prevalence of undernourishment'

df_scatter = df[df['Item'].str.contains(indicator_x, case=False, na=False)]
df_scatter_y = df[df['Item'].str.contains(indicator_y, case=False, na=False)]

# Merge both indicators on Year
df_merge = df_scatter.merge(df_scatter_y, on='Year', suffixes=('_X', '_Y'))

# Scatter Plot
fig = px.scatter(df_merge, x='Value_X', y='Value_Y', 
                 title=f'Relationship Between {indicator_x} and {indicator_y}',
                 labels={'Value_X': indicator_x, 'Value_Y': indicator_y})

fig.show()


# %% [markdown]
# # iv- Food Availablity - Average Protein supply (g/capita/day) (3 year average)

# %%
#load dataset
uae_data = pd.read_csv(r"F:\Courses-Learning\Codanics-Data Science\datasets_practice\uae_avg_protein_FAOSTAT_data_en_2-25-2025.csv")
pak_data = pd.read_csv(r"F:\Courses-Learning\Codanics-Data Science\datasets_practice\pak_avg_protein_FAOSTAT_data_en_2-25-2025.csv")

# %%
#Preview the dataset
print("UAE Data Preview:")
display(uae_data.head())

print("\nPakistan Data Preview:")
display(pak_data.head())

# %%
#Check column name and data types
print("UAE Columns:", uae_data.columns)
print("\nPakistan Columns:", pak_data.columns)

print("\nUAE Data Types:\n", uae_data.dtypes)
print("\nPakistan Data Types:\n", pak_data.dtypes)

# %%
#Check for missing values
print("Missing Values in UAE Data:\n", uae_data.isnull().sum())
print("\nMissing Values in Pakistan Data:\n", pak_data.isnull().sum())

# %% [markdown]
# # Combining datasets

# %%
# Combine datasets for comparison
pak_data["Country"] = "Pakistan"
uae_data["Country"] = "UAE"
df = pd.concat([pak_data, uae_data])

# %% [markdown]
# # 01-Time Series Line Chart – Protein Supply Trend Over Time

# %%
import plotly.express as px

# Convert Year to string for proper plotting
df_pakistan['Year'] = df_pakistan['Year'].astype(str)

# Line Chart
fig = px.line(df_pakistan, x='Year', y='Value', 
              title='Average Protein Supply Trend Over Time (Pakistan)',
              labels={'Value': df_pakistan['Unit'].iloc[0]},
              markers=True)

fig.show()

# %% [markdown]
# # 02-Bar Chart – Protein Supply in Different Years

# %%
# Bar Chart
fig = px.bar(df_pakistan, x='Year', y='Value', 
             title='Average Protein Supply in Different Years (Pakistan)',
             labels={'Value': 'Protein Supply (g/cap/day)'},
             text_auto=True)

fig.update_layout(xaxis_tickangle=-45)
fig.show()

# %%



