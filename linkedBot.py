import time,random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class linkedBot:

    def __init__(self, username, password,mongoConf):
        self.username = username
        self.password = password
        self.mongoConf = mongoConf
        self.browser = webdriver.Chrome(r"C:\Users\stagiaire 10\Desktop\scrapping\chromedriver_win32\chromedriver.exe")

    def login_linkedin(self):
        browser = self.browser
        browser.get("https://www.instagram.com/")
        time.sleep(10)
        email = browser.find_element_by_name('username')
        password = browser.find_element_by_name('password')
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(10)

    def google_search(self, googling):
        browser = self.browser
        browser.get(googling)
        # check=True
        time.sleep(10)
        src = self.browser.page_source
        soup = BeautifulSoup(src, 'lxml')
        search = soup.find_all('section', {'class': 'EDfFK ygqzn'})
        #print(search)
        div=search[0].find('div',{'class':'qF0y9 Igw0E IwRSH eGOV_ ybXk5 vwCYk'})
        div = div.find('div', {'class': 'qF0y9 Igw0E IwRSH eGOV_ vwCYk YlhBV'})
        div = div.find('div', {'class': '_7UhW9 xLCgt MMzan KV-D4 uL8Hv T0kll'})
        a = div.find('div')
        print(a)
        print(div)
        nmbrJaime=a.find('span').get_text().strip()
        print(nmbrJaime)
        return nmbrJaime
        # for x in range(20):
        # buttonShowComment = self.browser.find_elements_by_css_selector('section.EDfFK ygqzn')
        # print('heeeeeeeeeeeeeeeeeeeeeeeeee')
        # print(buttonShowComment)
        # buttonShowComment[-3].click()
        # time.sleep(5)
        # time.sleep(5)
        # src = self.browser.page_source
        # soup = BeautifulSoup(src, 'lxml')
        # self.random_sleep()
        # search = soup.find_all('ul', {'class': 'Mr508'})
        # print("number comments")
        # print(len(search))
        # id = 1
        # mongo = self.mongoConf
        # mongo.db.profiles.drop()
        # for coord in search:
        #     div = coord.find('div',{'class':'ZyFrc'})
        #     li = div.find('li',{'class':'gElp9 rUo9f'})
        #     div = li.find('div',{'class':'P9YgZ'})
        #     div = div.find('div',{'class':'C7I1f'})
        #     divName=div.find('div',{'class':'C4VMK'})
        #     h3name=div.find('h3',{'class':'_6lAjh'})
        #     self.humain_scrapping()
        #     #nombre j'aime
        #     # divjaime=div.find('div',{'class':'qF0y9 Igw0E IwRSH eGOV_ _4EzTm pjcA_ aGBdT'})
        #     # divsousdivjaime=divjaime.find('div',{'class':'_7UhW9 PIoXz MMzan _0PwGv uL8Hv'})
        #     # buttonjaime=self.browser.find_element_by_css_selector('button.FH9sR')
        #     #
        #     # print('99999')
        #     # print(buttonjaime)
        #     # #buttonjaime=divsousdivjaime.find('button',{'class':'FH9sR'})
        #     # divdernierjaime=buttonjaime.find('div',{'class':'_7UhW9 PIoXz qyrsm _0PwGv uL8Hv T0kll'})
        #     # nbrjaime=divdernierjaime.get_text().strip()
        #     #nombre j'aime
        #     divNamesoush3=h3name.find('div',{'class':'qF0y9 Igw0E IwRSH eGOV_ _4EzTm ItkAi'})
        #     spanName = divNamesoush3.find('span',{'class':'Jv7Aj mArmR MqpiF'})
        #     print(spanName)
        #     aName=spanName.find('a',{'class':'sqdOP yWX7d _8A5w5 ZIAjV'})
        #     print('----*/*/-----')
        #     print(aName)
        #     name=aName.get_text().strip()
        #     div = div.find('div',{'class': 'Jv7Aj mArmR pZp3x'})
        #     print(div)
        #     div = div.find('div', {'class': 'RR-M- TKzGu'})
        #     print(div)
        #     try:
        #         a = div.find('a', {'class': '_2dbep qNELH kIKUG'})
        #         print(a)
        #         img=a.find('img',{'class':'_6q-tv'})
        #         print(img)
        #         imgurl=img.attrs['src']
        #     except:
        #         img='not exist'
        #     print(imgurl)
        #     print(name)
        #     #print(nbrjaime)
        #     print(mongo.db.profiles.find_one({"name": name},{'_id': False}))
        #     if mongo.db.profiles.find_one({"name": name},{'_id': False}) is None:
        #         mongo.db.profiles.insert_one({'id':id,'name': name, 'imgUrl':imgurl, })
        #         id=id+1
        #     else:
        #         print('existe deja')



