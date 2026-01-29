# Copyright (c) 2026, me and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class FlightPassenger(Document):
	pass

	def before_save(self):
		self.full_name = f"{self.first_name} {self.last_name}"
