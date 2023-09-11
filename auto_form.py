from selenium import webdriver

driver = webdriver.Firefox()
driver.get('https://mega.io/copyrightnotice')

mega_links = "A"
mega = driver.find_element('//*[@id="copy"]/textarea', 'xpath')
mega.send_keys(mega_links)

