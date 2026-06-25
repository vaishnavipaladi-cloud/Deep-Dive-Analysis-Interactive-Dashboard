
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel("Customer_sales_dataset_EDA.xlsx")
df['Purchase_Date'] = pd.to_datetime(df['Purchase_Date'])
df['Month'] = df['Purchase_Date'].dt.to_period('M')

# --- KPI 1: Total Revenue ---
print("Total Revenue:", df['Total_Sales'].sum())

# --- KPI 2: AOV ---
print("Average Order Value:", df['Total_Sales'].mean())

# --- KPI 3: Revenue by Category ---
cat_rev = df.groupby('Category')['Total_Sales'].sum().sort_values(ascending=False)
print(cat_rev)

# --- KPI 4: Revenue by City ---
city_rev = df.groupby('City')['Total_Sales'].sum().sort_values(ascending=False)
print(city_rev)

# KPI 5: Top Product
print("\nTop Product by Revenue:")
print(df.groupby('Product')['Total_Sales'].sum().sort_values(ascending=False))

# --- Segmentation Analysis (Deep-Dive) ---
# Segment customers by spend level
df['Spend_Segment'] = pd.cut(df['Total_Sales'],
    bins=[0, 30000, 80000, 150000, 300000],
    labels=['Low', 'Medium', 'High', 'Premium'])

seg = df.groupby('Spend_Segment', observed=True)['Customer_ID'].count()
print(seg)

# --- Plot 1: Revenue by Category ---
plt.figure(figsize=(8,5))
cat_rev.plot(kind='bar', color='steelblue')
plt.title('Revenue by Category')
plt.tight_layout()
plt.savefig('revenue_by_category.png')

# --- Plot 2: Revenue by City ---
plt.figure(figsize=(8,5))
city_rev.plot(kind='bar', color='coral')
plt.title('Revenue by City')
plt.tight_layout()
plt.savefig('revenue_by_city.png')

# --- Plot 3: Monthly Revenue Trend ---
monthly = df.groupby('Month')['Total_Sales'].sum()
plt.figure(figsize=(10,5))
monthly.plot(kind='line', marker='o')
plt.title('Monthly Revenue Trend')
plt.tight_layout()
plt.savefig('monthly_trend.png')

print("Charts saved!")