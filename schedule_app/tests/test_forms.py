from django.test import SimpleTestCase
from schedule_app.forms import WeekForm

class TestForms(SimpleTestCase):

	def test_week_form_valid_data(self):
		form = WeekForm( data = {
			'weekDate': 'Nov 12 - Nov 18'
		})

		self.assertTrue(form.is_valid())

	def test_expense_form_no_data(self):

		form = WeekForm(data = {})

		self.assertFalse(form.is_valid())
		self.assertEquals(len(form.errors), 1)
