from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get('https://www.google.com')

field=browser.find_element_by_name('q')
field.send_keys('python')
field.send_keys(Keys.RETURN)

try:
    assert 'java' in browser.title
except AssertionError as a:
    print('Exception: ', type(a))

browser.close()

import unittest

class MyTest(unittest.TestCase):

    def setUp(self):
        print('setup...')
        self.browser = webdriver.Chrome()

    def test_testcase1(self):
        browser = self.browser
        browser.get('https://www.google.com')

        field = browser.find_element_by_name('q')
        field.send_keys('python')
        field.send_keys(Keys.RETURN)

        assert 'java' in browser.title

    def test_testcase2(self):
        browser = self.browser
        browser.get('https://www.google.com')

        field = browser.find_element_by_name('q')
        field.send_keys('python')
        field.send_keys(Keys.RETURN)

        assert 'python' in browser.title


    def test_testcase3(self):
        browser = self.browser
        browser.get('https://www.google.com')

        field = browser.find_element_by_name('q')
        field.send_keys('python')
        field.send_keys(Keys.RETURN)

        assert 'java' in browser.title

    def tearDown(self):
        self.browser.close()
        print('teardown...')

if __name__ == '__main__':
    unittest.main()