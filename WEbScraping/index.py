import requests
from bs4 import BeautifulSoup

url = 'https://www.cafeendosis.site'
response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
 
 
print('네이버 실시간 검색어')    

titles = soup.find_all('h2')



        


print("\n titulos encontrados:")
for title in titles:
    print(title.get_text())
    
print("Contenido HTML recibido:\n", response.text)

    
