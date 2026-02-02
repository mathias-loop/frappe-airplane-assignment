// Copyright (c) 2026, me and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Airplane Ticket", {
// 	refresh(frm) {

// 	},
// });

frappe.ui.form.on('Airplane Ticket', {
    refresh(frm) {
        frm.add_custom_button('Assign Seat', () => {
            frappe.prompt([
                {
                    label: 'Seat Number',
                    fieldname: 'seat',
                    fieldtype: 'Data',
                    reqd: 1
                }
            ], 
            (values) => {
                // Clean the input (remove spaces, make uppercase)
                let seat = values.seat.trim().toUpperCase();
                
                // Validate format using Regex (Number + Letter) 
                // Number between 1 - 100 
                // Letter between A - F 
                let match = seat.match(/^(\d+)([A-F])$/);

                if (!match) {
                    frappe.throw("Invalid Seat format! Use a number followed by a letter (e.g., 12A).");
                }

                // Extract parts
                let row = parseInt(match[1]);

                // Validate Row range (1 to 100)
                if (row < 1 || row > 100) {
                    frappe.throw("Row number must be between 1 and 100.");
                }

                // If all good, set the value
                frm.set_value('seat', seat);
            },
            'Select Seat',
            'Assign'
            );
        }, 'Actions');
    }
});