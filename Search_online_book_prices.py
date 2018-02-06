# Program to search best available online book prices using ISBN
# Data source used - https://www.bookfinder.com/ since it displays a wide range of prices (Amazon, Ebay, Publisher, Barnes & Nobles, ecampus.com, BookByte, Textbook.com, Abebooks, Alibris and more)
# which includes shipping. This gives a better view
from StringIO import StringIO
import bs4
import re
import csv
from bs4 import BeautifulSoup
import urllib2

ctr = 0

final_list = []
isbns = []

with open('Dataset/isbn.csv', 'r') as file:
    reader = csv.reader(file, delimiter=",")
    for x in reader:
        print x
        if ("ISBN" not in x):
            isbns.extend(x)
    file.close()

#print isbns

myfile = open('Dataset/myfile.csv', 'w')
writer = csv.writer(myfile, quoting=csv.QUOTE_ALL, delimiter=",")
writer.writerow(["S.No","ISBN", "MIN PRICE"])

sno = 1
for isbn in isbns:
    myurl = "https://www.bookfinder.com/search/?author=&title=&lang=en&new_used=*&destination=us&currency=USD&binding=*&isbn=" + isbn.strip() + "&keywords=&minprice=&maxprice=&min_year=&max_year=&mode=advanced&st=sr&ac=qr"
    try:
        mypage = urllib2.urlopen(myurl)
        mysoup = BeautifulSoup(mypage)
        all_tables = mysoup.find_all('table')
        new_book_right_table = mysoup.find('table', class_='results-table-Logo')
        mypricelist = []
        mystr_newbook = str(new_book_right_table)
        mypricelist = re.findall("(?<=\$)(\d+\.\d{2})", mystr_newbook)
        min_price = min(float(i) for i in mypricelist)
    except Exception as exp:
        print exp
        min_price = -1

    print sno, isbn, min_price

    # write isbn, min_price to csv file

    row = (sno, isbn, min_price)
    writer.writerow(row)
    sno = sno+1
myfile.close()

# with open('myfile.csv', 'r') as f:
#     for line in f:
#         print line
