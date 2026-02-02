// Copyright (c) 2026, me and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Airline", {
// 	refresh(frm) {

// 	},
// });

frappe.ui.form.on('Airline', {
    refresh: function(frm) {
        // Check if the website field has a value
        if (frm.doc.website) {
            // Add a custom button to the form
            frm.add_web_link(frm.doc.website, "Visit Website");
        }
    }
});