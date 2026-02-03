# Copyright (c) 2026, me and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
import frappe

class AirportShop(Document):
	pass

	def before_insert(self): 
		# Fetch the default rent from Single DocType 'Shop Settings'
		default_rent = frappe.db.get_single_value('Shop Settings', 'default_rent_amount')
		
		# If the user hasn't typed a rent, apply the default
		if not self.rent_amount and default_rent:
			self.rent_amount = default_rent