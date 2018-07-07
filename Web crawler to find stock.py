import re
import urllib.request
from urllib.request import Request
url = "https://www.google.com/search?q="
stockFinder = input("Enter the company name to find its stock.\n")
url = url + stockFinder
print("The url of your preffered site is "+ url)
newUrl = Request(url,headers={'User-Agent':'Mozilla/5.0'})
dataOfSite = urllib.request.urlopen(newUrl).read()
actualData = dataOfSite.decode("utf-8")
m = re.search("US[$]",actualData)
stockValue=actualData[m.start():m.end()+10]
print("Stock of the entered company is: "+ stockValue)

