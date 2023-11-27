from selenium import webdriver
from django.test import LiveServerTestCase
from schedule_app.models import Employee
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test import TestCase, Client
from django.contrib.auth.models import User, Group
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from django.urls import reverse
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


'''class TestEmployeeListPage(StaticLiveServerTestCase):

	def setUp(self):
		self.browser = webdriver.Chrome()
		

	def tearDown(self):
		self.browser.quit()

	def test_no_employee_alert_is_displayed(self):
		self.browser.get(self.live_server_url)
		
		alert = self.browser.find_element_by_class_name('noemployee-wrapper')
		self.assertEquals(
			alert.find_element_by_tag_name('p').text,
			'There are no employees registered.'
		)'''




class UserCreationTest(LiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = webdriver.Chrome()
        cls.selenium.implicitly_wait(10)

    '''@classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()'''

    def setUp(self):
        # Create an existing superuser with the manager_role
        self.superuser = User.objects.create_superuser('admin', 'admin@example.com', 'adminpassword')
        self.manager_role = Group.objects.create(name='manager_role')
        self.superuser.groups.add(self.manager_role)

    def test_create_user_and_login(self):
        # Log in as the superuser
        self.selenium.get(self.live_server_url + '/admin/')
        username_input = self.selenium.find_element(By.NAME, 'username')
        password_input = self.selenium.find_element(By.NAME, 'password')
        username_input.send_keys('admin')
        password_input.send_keys('adminpassword')
        password_input.send_keys(Keys.RETURN)

		# Navigate to the create user page
        self.selenium.get(self.live_server_url + '/accounts/register/')

        # Create a normal user through the application's create user page
        username_input = self.selenium.find_element(By.NAME, 'username')
        name_input = self.selenium.find_element(By.NAME, 'employee_name')
        email_input = self.selenium.find_element(By.NAME, 'email')
        phone_input = self.selenium.find_element(By.NAME, 'phone')
        password1_input = self.selenium.find_element(By.NAME, 'password1')
        password2_input = self.selenium.find_element(By.NAME, 'password2')
 

        username_input.send_keys('newuser')
        name_input.send_keys('john')
        email_input.send_keys('newuser@example.com')
        phone_input.send_keys('555555')
        password1_input.send_keys('cL345214')
        password2_input.send_keys('cL345214')    
        password2_input.send_keys(Keys.RETURN)

        # Log out the superuser
        self.selenium.get(self.live_server_url + '/admin/logout/')
        self.selenium.get(self.live_server_url)
        #time.sleep(10)
        # Log in as the newly created user
        self.selenium.get(self.live_server_url + '/accounts/login/?next=/user/')

        username_input = self.selenium.find_element(By.NAME, 'username')
        password_input = self.selenium.find_element(By.NAME, 'password')
        username_input.send_keys('newuser')
        password_input.send_keys('cL345214')
        password_input.send_keys(Keys.RETURN)

        # Check if the login was successful
        body_text = self.selenium.find_element(By.TAG_NAME, 'h3').text
        self.assertIn('Welcome, john', body_text)

        # Check if the user is redirected to the expected page after login
        self.assertEqual(self.selenium.current_url, self.live_server_url + '/user/')