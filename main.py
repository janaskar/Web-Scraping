import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style, init

def get_weather(city):
    # Initialize colorama
    init(autoreset=True)

    listdiv = []

    # Create URL
    url = f"https://www.google.com/search?q=weather+{city}"

    # Requests instance
    html = requests.get(url).content

    # Getting raw data
    soup = BeautifulSoup(html, 'html.parser')

    # Get the temperature and other data
    temp_div = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'})
    if temp_div:
        temp = temp_div.text
        str_div = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'})
        listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})

        data = str_div.text.split('\n')
        time = data[0] if len(data) > 0 else "Time data not found"
        sky = data[1] if len(data) > 1 else "Sky condition data not found"

        if listdiv:
            strd = listdiv[5].text

            # Formatting the string
            pos = strd.find('Wind')
            other_data = strd[pos:]

            # Get temperature color
            temp_color = get_temp_color(temp)

            # Printing all the data
            print("----------------")
            print(f"Temperature is: {temp_color}{temp}")
            print(f"{Fore.GREEN}{Style.BRIGHT}Time: {Fore.RESET}{time}")
            print(f"{Fore.CYAN}{Style.BRIGHT}Sky Description: {Fore.RESET}{sky}")
            print(other_data)
            print("----------------")
        else:
            print("Weather details not found.")
    else:
        print("Data not found.")

# Function to get color based on temperature
def get_temp_color(temp):
    try:
        temp_value = float(temp.strip()[:-2])
        if temp_value <= 10:
            return Fore.BLUE  # Cold
        elif temp_value <= 25:
            return Fore.GREEN  # Moderate
        else:
            return Fore.RED  # Hot
    except ValueError:
        return Fore.WHITE  # Default color if parsing fails

if __name__ == "__main__":
    city = input("Enter the city name: ")
    get_weather(city)