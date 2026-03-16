# amazon-sales-ETL-analysis
ETL and Power BI dashboard project analyzing Amazon e-commerce sales data using Python, SQL and Power BI.
# Amazon E-Commerce Sales ETL & Power BI Dashboard

## 📊 Project Overview

This project analyzes Amazon e-commerce sales data using an **ETL pipeline built in Python** and an **interactive Power BI dashboard**.
The goal of this project is to extract, clean, transform, and visualize sales data to generate meaningful business insights.

The dashboard provides insights into:

* Overall sales performance
* Customer purchasing behavior
* Product performance and trends

---

## 🛠 Tools & Technologies

* **Python** (Pandas, NumPy)
* **Excel**
* **Power BI**
* **Git & GitHub**
* **SQL**

---

## ⚙️ ETL Process

The ETL pipeline follows three main stages:

### 1️⃣ Extract

Sales data is imported from the Excel dataset.

### 2️⃣ Transform

Data cleaning and transformation steps include:

* Removing null or invalid values
* Filtering valid order statuses
* Converting date columns to datetime format
* Creating derived columns for analysis

### 3️⃣ Load

The cleaned dataset is loaded into **Power BI** for visualization and dashboard creation.

---

## 📈 Key KPIs Created

The dashboard tracks important business metrics such as:

* **Total Revenue**
* **Total Quantity Sold**
* **Total Orders**
* **Average Order Value (AOV)**
* **Revenue per Order**
* **Average Items per Order**
* **Month-over-Month (MoM) Revenue Growth**

---



### 1️⃣ Sales Summary Dashboard

Provides a high-level overview of sales performance.

Key visuals:

* Revenue trend over time
* Revenue by category
* Revenue distribution by region
* Metro vs Non-Metro sales comparison

---

### 2️⃣ Customer Analysis Dashboard

Analyzes purchasing behavior and geographic distribution of customers.

Key insights:

* Orders by state
* Revenue by city tier
* B2B vs B2C revenue comparison
* Average items per order

---

### 3️⃣ Product Analysis Dashboard

Evaluates product performance and category trends.

Key insights:

* Revenue by category
* Quantity sold by category
* Top performing products
* Sales by product size

---

## 🗂 Project Structure

amazon-ecommerce-sales-analysis

data

* amazon_sales_report.xlsx
* amazon_sales_clean.xlsx

python_etl

* data_cleaning.py

powerbi_dashboard

* amazon-ecommerce-sales.pbix

dashboard_images

* sales_summary.png
* customer_analysis.png
* product_analysis.png

README.md
requirements.txt

---



---

## 📌 Key Insights

Some insights derived from the analysis include:

* Metro cities contribute a significant portion of total revenue.
* Certain product categories dominate total sales.
* Average order value indicates customers often purchase multiple items per order.
* Product size preferences vary across categories.

---

## 🚀 Future Improvements

Possible improvements for this project:

* Add customer segmentation analysis
* Build automated ETL pipelines
* Integrate real-time data sources
* Deploy dashboards to Power BI Service

---

## 👩‍💻 Author

**Shristi Tarar**

Aspiring Data Analyst passionate about data visualization, analytics, and building data-driven solutions.
