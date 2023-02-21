#import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'
df = pd.read_csv(big_mac_file)

def get_big_mac_price_by_year(year,country_code):
    query1 = f"iso_a3 == {country_code.upper()} and date >= '{year}-01-01' and date <= '{year}-12-31'"
    pby = df.query(query1)
    pby['dollar_price'].mean()
    print(round(pby['dollar_price'].mean()),2)

def get_big_mac_price_by_country(country_code):
    country_code = country_code.upper()
    query1 = f"(iso_a3 == '{country_code}')"
    pby = df.query(query1)
    print(round(pby['dollar_price'].mean(),2))

def get_the_cheapest_big_mac_price_by_year(year):
    query1 = f"date >= '{year}-01-01' and date <= '{year}-12-31'"
    pby_df = df.query(query1) #price by year dataframe
    idx_min_price = pby_df['dollar_price'].idxmin()
    min_price = df.loc[idx_min_price]
    print(f"{min_price['name']}({min_price['iso_a3']}): ${round(min_price['dollar_price'],2)}")

def get_the_most_expensive_big_mac_price_by_year(year):
    df = pd.read_csv(big_mac_file)
    query1 = f"date >= '{year}-01-01' and date <= '{year}-12-31'"
    pby_df = df.query(query1) #price by year dataframe
    idx_max_price = pby_df['dollar_price'].idxmax()
    max_price = df.loc[idx_max_price]
    print(f"{max_price['name']}({max_price['iso_a3']}): ${round(max_price['dollar_price'],2)}")

if __name__ == "__main__":
    print(get_big_mac_price_by_year(2008,'jpn'))
'''    

    get_big_mac_price_by_year(2008,'arg')
'''