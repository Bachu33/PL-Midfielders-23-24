import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("premier-player-23-24.csv")

# Filter midfielders
midfielders = df[df["Pos"].str.contains("MF")]

# Sidebar options
sort_by = st.sidebar.selectbox("Sort midfielders by", [
    "Ast", "Ast_90", "xAG", "xAG_90", "npxG+xAG_90",
    "G+A_90", "PrgP", "PrgC", "PrgR", "xG_90"
])

top_n = st.sidebar.slider("Top N midfielders", min_value=5, max_value=30, value=10)

# Sort and select
top_midfielders = midfielders.sort_values(by=sort_by, ascending=False).head(top_n)

# Title
st.title("Premier League Midfielders Analysis (2023/24)")

# Display table
st.dataframe(top_midfielders[["Player", "Team", "Age", "Min", "Starts",
                              "Ast", "Ast_90", "xAG", "xAG_90", "npxG+xAG_90",
                              "G+A_90", "PrgP", "PrgC", "PrgR", "xG_90"]])

# Barplot
st.subheader(f"Top {top_n} Midfielders by {sort_by}")
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(data=top_midfielders, y="Player", x=sort_by, palette="viridis", ax=ax)
st.pyplot(fig)
