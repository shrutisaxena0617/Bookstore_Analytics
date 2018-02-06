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
#import pdb;pdb.set_trace()
with open('Dataset/isbn_ebook.csv', 'r') as file:
    reader = csv.reader(file, delimiter=",")
    for x in reader:
        #print x
        if ("ISBN" not in x):
            isbns.extend(x)
    file.close()

#print isbns

myfile = open('Dataset/myfile_ebook.csv', 'w')
writer = csv.writer(myfile, quoting=csv.QUOTE_ALL, delimiter=",")
writer.writerow(["S.No","ISBN", "Ebook available online?(Y/N)"])

sno = 1
for isbn in isbns:

    #myurl = http://gen.lib.rus.ec/search.php?req=9780029124857&lg_topic=libgen&open=0&view=simple&res=25&phrase=0&column=identifier
    myurl = "http://gen.lib.rus.ec/search.php?req=" + isbn.strip() + "&lg_topic=libgen&open=0&view=simple&res=25&phrase=0&column=identifier"
    try:
        mypage = urllib2.urlopen(myurl)
        mysoup = BeautifulSoup(mypage)
        all_tables = mysoup.find_all('table')
        new_book_right_table = mysoup.find('table', class_='c')
        mystr_newbook = str(new_book_right_table)

        if("Mb" in mystr_newbook):
            flag = 1
        else:
            flag = 0
        #new_book_right_table = mysoup.find('table', class_='results-table-Logo')
        #mypricelist = []
        #mystr_newbook = str(new_book_right_table)
        #mypricelist = re.findall("(?<=\$)(\d+\.\d{2})", mystr_newbook)
        #min_price = min(float(i) for i in mypricelist)
    except Exception as exp:
        #print exp
        flag = 0

    print sno, isbn, flag

    # write isbn, min_price to csv file

    row = (sno, isbn, flag)
    writer.writerow(row)
    sno = sno+1
myfile.close()

# with open('myfile.csv', 'r') as f:
#     for line in f:
#         print line
