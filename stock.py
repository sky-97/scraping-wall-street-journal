from bs4 import BeautifulSoup
import requests
import sqlite3

conn = sqlite3.connect('stock.db')
c = conn.cursor()
c.execute("""create table stocktable (name TEXT,CurrentPrice TEXT,pricechange TEXT,open TEXT,prior_close TEXT)""")

list = ['AAPL','NKE','NFLX','AMZN','MSFT']
for i in list:
    url = 'https://quotes.wsj.com/'+i
    source = requests.get(url)
    soup = BeautifulSoup(source.text,'lxml')
    header = soup.find_all("header")

    div =soup.find_all("div")[0]

    table = div.find('div', attrs={'data-module-id': '2'})
    #print(table.text)
    spam_current=table.find_all("span")[4]
    #print(spam_current.text)
    price_change=table.find_all("span")[7]
    open =table.find_all("li")[28]
    open_data = open.find('span', attrs={'class': 'data_data'})
    #open_data=open.find_all("data_data")
    piror=table.find_all("li")[29]
    prior_data = piror.find('span', attrs={'class': 'data_data'})
    list_prior = prior_data.text.split()
    close_prior = list_prior[0]
    #print(price_change.text)
    # c.execute("INSERT into movie values (?,?,?,?,?)",(my_movie_item[0].text,my_movie_item[1].text,my_movie_item[4].text,my_movie_item[5].text,my_movie_item[6].text))
    c.execute("INSERT into stocktable values (?,?,?,?,?)",(str(i),spam_current.text,price_change.text,open_data.text,str(close_prior)))
conn.commit()
#c.execute("INSERT INTO stocktable values(?)",(APPLE.text,NIKE.text,NETFLIX.text,AMAZON.text,MICROSOFTA.TEXT))
#conn.commit()
conn.close()
