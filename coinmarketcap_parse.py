# structure of html, unlike json, is crazy. so we need another tool. beautiful soup.
from bs4 import BeautifulSoup
# this is how you parse html file.
import os
# bc we need to make a folder.
import glob
# to save as csv file, import pandas
import pandas as pd

if not os.path.exists("parsed_files"):
	os.mkdir("parsed_files")

df = pd.DataFrame()

for one_file_name in glob.glob("html_files/*.html"):
	# one_file_name = html_files/coinmarketcap20200929131452.html
	print(one_file_name)
	one_file_name = "html_files/coinmarketcap20200929131452.html"
	# we want to actually extract the time out of the name. 
	# need to get the file name. so we can actually use another name:
	# print(os.path.basename(one_file_name).replace("coinmarketcap","").replace(".html",""))
	# # this replaces the things we don't want with nothing.
	scrape_time = os.path.basename(one_file_name).replace("coinmarketcap","").replace(".html","")
	f = open(one_file_name, "r")
	soup = BeautifulSoup(f.read(), "html.parser")
	f.close()

	# shows the text of the html as if it didn't change anything. but it's actually coding the raw html into a form of soup.
	# it's not the raw html, it's coded into soup that you can read relatively easily. but it's still printing out the text like nothing was changed.
	# tools to navigate in this soup exist.

	currencies_table = soup.find("tbody")
	# tbody stands for table body
	# that's why it's a step below table
	currency_rows = currencies_table.find_all("tr")
	# now we need to get to individual rows.

	for r in currency_rows:
	# 	# inside each for loop, we deal with only one row. then, we can actually find the td.
	# 	# however, there are many tds with different info. how do we get the info we want?
	# 	# go back to coinmarket cap
	# 	print()
		currency_columns = r.find_all("td")
		if len(currency_columns)>10:
		# print(currency_columns[0])
		# print(currency_columns[1])
		# # this is about the number
		# print(currency_columns[2])
		# # this one is about the name
		# print(currency_columns[3])
		# this one is about the price
			currency_price = currency_columns[3].find("a", {"class": "cmc-link"}).text.replace("$", "").replace(",","")
			currency_name = currency_columns[2].find("p").text
			currency_symbol = currency_columns[2].find("p", {"class": "coin-item-symbol"}).text
			currency_marketcap = currency_columns[6].find("p").text.replace("$", "").replace(",","")
			currency_link = currency_columns[2].find("a")["href"]
			df = df.append({
					'time': scrape_time,
					'name': currency_name,
					'price': currency_price,
					'symbol': currency_symbol,
					'marketcap': currency_marketcap,
					'link': currency_link
				}, ignore_index=True)


df.to_csv("parsed_files/coinmarketcap_dataset.csv")
