from selenium.webdriver.common.by import By


class TasPage:
    def __init__(self, driver):
        driver.get("https://academy.testifyltd.com/courses/test-automation-simplified")
        self.courses = driver.find_element(By.XPATH, '//*[@id="__next"]/main/section[1]/header/div/div/div[2]/button')
        self.success_stories_link = driver.find_element(By.LINK_TEXT, 'Success Stories')
        self.title = driver.find_element(By.TAG_NAME, 'h1')
        self.enroll_now_button = driver.find_element(By.XPATH, '//*[@id="__next"]/main/section[4]/div[1]/div/div[2]/div[2]').find_element(By.XPATH, '//*[@id="__next"]/main/section[4]/div[1]/div/div[2]/div[2]/div/button')
        self.send_message_button = driver.find_element(By.XPATH, '//*[@id="enrol"]/div/div/div[1]/div/a')

