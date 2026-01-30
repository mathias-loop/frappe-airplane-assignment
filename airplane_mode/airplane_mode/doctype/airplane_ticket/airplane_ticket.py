# Copyright (c) 2026, me and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class AirplaneTicket(Document):
	pass

	def before_save(self):
		total = self.flight_price or 0.0

		# Add the total cost of all the items. 
		if self.add_ons:
			for item in self.add_ons:
				total += item.amount
		
		self.total_amount = total
