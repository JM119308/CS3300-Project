from selenium import webdriver
from django.test import LiveServerTestCase
from schedule_app.models import *
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test import TestCase, Client
from django.contrib.auth.models import User, Group
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from django.urls import reverse
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class UserCreationTest(LiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = webdriver.Chrome()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def setUp(self):
        # Create an existing superuser with the manager_role
        self.superuser = User.objects.create_superuser('admin', 'admin@example.com', 'adminpassword')
        self.manager_role = Group.objects.create(name='manager_role')
        self.employee_role = Group.objects.create(name='employee_role')
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

        time.sleep(5)
        # Check if the login was successful
        body_text = self.selenium.find_element(By.TAG_NAME, 'h3').text
        self.assertIn('Welcome, john', body_text)

        # Check if the user is redirected to the expected page after login
        self.assertEqual(self.selenium.current_url, self.live_server_url + '/user/')


class TestCreateWeekAndSchedule(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = webdriver.Chrome()
        cls.selenium.implicitly_wait(10)


    def setUp(self):
        # Create an existing superuser with the manager_role
        self.superuser = User.objects.create_superuser('admin', 'admin@example.com', 'adminpassword')
        self.manager_role = Group.objects.create(name='manager_role')
        self.superuser.groups.add(self.manager_role)

    def test_create_week_and_schedule(self):
        # Log in as the superuser
        self.selenium.get(self.live_server_url + '/admin/')
        username_input = self.selenium.find_element(By.NAME, 'username')
        password_input = self.selenium.find_element(By.NAME, 'password')
        username_input.send_keys('admin')
        password_input.send_keys('adminpassword')
        password_input.send_keys(Keys.RETURN)

        #register new user

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
        # Navigate to create week page

        self.selenium.get(self.live_server_url + '/week/create_week')
        
        # Fill out the create week form
        week_date_input = self.selenium.find_element(By.NAME, 'weekDate')
        week_date_input.send_keys('Nov 12 - Nov 18')  # Provide a valid date
        create_week_button = self.selenium.find_element(By.CSS_SELECTOR, '[type="submit"]')
        create_week_button.click()
        
       

        # Navigate to create schedule page
        self.selenium.get(self.live_server_url + '/week/1')  # Assuming 1 is a valid week ID
        

        self.selenium.get(self.live_server_url + '/week/1/create_schedule')
        # Fill out the create schedule form

        # Locate the dropdown element
        week_dropdown = self.selenium.find_element(By.NAME, 'week')  # Replace 'your_dropdown_id' with the actual ID of your dropdown

        # Create a Select object
        dropdown = Select(week_dropdown)

        # Select by visible text
        dropdown.select_by_visible_text('Nov 12 - Nov 18')

        employee_dropdown = self.selenium.find_element(By.NAME, 'employee')
        dropdown = Select(employee_dropdown)

        dropdown.select_by_visible_text('john')

        sunday_start = self.selenium.find_element(By.NAME, 'sunday_start')

        dropdown = Select(sunday_start)
        dropdown.select_by_visible_text('09:00')

        sunday_end = self.selenium.find_element(By.NAME, 'sunday_end')

        dropdown = Select(sunday_end)
        dropdown.select_by_visible_text('17:00')

        # Select by index (index starts from 0)
        #dropdown.select_by_index(1)  # Selects the second option

        # Select by value
        #dropdown.select_by_value('option_value')  # Replace 'option_value' with the actual value attribute of the option


        # Submit the form
        create_schedule_button = self.selenium.find_element(By.CSS_SELECTOR, '[type="submit"]')
        create_schedule_button.click()
        time.sleep(5)

        # Check if the employee was added to schedule
        body_text = self.selenium.find_element(By.TAG_NAME, 'h5').text
        self.assertIn('john', body_text)

        sunday_start_element = self.selenium.find_element(By.XPATH, "//div[@class='col border black-line text-truncate scrollable-content']//span[contains(text(), '09:00')]")

        # Get the text content of the element
        sunday_start_text = sunday_start_element.text

        # Assert that the expected text is present in the element's content
        self.assertIn('09:00', sunday_start_text)

        sunday_end_element = self.selenium.find_element(By.XPATH, "//div[@class='col border black-line text-truncate scrollable-content']//span[contains(text(), '17:00')]")

        # Get the text content of the element
        sunday_end_text = sunday_end_element.text

        # Assert that the expected text is present in the element's content
        self.assertIn('17:00', sunday_end_text)

        # Check if the user is redirected to the expected page after creation
        self.assertEqual(self.selenium.current_url, self.live_server_url + '/week/1')
