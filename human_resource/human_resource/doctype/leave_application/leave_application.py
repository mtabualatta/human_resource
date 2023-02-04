# Copyright (c) 2023, mtabualatta and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class LeaveApplication(Document):

	def validate(self):
		self.set_total_leave_days()
		self.check_leave_balance()



	def set_total_leave_days(self):
		total_leave_days=0
		if self.from_date and self.to_date:
			total_leave_days = frappe.utils.date_diff(self.to_date,self.from_date)+1
		if total_leave_days >=0:
			self.total_leave_days = total_leave_days


	def check_leave_balance(self):
		if self.employee and self.leave_type and self.from_date and self.to_date:
			leave_balance = frappe.db.sql(""" SELECT total_leaves_allocated FROM `tabLeave Allocation` 
			where employee = %s and leave_type = %s and from_date <= %s and to_date >= %s""",
										 (self.employee, self.leave_type, self.from_date, self.to_date), as_dict=1)
		if leave_balance:
			self.leave_balance_before_application = leave_balance[0].total_leaves_allocated