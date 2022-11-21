from selenium.webdriver.common.by import By


class StstPage:
    def __init__(self, driver):
        driver.get("https://academy.testifyltd.com/courses/switch-to-software-testing")
        self.got_question_link = driver.find_element(By.XPATH, '//*[@id="__next"]/main/section[8]/div[1]/div[2]/div[1]/div[2]/a/span[2]')
        self.enroll = driver.find_element(By.XPATH, '//*[@id="__next"]/main/section[14]/div/h2')
        self.image = driver.find_element(By.XPATH, '//*[@id="story"]/div/div[2]/div[1]/div[1]/span/img')
        self.resources = driver.find_element(By.XPATH, '//*[@id="__next"]/section/div/div[1]/div[2]/div/div[2]/h3')