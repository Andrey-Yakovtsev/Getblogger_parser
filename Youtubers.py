import csv
from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup

# путь к драйверу chrome
browser = webdriver.Firefox()
# browser.implicitly_wait(5)

browser.get('https://getblogger.ru/#signin')
sleep(1)
# login_link = browser.find_element_by_xpath("//a[text()='Войти']")
# login_link = browser.find_element_by_xpath("//a[text()='signin']")
email = browser.find_element_by_xpath('//*[@id="modal-signin"]/div[2]/div/div/div[2]/form/div[1]/input')
password = browser.find_element_by_xpath('//*[@id="modal-signin"]/div[2]/div/div/div[2]/form/div[2]/input')

email.send_keys("")
password.send_keys("")

login = browser.find_element_by_xpath('//*[@id="modal-signin"]/div[2]/div/div/div[2]/form/button')
login.click()

sleep(1)
# close_button = browser.find_element_by_xpath('/html/xrtg-app/div[2]/div/div[2]/div/div/a[1]')
# close_button = browser.find_element_by_css_selector('.xrtg__balloon_close')
# close_button.click()

# Получение HTML-содержимого

final_list = []

def get_1st_page_content(broswer_get_address):
    requiredHtml = browser.page_source
    soup = BeautifulSoup(requiredHtml, 'html.parser')
    blogers_data = soup.find_all('div', class_='bloggers-list-item__data')
    counter = 0
    for item in blogers_data:
        try:
            final_list.append(
                {
                    # 'Name': item.find('div', class_='bloggers-list-item__name').find('a'),
                    'Name': str(list(item.find('div', class_='bloggers-list-item__name').find('h3'))[0]).strip(),
                    # .get_text(strip=True),
                    'Location': item.find('div', class_='bloggers-list-item__name').find('p').get_text(strip=True),
                    'Audience': str(
                        list(item.find('div', class_='bloggers-list-item__audience').find('h3'))[0]).strip(),
                    # .get_text(strip=True),
                    # 'Audience_Qaulity': item.find('div', class_='bloggers-list-item__audience').find('span'),
                    # .get_text(strip=True),
                    'Price1': item.find_all('div', class_='bloggers-list-item__price')[0].find('h4').get_text(
                        strip=True),
                    'Post_kind1': item.find_all('div', class_='bloggers-list-item__price')[0].find('p').get_text(
                        strip=True),
                    'Price2': item.find_all('div', class_='bloggers-list-item__price')[1].find('h4').get_text(
                        strip=True),
                    'Post_kind2': item.find_all('div', class_='bloggers-list-item__price')[1].find('p').get_text(
                        strip=True),
                    'Price3': item.find_all('div', class_='bloggers-list-item__price')[2].find('h4').get_text(
                        strip=True),
                    'Post_kind3': item.find_all('div', class_='bloggers-list-item__price')[2].find('p').get_text(
                        strip=True),
                }
            )

        except IndexError:
            print(f'Got an Index Error on page {counter}')
            continue
        counter += 1
    return final_list

def get_pagination_page_content(broswer_get_address):
    requiredHtml = browser.page_source
    soup = BeautifulSoup(requiredHtml, 'html.parser')
    blogers_data = soup.find_all('div', class_='bloggers-list-item__data')
    counter = 0
    for item in blogers_data:
        try:
            final_list.append(
                {
                    # 'Name': item.find('div', class_='bloggers-list-item__name').find('a'),
                    'Name': str(list(item.find('div', class_='bloggers-list-item__name').find('h3'))[0]).strip(),
                    # .get_text(strip=True),
                    'Location': item.find('div', class_='bloggers-list-item__name').find('p').get_text(strip=True),
                    'Audience': str(
                        list(item.find('div', class_='bloggers-list-item__audience').find('h3'))[0]).strip(),
                    # .get_text(strip=True),
                    # 'Audience_Qaulity': item.find('div', class_='bloggers-list-item__audience').find('span'),
                    # .get_text(strip=True),
                    'Price1': item.find_all('div', class_='bloggers-list-item__price')[0].find('h4').get_text(
                        strip=True),
                    'Post_kind1': item.find_all('div', class_='bloggers-list-item__price')[0].find('p').get_text(
                        strip=True),
                    'Price2': item.find_all('div', class_='bloggers-list-item__price')[1].find('h4').get_text(
                        strip=True),
                    'Post_kind2': item.find_all('div', class_='bloggers-list-item__price')[1].find('p').get_text(
                        strip=True),
                    'Price3': item.find_all('div', class_='bloggers-list-item__price')[2].find('h4').get_text(
                        strip=True),
                    'Post_kind3': item.find_all('div', class_='bloggers-list-item__price')[2].find('p').get_text(
                        strip=True),
                }
            )

        except IndexError:
            print(f'Got an Index Error on page {counter}')
            continue
        counter += 1
    return final_list

get_1st_page_content(
    browser.get(
        'https://getblogger.ru/user/search?s%5Bn%5D%5B%5D=youtube&s%5Ba%5D%5B%5D=1&s%5Ba%5D%5B%5D=75&s%5Bp%5D%5B%5D=0&s%5Bp%5D%5B%5D=1000000'
        )
    )

sleep(5)
page_counter = 1
for page in range(2, 44): # total pages - 43
    get_pagination_page_content(
        browser.get
            (
        f'https://getblogger.ru/user/search?s%5Bn%5D%5B0%5D=youtube&s%5Ba%5D%5B0%5D=1&s%5Ba%5D%5B1%5D=75&s%5Bp%5D%5B0%5D=0&s%5Bp%5D%5B1%5D=1000000&s%5Bview%5D=asc&page={page}'
        )
    )
    page_counter +=1
    print(f'Done with page {page_counter}')
    sleep(5)


with open('youtubers_new.csv', 'w', encoding='utf-8', newline='') as fcsv:
    writer = csv.writer(fcsv, delimiter=';')
    writer.writerow(['Name', 'Location', 'Audience',
                     'Price1', 'Post_kind1', 'Price2', 'Post_kind2',
                     'Price3', 'Post_kind3'])

    for item in final_list:
        # writer.writerow(final_list)
        writer.writerow([item['Name'], item['Location'],
                        item['Audience'],
                        item['Price1'], item['Post_kind1'],
                        item['Price2'], item['Post_kind2'],
                        item['Price3'], item['Post_kind3']]
                        )




