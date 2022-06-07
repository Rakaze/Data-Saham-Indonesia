import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://sahamidx.com/?view=Stock.Top&path=Stock&date_now=2022-06-03&field_sort=stock_persen&sort_by=DESC'

r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')

gain_table = soup.find('table', class_ = 'tbl_border_gray')

headers = []

for i in gain_table.find_all('td', class_ = 'menu_link'):
    title = i.text.strip()
    headers.append(title)
    print(headers)

df = pd.DataFrame(rows = headers)
save = df.to_csv('top_gainers.csv')