from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

EMAIL = 'test@test.com'
PASSWORD = '123456'

class CrackGeetest():
    def __init__(self): 
        self.url = "https://login.flyme.cn/vCodeLogin"
        self.browser = webdriver.Chrome()
        self.wait = WebDriverWait(self.browser,20)
        self.email = EMAIL
        self.password = PASSWORD

    def get_geetest_button(self):
        button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME,'geetest_radar_tip')))
        return button

    def get_position(self):
        img = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME,'geetest_canvas_img')))
        time.sleep(2)
        location = img.location
        size = img.size
        top,bottom,left,right = location['y'],location['y'] + size['height'],location['x'],location['x']+size['width']
        return (top,bottom,left,right)

    def get_geetest_image(self,name='captcha.png'):
        top,bottom,left,right = self.get_position()
        print('验证码位置：',top,bottom,left,right)
        screenhot = self.get_screenhot()
        captcha = screenhot.crop((left,top,right,bottom))
        return captcha
    
    def get_slider(self):
        slider = slef.wait.until(EC.element_to_be_clickable((By.CLASS_NAME,'geetest_slider_button')))
        return slider
    
    



    button = self.get_geetest_button()
    button.click()