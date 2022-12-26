// Copyright (c) 2022, Luis Pillaga and contributors
// For license information, please see license.txt

frappe.ui.form.on('Medicion', {
	// refresh: function(frm) {

	// }
});

frappe.ui.form.on("Medicion", "actual_reading", function(frm) {
    let total_consumption = frm.doc.actual_reading - frm.doc.previous_reading;

    if (frm.doc.actual_reading < frm.doc.previous_reading) {
        frappe.msgprint("El valor actual no puede ser menor que el valor anterior");
        frm.doc.actual_reading = frm.doc.previous_reading;
        return;
    }

    frm.set_value('total_consume', total_consumption);
});