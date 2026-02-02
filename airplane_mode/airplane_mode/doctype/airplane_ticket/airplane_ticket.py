# Copyright (c) 2026, me and contributors
# For license information, please see license.txt

from frappe.model.document import Document
import frappe
import random


class AirplaneTicket(Document):
    def validate(self):
        """
        Validates the Airplane Ticket before saving:
        1. Assigns a random seat (row 1-100, A-E) if not already set.
        2. Removes duplicate Add-ons.
        3. Calculates Total Amount (Flight Price + Add-ons).
        4. Checks flight capacity to prevent overbooking.
        """
        
        if not self.seat:
            random_int = random.randint(1, 100)
            random_letter = random.choice(['A', 'B', 'C', 'D', 'E'])
            self.seat = f"{random_int}{random_letter}"

        seen_items = set()
        unique_rows = [] 
        if self.add_ons:
            for row in self.add_ons: 
                if row.item not in seen_items:
                    unique_rows.append(row)
                    seen_items.add(row.item)
            self.add_ons = unique_rows

        total = self.flight_price or 0.0
        if self.add_ons:
            for item in self.add_ons:
                total += item.amount
        self.total_amount = total

        flight = frappe.get_doc("Airplane Flight", self.flight)
        airplane = frappe.get_doc("Airplane", flight.airplane)
        capacity = airplane.capacity
        
        existing_tickets = frappe.db.count("Airplane Ticket", 
            filters={
                "flight": self.flight
            }
        )
        
        if self.is_new() and existing_tickets >= capacity:
            frappe.throw(f"Cannot book ticket. The flight is full! (Capacity: {capacity})")

    def before_submit(self): 
        if self.status != "Boarded": 
            frappe.throw("You cannot submit this ticket because the status is not 'Boarded'. ")