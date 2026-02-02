# Copyright (c) 2026, me and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
import frappe
import random


class AirplaneTicket(Document):
	pass

	def before_save(self):
		total = self.flight_price or 0.0

		# Add the total cost of all the items. 
		if self.add_ons:
			for item in self.add_ons:
				total += item.amount
		
		self.total_amount = total
	
	def validate(self): 
		# Removes duplicate items from the add-ons table 

		# Creating a checklist to keep track of items we have seen 
		seen_items = set()
		unique_rows = [] 

		# Loop through the current add-ons 
		for row in self.add_ons: 
			if row.item not in seen_items:
				unique_rows.append(row)
				seen_items.add(row.item)

		self.add_ons = unique_rows
	
	def before_submit(self): 
		if self.status != "Boarded": 
			frappe.throw("You cannot submit this ticket because the status is not 'Boarded'. ")

	def before_save(self): 
		# Creates a random seat placement from rows 1-100 and a random column A-E
		random_int = random.randint(1, 100)
		random_letter = random.choice(['A', 'B', 'C', 'D', 'E'])
		self.seat = f"{random_int}{random_letter}"

	def validate(self):
		# Get the connected Airplane Flight
		flight = frappe.get_doc("Airplane Flight", self.flight)
		
		# Get the Airplane linked to that flight to see its capacity
		airplane = frappe.get_doc("Airplane", flight.airplane)
		capacity = airplane.capacity
		
		# Count how many tickets already exist for this flight
		existing_tickets = frappe.db.count("Airplane Ticket", 
			filters={
				"flight": self.flight
			}
		)
		
		# Check capacity (Only checks on creation of NEW tickets to avoid blocking edits)
		if self.is_new() and existing_tickets >= capacity:
			frappe.throw(f"Cannot book ticket. The flight is full! (Capacity: {capacity})")