'''
<span class="table-ip4-home"> 91.204.150.17</span>
'''


from bs4 import BeautifulSoup
import requests

response = requests.get('https://www.iplocation.net/')
html_data = response.text

soup = BeautifulSoup(html_data, 'lxml')
span_tag = soup.find('span', class_ = 'table-ip4-home')
ip_adress = span_tag.text.strip()
print(ip_adress)