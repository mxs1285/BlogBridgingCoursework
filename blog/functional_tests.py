from selenium import webdriver
from selenium import common
import time
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class CvAddTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.get('http://localhost:8000/admin/')
        username = self.browser.find_element_by_id('id_username')
        username.send_keys('test')
        password = self.browser.find_element_by_id('id_password')
        password.send_keys('test')
        btn_login = self.browser.find_element_by_xpath('/html/body/div/div[2]/div/form/div[3]/input')
        btn_login.click()

    def tearDown(self):
        self.browser.quit()

    def testCanEditSummary(self):
        self.browser.get('http://localhost:8000/cv/')

        btn_edit = self.browser.find_element_by_xpath('/html/body/div[2]/div/div/a[1]')
        btn_edit.click()

        summaryEdit = self.browser.find_element_by_xpath('/html/body/div[2]/div/div/form/p[3]/textarea')
        summaryEdit.text = "test"

        btn_save = self.browser.find_element_by_xpath('/html/body/div[2]/div/div/form/button')
        btn_save.click()

        summary = self.browser.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/p')

        self.failUnlessEqual(summary.text, summaryEdit.text)
        return

    def testCanEditQualifications(self):
        self.browser.get('http://localhost:8000/cv/')

        btn_edit = self.browser.find_element_by_xpath('/html/body/div[2]/div/div/a[2]')
        btn_edit.click()

        qualificationsEdit = self.browser.find_element_by_xpath('/html/body/div[2]/div/div/form/p[3]/textarea')
        qualificationsEdit.text = "test"

        btn_save = self.browser.find_element_by_xpath('/html/body/div[2]/div/div/form/button')
        btn_save.click()

        qualifications = self.browser.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/p')

        self.failUnlessEqual(qualifications.text, qualificationsEdit.text)
        return

    def testCanEditCoreSkills(self):
        self.browser.get('http://localhost:8000/cv/')

        btn_edit = self.browser.find_element_by_xpath('/html/body/div[2]/div/div/a[3]')
        btn_edit.click()

        coreSkillsEdit = self.browser.find_element_by_xpath('/html/body/div[2]/div/div/form/p[3]/textarea')
        coreSkillsEdit.text = "test"

        btn_save = self.browser.find_element_by_xpath('/html/body/div[2]/div/div/form/button')
        btn_save.click()

        coreSkills = self.browser.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/p')

        self.failUnlessEqual(coreSkills.text, coreSkillsEdit.text)
        return

    def testCanEditExperience(self):
        self.browser.get('http://localhost:8000/cv/')

        btn_edit = self.browser.find_element_by_xpath('/html/body/div[2]/div/div/a[4]')
        btn_edit.click()

        experienceEdit = self.browser.find_element_by_xpath('/html/body/div[2]/div/div/form/p[3]/textarea')
        experienceEdit.text = "test"

        btn_save = self.browser.find_element_by_xpath('/html/body/div[2]/div/div/form/button')
        btn_save.click()

        experience = self.browser.find_element_by_xpath('/html/body/div[2]/div/div/div[4]/p')

        self.failUnlessEqual(experience.text, experienceEdit.text)
        return
