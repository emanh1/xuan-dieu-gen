from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time
class Main:
    def __init__(self, driver=None):
        self.driver = driver

    def extract(self):
        self.driver.get("https://www.thivien.net/Xu%C3%A2n-Di%E1%BB%87u/author-RFLL7QmxIAtjETgw2z9Z4w")
        tables = self.driver.find_elements(By.CLASS_NAME, "poem-group-list")
        t = 0
        origin_tab = self.driver.current_window_handle
        for table in tables:
            t+=1
            links = table.find_elements(By.TAG_NAME, "a")
            l=0
            for link in links:
                time.sleep(10)
                l+=1
                href = link.get_attribute('href')
                self.driver.execute_script(
                    f'''window.open("{href}","_blank");'''
                    )
                self.driver.switch_to.window(self.driver.window_handles[1])
                time.sleep(3)
                div = self.driver.find_element(By.CLASS_NAME, "poem-content")
                content = div.find_element(By.TAG_NAME, "p").text
                print(f"writing table {t} link {l}")
                self.write_data(content)
                self.driver.close()
                self.driver.switch_to.window(origin_tab)
                #self.driver.switch_to.window(self.driver.window_handles[0])
                #self.driver.get("https://www.thivien.net/Xu%C3%A2n-Di%E1%BB%87u/author-RFLL7QmxIAtjETgw2z9Z4w")
        
    def write_data(self, text):
        with open('data.txt', 'a', encoding='utf-8') as f:
            f.write(text + "\n")
if __name__=='__main__':
    options = Options()
    #prof = webdriver.FirefoxProfile()
    #prof.add_extension('uBlock0_1.57.3b0.firefox.signed.xpi')
    options.add_argument("--headless")
    #options.profile = prof
    driver = webdriver.Firefox(options=options)
    main = Main(driver)
    #time.sleep(5)
    main.extract()