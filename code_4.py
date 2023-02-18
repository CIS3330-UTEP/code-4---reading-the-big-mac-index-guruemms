#import csv
import pandas as pd

'''
def get_big_mac_price_by_year(year,country_code):
    query1 = f"(iso_a3 == {country_code} and str(date[0:4]) == {year}"
    price_by_year = df['dollar_price'].query(query1)
    print(round(price_by_year),2)

def get_big_mac_price_by_country(country_code):
    query1 = f"(iso_a3 == {country_code}"
    price_by_country = df['dollar_price'].query(query1)
    print(round((price_by_country.mean()),2))
'''
def get_the_cheapest_big_mac_price_by_year(year):
    query1 = f"date[0:4] == '{year}'"
    pby_df = df.query(query1) #price by year dataframe
    print(price_by_year)
    idx_min_price = price_by_year['dollar_price'].idxmin()
    country = df['country'].loc[idx_min_price]
    price = df['dollar_price'].loc[idx_min_price]
    print(country,price)
'''
def get_the_most_expensive_big_mac_price_by_year(year):
    #query1 = f"str(date[0:4]) == {year}"
'''
if __name__ == "__main__":
    big_mac_file = './big-mac-full-index.csv'
    df = pd.read_csv(big_mac_file)
    get_the_cheapest_big_mac_price_by_year(2008)