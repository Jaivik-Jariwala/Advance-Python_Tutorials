import pandas as pd
import numpy as np
import logging
import datetime

filename ="sales_data.csv"

logging.basicConfig(filename='sales_data.csv', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def read_dataset(filename):
    try:
        df = pd.read_csv(filename)
        logging.info("Dataset read successfully")
        return df
    except Exception as e:
        logging.error(f"Error reading dataset: {str(e)}")
        return None

def display_first_rows(df):
    if df is not None:
        print(df.head(3))

def save_updated_dataset(df, Updated_dataset):
    try:
        df.to_csv(Updated_dataset, index=False)
        logging.info(f"Dataset saved to a new file: {Updated_dataset}")
    except Exception as e:
        logging.error(f"Error saving dataset: {str(e)}")

def calculate_totals(df):
    if df is not None:
        total_sales = np.sum(df['Sales'])
        total_profit = np.sum(df['Profit'])
        logging.info(f"Total Sales: {total_sales}")
        logging.info(f"Total Profit: {total_profit}")

def filter_dataset(df):
    if df is not None:
        filtered_df = df[df['Sales'] > 500]
        print("Rows with sales > 500:")
        print(filtered_df)

def run_daily_task():
    logging.info("Daily task started at {}".format(datetime.datetime.now()))
    df = read_dataset('Sales_data.csv')
    display_first_rows(df)
    calculate_totals(df)
    filter_dataset(df)
    save_updated_dataset(df, 'updated_Sales_data.csv')
    logging.info("Daily task completed at {}".format(datetime.datetime.now()))

if __name__ == '_main_':
    run_daily_task()