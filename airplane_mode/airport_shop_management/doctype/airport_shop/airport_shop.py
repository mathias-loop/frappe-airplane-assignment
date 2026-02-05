# Copyright (c) 2026, me and contributors
# For license information, please see license.txt

# import frappe
from frappe.website.website_generator import WebsiteGenerator
from frappe.model.document import Document
import frappe

class AirportShop(Document):
	pass

	def before_insert(self): 
		default_rent = frappe.db.get_single_value('Shop Settings', 'default_rent_amount')
		if not self.rent_amount and default_rent:
			self.rent_amount = default_rent

	def on_update(self):
		# Triggered every time a shop is saved/updated 
		update_airport_settings(self.airport)

	def on_trash(self):
		# Triggered when a shop is deleted
		update_airport_settings(self.airport)

def update_airport_settings(airport):
    # Calculates shop counts and updates the Airport document
    if not airport: return

    # Count Total Shops for this Airport
    total_shops = frappe.db.count("Airport Shop", filters={"airport": airport})

    # Count Occupied Shops
    occupied_shops = frappe.db.count("Airport Shop", filters={
        "airport": airport,
        "status": "Occupied"
    })

    # Available = Total - Occupied
    available_shops = total_shops - occupied_shops

    # Update the Airport Document
    frappe.db.set_value("Airport", airport, {
        "total_shops": total_shops,
        "occupied_shops": occupied_shops,
        "available_shops": available_shops
    }, update_modified=False)

class AirportShop(WebsiteGenerator):
	pass

	def get_context(self, context): 
		context.no_cache = 1 
		return context