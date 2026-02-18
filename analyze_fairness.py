import pandas as pd
import numpy as np

# Load data with demographics
df = pd.read_csv('seattle_with_demographics.csv')

print("=== FAIRNESS ANALYSIS ===\n")

# Compare predictions across demographic groups
majority_white = df[df['majority_minority'] == 0]
majority_minority = df[df['majority_minority'] == 1]

print("GROUP SIZES:")
print(f"Majority-white tracts: {len(majority_white)}")
print(f"Majority-minority tracts: {len(majority_minority)}")

print("\n=== PREDICTION RATES ===")
print(f"Majority-white predicted underserved: {majority_white['underserved'].sum()} ({majority_white['underserved'].mean():.1%})")
print(f"Majority-minority predicted underserved: {majority_minority['underserved'].sum()} ({majority_minority['underserved'].mean():.1%})")

print("\n=== AVERAGE FEATURES ===")
features = ['transit_stops', 'population', 'median_income', 'underserved_probability']

for feature in features:
    white_avg = majority_white[feature].mean()
    minority_avg = majority_minority[feature].mean()
    print(f"\n{feature}:")
    print(f"  Majority-white: {white_avg:.2f}")
    print(f"  Majority-minority: {minority_avg:.2f}")
    print(f"  Difference: {minority_avg - white_avg:.2f}")

# Fairness gap: difference in underserved rates
fairness_gap = majority_minority['underserved'].mean() - majority_white['underserved'].mean()
print(f"\n=== FAIRNESS GAP ===")
print(f"Underserved rate gap: {fairness_gap:.1%}")

if abs(fairness_gap) > 0.1:
    print("Significant disparity detected (>10% difference)")
else:
    print("Fairness gap is relatively small (<10% difference)")

# Statistical parity: Are both groups predicted underserved at similar rates?
print(f"\n=== DEMOGRAPHIC PARITY ===")
print(f"Statistical parity ratio: {majority_minority['underserved'].mean() / majority_white['underserved'].mean():.2f}")
print("(Ratio close to 1.0 indicates demographic parity)")
