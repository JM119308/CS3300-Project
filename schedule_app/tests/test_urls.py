from django.test import SimpleTestCase
from django.urls import reverse, resolve
from schedule_app.views import EmployeeListView, EmployeeDetailView

class TestUrls(SimpleTestCase):

	def test_employees_url_is_resolved(self):

		url = reverse('employees')

		

		self.assertEquals(resolve(url).func.view_class, EmployeeListView)

		url = reverse('employee-detail', args=['1'])

	

		self.assertEquals(resolve(url).func.view_class, EmployeeDetailView)