from selenium import webdriver 

def screen_f(message):
    op = webdriver.ChromeOptions()
    op.add_argument('--headless')
    op.add_argument("--window-size=1920x1080")
    chromedriver = '/Users/maliboo/Downloads/chromedriver'
    driver = webdriver.Chrome(chromedriver,options=op)
    driver.get(message)
    filename = driver.title+ ".png"
    driver.save_screenshot(filename)
    driver.quit()

    return filename

