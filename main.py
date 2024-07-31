# importing the library
import requests
from bs4 import BeautifulSoup

listdiv = []

# promting the user to enter a city name
city = input("Enter the city name: ")

# create url
url = "https://www.google.com/search?q="+"weather "+city

print(url)

# requests instance
html = requests.get(url).content
 
# getting raw data
soup = BeautifulSoup(html, 'html.parser')

# get the temperature and other data
temp_div = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'})
if temp_div:
    temp = temp_div.text
    str_div = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'})
    listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
else:
    temp = "Data not found"
 
# format the data
data = str.split('\n')
time = data[0] if len(data) > 0 else "Time data not found"
sky = data[1] if len(data) > 1 else "Sky condition data not found"
if listdiv:
    strd = listdiv[5].text
 
    # formatting the string
    pos = strd.find('Wind')
    other_data = strd[pos:]

if temp == "Data not found":
    print(temp)
else:
    # printing all the data
    print("Temperature is", temp)
    print("Time: ", time)
    print("Sky Description: ", sky)
    print(other_data)