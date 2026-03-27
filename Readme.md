# 📊 Madhav E-Commerce Sales Dashboard

> **Freelance Data Analytics Project** delivering end-to-end business intelligence solutions for Madhav E-Commerce Store.

An interactive sales analytics dashboard built using Python (Plotly/Dash) and Power BI to analyze e-commerce transaction data and deliver actionable business insights for Madhav E-Commerce Store.

## 💼 Project Background

This was a **freelance data analytics project** where I worked with Madhav E-Commerce Store to analyze their sales performance and build comprehensive dashboards for data-driven decision making.

This project demonstrates a complete data analytics workflow — from data acquisition and cleaning to exploratory analysis, static visualization, interactive dashboards, and business intelligence reporting. The analysis examines sales performance across categories, geographies, payment modes, and customer segments to identify growth opportunities and operational improvements.

**Key Responsibilities:**

- 📊 Created and structured the complete sales dataset from raw transaction data
- 🔍 Performed exploratory data analysis to identify business trends and patterns
- 📈 Developed static visualizations for presentation and reporting
- 💻 Built an interactive Python web dashboard using Plotly and Dash
- 📊 Created a professional Power BI dashboard for executive stakeholders
- 📝 Delivered actionable business recommendations based on data insights
- 🌐 Published the dataset to Kaggle for transparency and portfolio demonstration

### 🎯 Business Questions

- What are the monthly sales and profit trends?
- Which states generate the highest revenue?
- Which product categories perform best?
- Who are the top customers?
- What is the distribution of payment methods?
- Which sub-categories generate the most profit?

### 📦 Dataset

