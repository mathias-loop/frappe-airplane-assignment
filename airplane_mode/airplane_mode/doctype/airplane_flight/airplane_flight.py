# Copyright (c) 2026, me and contributors
# For license information, please see license.txt

# import frappe
from frappe.website.website_generator import WebsiteGenerator

from frappe.model.document import Document



class AirplaneFlight(WebsiteGenerator):
	pass

	def on_submit(self): 
		self.status = "Completed"
		self.db_set("status", "Completed")