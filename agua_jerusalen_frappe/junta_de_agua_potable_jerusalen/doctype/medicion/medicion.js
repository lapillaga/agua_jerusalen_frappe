// Copyright (c) 2022, Luis Pillaga and contributors
// For license information, please see license.txt

frappe.ui.form.on('Medicion', {
	// refresh: function(frm) {

	// }
});

frappe.ui.form.on("Medicion", "actual_reading", function(frm) {
    console.log('actual_reading');
});