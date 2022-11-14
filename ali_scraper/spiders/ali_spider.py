from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import scrapy
from ali_scraper.items import AliScraperItem
import time


class AliScraper(scrapy.Spider):
    name = 'ali_spider'
    allowe_domains = ['aliexpress.ru']
    start_urls = ['https://aliexpress.ru/category/202001195/cellphones.html?SortType=total_tranpro_desc&g=n&page=1&spm=a2g2w.productlist.refine.3.2a9c71dd6t5kz']


    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--disable-blink-features=AutomationControlled")
        s = Service(executable_path="/ozon_scraper/chromedriver")
        
        self.driver = webdriver.Chrome(options=options, service=s)

    def parse(self, response):
        try:
            self.driver.get(response.url)
            item = AliScraperItem()
            time.sleep(5)
            self.driver.execute_script("window.scrollTo(0,8000);")
            time.sleep(5)
            self.driver.execute_script("window.scrollTo(8000,16000);")
            time.sleep(5)
            elements = self.driver.find_elements(By.XPATH, '//div[@class = "product-snippet_ProductSnippet__content__1ettdy"]/a')
            url_list = []
            for i in elements:
                url_list.append(i.get_attribute('href'))
            
            url_list = list(set(url_list))
            item['urls_phone'] = url_list
        except Exception as ex:
            print(ex)
        finally:
            self.driver.close()
            self.driver.quit()
        return item
