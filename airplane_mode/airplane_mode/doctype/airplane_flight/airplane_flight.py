# Copyright (c) 2026, me and contributors
# For license information, please see license.txt

# import frappe
from frappe.website.website_generator import WebsiteGenerator
from frappe.model.document import Document
import frappe



class AirplaneFlight(WebsiteGenerator):
	pass

	def on_submit(self): 
		self.status = "Completed"
		self.db_set("status", "Completed")

	def get_template(self, context): 
		return "airplane_mode/airplane_mode/doctype/airplane_flight/templates/airplane_flight.html"
	
	def before_update_after_submit(self):
		
		frappe.db.set_value(
			"Airplane Ticket",
			{"flight": self.name},
			"gate_number",
			self.gate_number
		)