import requests
from bs4 import BeautifulSoup

def main():
  url = 'http://blog.serverworks.co.jp/tech/2018/12/04/reinvent2018_advanced_vpc_design/'

  response = requests.get(url)
  content = response.content

  soup = BeautifulSoup(content, 'html.parser')

  #n = soup.find_all('h3', class_='restaurant__name')
  n = soup.find_all('h1')

  for nname in n:
    print(nname.get_text())

if __name__ == '__main__':
  main()


