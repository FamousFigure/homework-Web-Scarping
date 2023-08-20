'''
<div class="serp-item"> == $0
'''
from pprint import pprint
import requests
import fake_headers
from bs4 import BeautifulSoup
import json

for i in range(1, 401):
    url = f'https://spb.hh.ru/search/vacancy?no_magic=true&L_save_area=true&text=python&excluded_text=&area=2&area=1&salary=&currency_code=RUR&experience=doesNotMatter&order_by=relevance&search_period=0&items_on_page=5&page={i}'
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.7.2.765 Yowser/2.5 Safari/537.36'}
    headers_gen = fake_headers.Headers(browser='firefox', os='win')
    lst = []
    response = requests.get(url, headers=headers_gen.generate())
    html_data = response.text
    soup = BeautifulSoup(html_data, 'lxml').find_all('div',class_='vacancy-serp-item-body__main-info')

    for div in soup:
        title = div.find('h3').find('a').text
        if "Django" in title or "Flask" in title:
            name_company = div.find('a',class_="bloko-link bloko-link_kind-tertiary").text
            #city = div.find('div', class_='bloko-text', text="Санкт-Петербург").text
            city = div.find("div",
                                        class_="bloko-text",
                                        attrs={
                                            "data-qa": "vacancy-serp__vacancy-address"
                                        }
                                        ).text
            link = div.find('h3').find('a').get('href')
            try:
                price = div.find('span',class_='bloko-header-section-2').text
            except:
                price='Зарплата не указана'
            result = {
                'city':city,
                'name_company':name_company,
                'title':title,
                'link':link,
                'price':price.strip(),
            }
            lst.append(result)
            with open(f'data/Job announcement{i}.json','w',encoding='utf-8') as file:
                json.dump(lst, file,indent=4, ensure_ascii=False)
        else:
            print('Нет объявлений на странице')
    print(f'number page {i} success')


# pprint()

