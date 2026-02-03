# Copyright (c) 2026, me and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
import re
import frappe


class AirplaneCrewMember(Document):

	def validate(self):

		# Make sure the crew member ID follows exactly 'CREW-XXXX' 
		if self.employee_id:
			if not re.match(r"^CREW-\d{4}$", self.employee_id):
				frappe.throw(("Employee ID must be in the format 'CREW-0000' (e.g., CREW-1234)"))

		if self.full_name:
			self.full_name = self.full_name.title()