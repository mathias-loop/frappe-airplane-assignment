import frappe

def execute():
    passengers = frappe.db.get_all("Flight Passenger", pluck="name")
    for name in passengers:
        doc = frappe.get_doc("Flight Passenger", name)
        doc.save()
    frappe.db.commit()