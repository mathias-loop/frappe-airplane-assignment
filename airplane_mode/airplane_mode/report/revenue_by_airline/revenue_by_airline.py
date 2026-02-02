# Copyright (c) 2026, me and contributors
# For license information, please see license.txt

# import frappe


import frappe

import frappe

def execute(filters=None):
    # Define Columns
    columns = [
        {
            "fieldname": "airline",
            "label": "Airline",
            "fieldtype": "Link",
            "options": "Airline",
            "width": 200
        },
        {
            "fieldname": "revenue",
            "label": "Revenue",
            "fieldtype": "Currency",
            "width": 150
        }
    ]

    # Fetch Data efficiently (No nested joins)
    
    # Get all Airlines (So we include even those with 0 revenue)
    airlines = frappe.get_all("Airline", fields=["name"])
    
    # Get mapping: Airplane -> Airline
    airplanes = frappe.get_all("Airplane", fields=["name", "airline"])
    airplane_to_airline = {row.name: row.airline for row in airplanes}

    # Get mapping: Flight -> Airplane
    flights = frappe.get_all("Airplane Flight", fields=["name", "airplane"])
    flight_to_airplane = {row.name: row.airplane for row in flights}

    # Get all Submitted Tickets
    tickets = frappe.get_all(
        "Airplane Ticket",
        fields=["total_amount", "flight"],
        filters={"docstatus": 1}
    )

    # Process Logic (Python)
    revenue_map = {a.name: 0 for a in airlines} # Initialize 0s

    for ticket in tickets:
        # Find the flight for this ticket
        flight_name = ticket.flight
        if not flight_name: continue

        # Find the airplane for that flight
        airplane_name = flight_to_airplane.get(flight_name)
        if not airplane_name: continue

        # Find the airline for that airplane
        airline_name = airplane_to_airline.get(airplane_name)
        
        # Add revenue if airline exists
        if airline_name and airline_name in revenue_map:
            revenue_map[airline_name] += ticket.total_amount or 0

    # Prepare Final Data List
    data = []
    total_revenue = 0
    
    for airline, revenue in revenue_map.items():
        data.append({
            "airline": airline,
            "revenue": revenue
        })
        total_revenue += revenue

    # Chart Configuration
    chart = {
        "data": {
            "labels": [x["airline"] for x in data],
            "datasets": [{"values": [x["revenue"] for x in data]}]
        },
        "type": "donut"
    }

    # Summary Block
    report_summary = [
        {
            "value": total_revenue,
            "indicator": "Green",
            "label": "Total Revenue",
            "datatype": "Currency",
        }
    ]

    return columns, data, None, chart, report_summary