# 导入webdriver来打开浏览器
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        # 打开谷歌浏览器
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.browser = webdriver.Chrome(executable_path=r'C:\Users\Zen\AppData\Local\Programs\Python\Python38-32\chromedriver.exe', options=options)
        self.browser.implicitly_wait(3)
        
    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):    
        # 安静听说有一个贼酷的在线待办事项应用
        # 他去瞅了眼这个应用的首页
        self.browser.get('http://localhost:8000')

        # 他发现这首页的标题和头部都有'To-Do'这个玩意
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # 应用邀请他输入一个待办事项
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # 他在一个文本框中输入了"我是你爸爸"
        # 安静的爱好是吹牛逼
        inputbox.send_keys('我是你爸爸')

        # 他按回车键后，页面更新了
        # 待办事项表格中显示了"1: 我是你爸爸"
        inputbox.send_keys(Keys.ENTER)

        self.check_for_row_in_list_table('1: 我是你爸爸')

        # 页面中又显示了一个文本框，可以输入其他的待办事项
        # 他输入了"我仍然是你爸爸"
        # 安静说话很有条理
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('我仍然是你爸爸')
        inputbox.send_keys(Keys.ENTER)
        # 页面再次更新，他的清单中显示了这两个代办事项
        self.check_for_row_in_list_table('1: 我是你爸爸')
        self.check_for_row_in_list_table('2: 我仍然是你爸爸')

        #　安静想知道这个网站是否会记住他的清单

        # 他看到网站为他生成了一个唯一的URL
        # 而且页面中有一些文字解说这个功能

        # 他访问那个URL，发现他的待办事项还在

        # 他很满意，滚去睡觉了
        self.fail('Finish the test!')

if __name__ == "__main__":
    unittest.main(warnings='ignore')