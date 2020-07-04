from selenium import webdriver   
def screen_f(message):
    op = webdriver.ChromeOptions()
    op.add_argument('--headless')
    op.add_argument("--window-size=1440x1024")
    chromedriver = '/Users/maliboo/Downloads/chromedriver'
    driver = webdriver.Chrome(chromedriver,options=op)
    driver.get(message)
    driver.save_screenshot(driver.title+".png")
    driver.quit()


screen_f(
    message = input('enter: ')
)