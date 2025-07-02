# analysis.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv('data/c02.csv')

# Quick look
print(df.head())
print(df.columns)