- **Source**: Custom dataset created and uploaded to Kaggle
- **Link**: [Madhav E-Commerce Sales Dataset on Kaggle](https://www.kaggle.com/datasets/amitkumar209/madhav-e-commerce-sales-dataset)
- **Tables**: Orders.csv (customer & transaction data) + Details.csv (product & line-item data)
- **Records**: 500+ transactions across multiple categories and states

### 🔗 Live Demo

- ****Interactive** Python Dashboard**: [View Demo](/images/GIF%20Interactive%20Dashboard.gif)
- **Power BI Dashboard**: [View Report](/Madhav%20E-Commerce%20Sales%20Dashboard.pbix)

---

## 🚀 Project Workflow

This project follows a complete data analysis pipeline:

<img alt="Workflow Image" src="/images/Workflow Image.png" height="400" align="left ">

**Step-by-Step Process:**

1. **Data Collection & Publication** 
   - Created comprehensive e-commerce sales dataset for Madhav Store
   - Structured data into two tables: `Orders.csv` (customer & order details) and `Details.csv` (line-item details)
   - Published dataset to Kaggle: [Madhav E-Commerce Sales Dataset](https://www.kaggle.com/datasets/amitkumar209/madhav-e-commerce-sales-dataset)
   - Implemented automated data acquisition using KaggleHub API

2. **Data Cleaning & Transformation**
   - Merged Orders and Details tables on `Order ID`
   - Converted date fields to datetime format
   - Extracted temporal features (month, quarter)
   - Handled missing values and data type conversions

3. **Exploratory Data Analysis**
   - Calculated key metrics (revenue, profit, quantity, AOV)
   - Analyzed trends across time, geography, and categories
   - Identified top customers and payment patterns

4. **Static Dashboard** 
   - Created publication-ready visualizations using Matplotlib and Seaborn
   - 6-panel dashboard with KPIs, trends, and distributions

5. **Interactive Dashboard**
   - Built web-based dashboard using Plotly and Dash
   - Implemented dynamic filters (category, quarter)
   - Created responsive layouts with callback functions

6. **Power BI Dashboard**
   - Designed professional BI dashboard with Power BI Desktop
   - Implemented slicers, cross-filtering, and drill-through capabilities
   - Published to Power BI Service for sharing

## 📁 Project Structure

```
Madhav-Ecommerce-Sales-Dashboard/
│
├── Madhav_E-Commerce_Sales_Analysis.ipynb      # Complete data analysis & static dashboard
├── madhav_sales_dashboard.py                   # Interactive Dash application
├── Power_BI_Dashboard_Image.png                # Power BI dashboard screenshot
├── Python_Dashboard_Image.png                  # Python dashboard screenshot
├── README.md                                   # Project documentation
└── requirements.txt                            # Python dependencies
```

---

## 🛠️ Tools & Technologies

### Programming

- Python

### Libraries

- Pandas → Data cleaning & analysis  
- NumPy → Data processing  
- Matplotlib → Static visualizations  
- Seaborn → Advanced visualizations  
- Plotly → Interactive charts  
- Dash → Web-based interactive dashboard  

### BI Tool

- Power BI → Business dashboard

### Other Tools

- Jupyter Notebook  
- VS Code  
- Git & GitHub  

---

## 📊 Dashboards

### 1️⃣ Power BI Dashboard

Professional business intelligence dashboard with drill-down capabilities and cross-filtering.

![Power BI Dashboard](/images/Power%20BI%20Dashboard%20Image.png)

**Key Features:**

- Interactive quarter and category filters
- Real-time KPI cards (Revenue, Profit, Quantity, AOV)
- Geographic revenue distribution
- Temporal profit trends
- Payment mode analysis
- Customer segmentation

---

### 2️⃣ Python Interactive Dashboard (Plotly + Dash)

Web-based interactive dashboard with dynamic filtering and responsive design.

<img alt="Python Dashboard" src="/images/Python Dashboard Image.png" height="400" align="center">

**Key Features:**

- **Dynamic Filters**: Category and quarter-based filtering
- **Real-time Updates**: All visualizations update based on filter selections
- **KPI Indicators**: 
  - Total Revenue: ₹438K
  - Total Profit: ₹37K
  - Quantity Sold: 5,620 units
  - Average Order Value: ₹78
- **Interactive Charts**:
  - Monthly profit trends (bar chart)
  - Sub-category profitability (horizontal bar)
  - State-wise revenue distribution (percentage bars)
  - Category-wise quantity breakdown (pie chart)
  - Payment mode distribution (pie chart)
  - Top 5 customers by revenue (bar chart)

## 📈 Key Business Insights 🔍

1. **Business is profitable with healthy unit economics**
   - Total revenue is **₹437,771** and total profit is **₹36,963**.
   - Overall profit margin is **8.44%**.
   - Average revenue per unit sold is **₹77.96**.

2. **Sales are highly seasonal and volatile month-to-month**
   - **November** is the peak month with **₹61,632** revenue.
   - **May** is the weakest month with **₹12,966** revenue.

3. **Revenue is concentrated in a few states**
   - Top 3 states (Maharashtra, Madhya Pradesh, Uttar Pradesh) contribute **52.16%** of total revenue.
   - Top 5 states contribute **62.50%** of revenue.
   - Maharashtra alone is the largest market at **₹102,498**.

4. **Clothing is the volume engine**
   - Clothing contributes **63%** of total quantity sold.
   - Electronics contributes **21%** and Furniture **17%**.
   - This indicates dependence on one category for volume.

5. **Payment mix is dominated by COD**
   - COD accounts for **46%** of transactions.
   - UPI is second at **22%**.
   - High COD dependence can increase return, cancellation, and cash-flow risk.

## 🚀 Business Recommendations

### 🎯 Target Audience

- **Primary:** High-frequency **Clothing buyers** in core states (Clothing drives **63%** of total units sold).
- **Secondary:** Value-seeking buyers in **Electronics** and **Furniture** for cross-sell growth.

### 📍 Target Locations

#### 🔝 High-Priority States (Maintain & Scale)

| State | Strategic Role |
|-------|----------------|
| Maharashtra | #1 revenue market, protect share aggressively |
| Madhya Pradesh | #2 market, scale repeat-order campaigns |
| Uttar Pradesh | #3 market, strong expansion potential |

#### 📈 Growth Opportunity States (Expand & Invest)

- **Delhi** and **Rajasthan**: next growth markets after top 3.
- Top 3 states already contribute **52.16%** of revenue and top 5 contribute **62.50%**, so selective expansion is necessary to reduce regional concentration risk.

### 🛒 Target Channels

#### 💳 Payment Channel Strategy

- **COD (46%)**: largest current channel, but operationally expensive.
- **UPI (22%)**: best candidate for prepaid conversion campaigns.
- **Cards (24% combined)**: improve trust and offers to increase adoption.

#### ✅ Channel Action

- Incentivize prepaid (UPI/Card) with small checkout discounts.
- Keep COD available for conversion, but use nudges to shift first-time customers to prepaid in next orders.

### 📣 Marketing Strategy

#### 🗓️ Seasonal Campaigns

- Double down in **Q1**, especially around **January** (best month: **₹61,632** revenue).
- Launch **recovery campaigns** before and during weak periods around **May** (lowest month: **₹12,966**).
- Build monthly promotional waves to reduce the **78.96% peak-to-low revenue gap**.

#### 💰 Promotions & Offers

- Use **repeat-customer coupons** and threshold-based offers to lift AOV.
- Push high-margin SKUs in campaign creatives, not just high-volume SKUs.

#### 📱 Performance Marketing

- Geo-target ads by state priority: Maharashtra, Madhya Pradesh, Uttar Pradesh first.
- Build separate ad sets by category objective:
  - **Volume objective:** Clothing
  - **Margin objective:** Electronics/Furniture

#### 🔄 Operations & Conversion Quality

- Reduce COD friction with proactive order confirmation and shipment updates.
- Improve product detail clarity to reduce cancellations/returns.
- Track prepaid share, cancellation rate, and delivery success rate as weekly operational KPIs.

### 📊 Summary Action Plan

| Priority | Action | Expected Impact |
|----------|--------|-----------------|
| 🔴 High | Convert COD share from **46%** toward **<40%** with prepaid incentives | Better cash flow + lower fulfillment risk |
| 🔴 High | Run monthly demand-recovery campaigns for weak months (especially around May and July) | More stable revenue across the year |
| 🟡 Medium | Defend top 3 states and scale Delhi/Rajasthan with geo-targeted campaigns | Higher regional growth with lower concentration risk |
| 🟡 Medium | Increase Electronics/Furniture attach rate via bundles | Category diversification + margin lift |
| 🟢 Low | Launch retention automations (repeat coupons, reorder nudges) | Higher repeat rate and CLV |

---

## 🚀 Getting Started
 
### Prerequisites

```bash
Python 3.12+
pip (Python package manager)
```

### Installation

1. **Clone the repository**

```bash
git clone https://github.com/amitkr209/madhav-ecommerce-dashboard.git

cd madhav-ecommerce-dashboard
```

1. **Install dependencies**

```bash
pip install -r requirements.txt
```

1. **Download the dataset**
   - The script automatically downloads data from Kaggle using KaggleHub
   - Dataset link: [Madhav E-Commerce Sales Dataset](https://www.kaggle.com/datasets/amitkumar209/madhav-e-commerce-sales-dataset)
   - Manual download: Download `Orders.csv` and `Details.csv` from the Kaggle link above

### Running the Dashboard

**Option 1: Run the Interactive Dash App**

```bash
python madhav_sales_dashboard.py
```

Then open your browser and navigate to: `http://127.0.0.1:8050/`

**Option 2: Explore the Jupyter Notebook**

```bash
jupyter notebook Madhav_E-Commerce_Sales_Analysis.ipynb
```

---

## 📚 Key Learnings & Project Scope

### 💼 Freelancing Project Deliverables

- ✅ **Client Requirements**: Sales performance analysis and interactive dashboards
- ✅ **Data Collection**: Created and structured e-commerce transaction dataset
- ✅ **Dataset Publication**: Published dataset to Kaggle for public access
- ✅ **Multi-format Delivery**: Python dashboards + Power BI reports
- ✅ **Business Insights**: Actionable recommendations for revenue optimization
- ✅ **Documentation**: Complete project documentation and code comments

### Technical Skills Demonstrated

- ✅ End-to-end data pipeline development
- ✅ Data cleaning and transformation with Pandas
- ✅ Statistical analysis and metric calculation
- ✅ Static visualization best practices (Matplotlib/Seaborn)
- ✅ Interactive dashboard development (Plotly/Dash)
- ✅ Web application deployment with Python
- ✅ Business intelligence reporting (Power BI)
- ✅ API integration (Kaggle)

### Business Skills Demonstrated

- ✅ KPI definition and tracking
- ✅ Trend analysis and forecasting
- ✅ Customer segmentation
- ✅ Geographic analysis
- ✅ Payment behavior analysis
- ✅ Business recommendation development

---

## 🎓 Use Cases & Portfolio Value

This project is ideal for showcasing:

- **Freelance Data Analytics Experience**: End-to-end client project delivery
- **Data Analyst Portfolio**: Complete analytics capabilities from data creation to insights
- **Business Intelligence Role**: Demonstrates BI dashboard development and business acumen
- **E-commerce Analytics**: Shows domain expertise in retail/e-commerce metrics
- **Dashboard Developer Position**: Proves ability to build interactive, client-ready visualizations

---

## 🎬 Conclusion

This Madhav E-Commerce Sales Dashboard project represents a **complete data analytics lifecycle** — from raw business requirements to actionable insights and interactive visualizations. As a freelance engagement, it showcases not just technical proficiency, but also the ability to:

### 💡 Key Achievements

**📊 Technical Excellence:**

- Built three different visualization platforms (Static, Interactive Web, Power BI) from a single dataset
- Demonstrated mastery across the entire Python data science stack
- Created production-ready, client-facing dashboards with professional polish

**🚀 Process & Deliverables:**

- Structured raw business data into a clean, analysis-ready Kaggle dataset
- Completed comprehensive EDA with statistical analysis and trend identification
- Built multi-platform dashboards tailored to different stakeholder needs
- Provided strategic recommendations backed by data-driven insights

This project serves as a foundation for building similar analytics solutions across various e-commerce and retail domains, demonstrating adaptability and scalable analytical thinking.

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 📊 Project Statistics

![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)
![Pandas](https://img.shields.io/badge/Pandas-1.5+-green.svg)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.7+-orange.svg)
![Seaborn](https://img.shields.io/badge/Seaborn-0.12+-teal.svg)
![Plotly](https://img.shields.io/badge/Plotly-5.11+-red.svg)
![Dash](https://img.shields.io/badge/Dash-2.7+-purple.svg)
![Power BI](https://img.shields.io/badge/Power%20BI-Latest-yellow.svg)

[![Kaggle](https://img.shields.io/badge/Kaggle-Dataset-blue?logo=kaggle&logoColor=white)](https://www.kaggle.com/datasets/amitkumar209/madhav-e-commerce-sales-dataset)
[![GitHub stars](https://img.shields.io/github/stars/amitkr209/Madhav_E-Commerce-Sales_Intelligence_Dashboard?style=social)](https://github.com/amitkr209/Madhav_E-Commerce-Sales_Intelligence_Dashboard)

![License](https://img.shields.io/badge/License-MIT-orange.svg)

---

<div align="center">
  ⭐ Found this project useful? Show your support by starring the repository!
</div>
