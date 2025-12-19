# ☕️ Cafe Revenue Insights Lab
> **From Intuition to Insight: Re-engineering past business experience with Data.**

## 1. Project Motivation

### Background: From Intuition to Insight
> *Running a business solo meant facing a wall of silence. No feedback, just consequences.*

For three years, I ran a cafe alone. I poured my heart into it, but I lacked the "system."
I struggled with pricing, traffic analysis, and the invisible variables of business.
"Why were sales low today?" "Is my marketing effective?"
I closed the doors, but I didn't lock away the lessons.
I decided to simulate my past reality. By digitizing the environment, the weather, and the financials of those 3 years, I am building the mentor I never had.
This project is not just about data; it’s about giving structure to chaos.

### Vision: Re-engineering the Past
> *Validating the past with the technology of the present to design a better future.*

Three years of trial and error. A multitude of "Why?" without "How."
I realized that passion alone cannot overcome the lack of accurate design and management.
My cafe is gone, but the data points remain in my memory.
I am now retrieving them to build a virtual dataset—standardizing everything from local climate to menu margins.
I am creating a comprehensive solution that I wish I had back then.

---

## 2. Project Overview
This repository, **Cafe Revenue Insights Lab**, is a data simulation and analysis project.
The goal is to reconstruct the operational data of a small business to derive actionable insights and strategic solutions.

### Key Objectives
* **Virtual Data Construction:** Creating a realistic dataset based on actual past experiences (Sales, Weather, **Marketing, Cost, Labor**).
* **Scalability:** Starting with a high-fidelity **1-year pilot model** and expanding to a 3-year simulation using Python.
* **Root Cause Analysis:** Identifying correlations between environmental factors (Weather, Seasonality) and Business KPIs.
* **Strategic Dashboarding:** Visualizing the "What-if" scenarios to find the optimal operating strategy.

---

## 3. Tech Stack
* **Language:** Python 3.x
* **Data Manipulation:** Pandas, NumPy
* **Visualization:** Matplotlib, Seaborn
* **Tools:** Jupyter Notebook, Git/GitHub

---

## 4. Roadmap

### Phase 1: Data Simulation & Construction [Completed]
> *Status: Successfully re-engineered 1 year of operation data (approx. 27,000 txns) and marketing logs with complex business logic.*

- [x] **Define Data Schema:** Established logic for Date, Weather, Menu Category, and Unit Economics (Price/Cost/Margin).
- [x] **Implement Business Logic (The "Rules"):**
    - *Rule 1 (Seasonality):* Adjusted daily order volume based on seasonal trends (Winter dip vs. Summer peak).
    - *Rule 2 (Weather Impact):* Correlated specific weather conditions (Rain/Snow) with Menu Type (Ice/Hot) preferences.
    - *Rule 3 (Menu Mix):* Applied weighted probabilities reflecting real-world popularity (e.g., Americano dominance).
    - *Rule 4 (Strategic Event):* Simulated the **"Sandwich Launch Effect" (July 1st)**, reflecting a traffic boost and analyzing the cross-selling effect (Set Menu Bundling).
- [x] **Generate Marketing Data (New):**
    - Engineered the **"Marketing Paradox"**: Modeled a disconnect between high Instagram ad spend and actual revenue.
    - Implemented the **"Offline Variable"**: Simulated the high impact of a physical signboard installation in H2.
- [x] **Generate Virtual Dataset:** Created 1-year transaction log (`cafe_sales_data_en.csv`) and marketing log (`cafe_marketing_data.csv`).

### Phase 2: Exploratory Data Analysis (EDA) [In Progress]
> *Status: Verifying data integrity, merging datasets, and analyzing causal relationships.*

- [x] **Sanity Check:** Verified business logic reflection (Sandwich Launch impact & Seasonality) using `notebooks/01_eda_basic_check.ipynb`.
- [x] **The Marketing Paradox Visualization:** Merged Sales and Marketing datasets to visualize the ROI disconnect (High Digital Spend ≠ High Sales) and confirmed the impact of the Offline Signboard.
- [ ] **Profitability Analysis:** Analyze Net Profit Margin trends by Season and Menu Category.
- [ ] **Weather Correlation:** Visualize how 'Rain' or 'Snow' impacts the sales share of Hot vs. Ice beverages.
- [ ] **Peak Time Analysis:** Identify "Golden Hours" for each menu category to optimize preparation.
- [ ] **Scenario Verification:** Validate if the simulated data aligns with actual business memories (Reality Check).

### Phase 3: Insight & Solution (Digital Twin Expansion)
> *Status: Planning data expansion for deeper operational analysis.*

- [ ] **Data Expansion (Digital Twin):** Integrate **Cost (P&L)**, **Labor Efficiency**, and **Competitor** datasets for root cause analysis.
- [ ] **Dashboard Development:** Build an interactive dashboard to visualize "What-if" scenarios.
- [ ] **Strategy Formulation:** Propose an optimized operation strategy based on the data (e.g., Dynamic Pricing or Inventory Management).

---

## ✉️ Contact
* **Author:** Seoyeon Jeong
* **LinkedIn:** [https://www.linkedin.com/in/im-seoyeon-jeong/]
* **Email:** [syn.eoeo@gmail.com]
