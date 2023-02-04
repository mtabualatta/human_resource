# Copyright (c) 2023, mtabualatta and contributors
# For license information, please see license.txt
import datetime
import frappe
from frappe.model.document import Document
from datetime import datetime, timedelta


class Employee(Document):
	def validate(self):
		self.diff_date()
		self.con_full_name()
		self.validate_status_and_age()
		self.validate_mobile_number()
		self.validate_employee_education()



	def diff_date(self):
		age = frappe.utils.date_diff(frappe.utils.getdate(frappe.utils.today), self.date_of_birth) /365.25
		self.age = int(age)


	def con_full_name(self):
		self.full_name = self.first_name + " " + self.middle_name + " " + self.last_name

	def validate_status_and_age(self):
		if self.age > 60 and self.status == 'Active':
			frappe.throw('The Employee is over the age of 60 Can\'t  have an Active status.')

	def validate_mobile_number(self):
		# Check if the mobile field is not empty
		if self.employee_number:
			# Check if the length of the mobile field is 10
			if len(self.employee_number) != 10:
				frappe.throw("Mobile field must contain 10 numbers")
			# Check if the first 3 characters of the mobile field is 059
			if self.employee_number[:3] != "059":
				frappe.throw("Mobile field must start with 059")

	def validate_employee_education(self):
			if len(self.employee_education) < 2:
				frappe.throw("An employee must have at least two education records")