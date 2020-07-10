from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def screen_f(message):
    op = webdriver.ChromeOptions()
    op.add_argument('--headless')
    chromedriver = '/Users/maliboo/Downloads/chromedriver'
    driver = webdriver.Chrome(chromedriver,options=op)
    driver.get(message)
    height = driver.execute_script("return document.body.scrollHeight")
    driver.set_window_size(1920, height)
    filename = driver.title+ ".png"
    driver.save_screenshot(filename)
    driver.quit()


    return filename

