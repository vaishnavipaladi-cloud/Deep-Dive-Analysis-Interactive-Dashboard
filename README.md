# Task 3 - Deep-Dive Analysis & Interactive Dashboard

## Objective
To answer complex business problems by performing deep-dive analysis and building an interactive dashboard.

## Dataset
- **File:** Customer_sales_dataset_EDA.xlsx
- **Records:** 150 customers
- **Columns:** Customer_ID, Name, Gender, City, Product, Category, Quantity, Unit_Price, Total_Sales, Purchase_Date

## Core KPIs Defined
| KPI | Formula |
|-----|---------|
| Total Revenue | SUM(Total_Sales) |
| Average Order Value | Total_Sales / No. of Orders |
| Revenue by Category | Sales per Category / Total Sales × 100 |
| Revenue by City | SUM(Total_Sales) grouped by City |
| Top Product | Product with highest Total_Sales |

## Deep-Dive Analysis
- Revenue breakdown by Category, City, Product
- Monthly Revenue Trend
- Gender-wise Revenue split
- Customer Segmentation by Spend Level

## Interactive Dashboard
Built using **Plotly Dash** in Python.

### How to Run
```bash
pip install pandas matplotlib seaborn plotly dash openpyxl
python dashboard.py
```
Open browser and go to: http://127.0.0.1:8050

## Tools Used
- Python
- Pandas
- Plotly Dash
- VS Code
