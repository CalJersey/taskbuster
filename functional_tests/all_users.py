# _*_ coding: utf-8 _*_
import os
from selenium import webdriver
import unittest

# System.setProperty("webdriver.chrome.driver", "/usr/local/bin/");
# WebDriver driver = new ChromeDriver();

chromedriver = "/usr/local/bin/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = driver
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_it_worked(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Welcome to Django', self.browser.title)

if __name__ == '__main__':
    unittest.main(warnings='ignore')