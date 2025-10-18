# Finance-Data-Project
 This project focuses on exploratory data analysis (EDA) of stock prices for major U.S. banks using Python and Pandas.
 It was developed as part of the Python for Data Science and Machine Learning Bootcamp.
 The goal is to visualize and analyze how bank stocks evolved during and after the 2007–2008 financial crisis up to early 2016.

## Dataset Description
Stock data is obtained using pandas-datareader, which fetches historical stock prices for each bank.
We analyze the following institutions:

- **Bank of America**

- **CitiGroup**

- **Goldman Sachs**

- **JPMorgan Chase**

- **Morgan Stanley**

- **Wells Fargo**

Each bank’s data is stored in a separate Pandas DataFrame, named after its ticker symbol (e.g., BAC for Bank of America).

## Objectives

- Retrieve historical stock data from January 1, 2006 to January 1, 2016 using pandas_datareader
- Explore daily stock prices, trading volumes, and trends over time
- Visualize bank stock performance during the financial crisis (2007–2008)
- Compare key financial metrics across multiple banks
- Practice data cleaning, manipulation, and visualization with real financial data

## Tech Stack
- Python
- Pandas, NumPy
- Matplotlib, Seaborn
- PyCharm

## How to Run
1. Clone the repository:  
```bash
git clone <your-repo-url>
```
2. Install dependencies:
 ```bash
pip install name of libraries
```
3. Run the main Python script:
 ```bash
python FinanceMain.py
```
## Notes
- Make sure to use the latest working data source for pandas_datareader (as APIs may change)
- You can check the latest supported sources in the official documentation: https://pandas-datareader.readthedocs.io/en/latest/remote_data.html
- A pickle file with pre-fetched data is also provided in the course resources to avoid fetching issues

