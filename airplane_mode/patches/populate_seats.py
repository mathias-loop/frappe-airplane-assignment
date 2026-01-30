import frappe
import random

def execute():
    # 1. Fetch all Airplane Tickets where the 'seat' field is empty or null
    tickets = frappe.db.get_all(
        "Airplane Ticket",
        filters={"seat": ["is", "not set"]},
        pluck="name"
    )

    # 2. Loop through each ticket
    for ticket_name in tickets:
        # 3. Generate the random seat (same logic as before)
        random_int = random.randint(1, 100)
        random_letter = random.choice(['A', 'B', 'C', 'D', 'E'])
        new_seat = f"{random_int}{random_letter}"

        # 4. Update the database record directly
        frappe.db.set_value("Airplane Ticket", ticket_name, "seat", new_seat)