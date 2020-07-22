from django.urls import resolve
from django.test import TestCase

from blog import functional_tests
from blog.views import cv_list


class CvTest(TestCase):

    def testCVURL(self):
        found = resolve('/cv/')
        self.assertEqual(found.func, cv_list)

    def testSummary(self):
        testclass = functional_tests.CvAddTest()
        testclass.setUp()
        testclass.testCanEditSummary()
        testclass.tearDown()

    def testQualifications(self):
        testclass = functional_tests.CvAddTest()
        testclass.setUp()
        testclass.testCanEditQualifications()
        testclass.tearDown()

    def testCoreSkills(self):
        testclass = functional_tests.CvAddTest()
        testclass.setUp()
        testclass.testCanEditCoreSkills()
        testclass.tearDown()

    def testExperience(self):
        testclass = functional_tests.CvAddTest()
        testclass.setUp()
        testclass.testCanEditExperience()
        testclass.tearDown()
