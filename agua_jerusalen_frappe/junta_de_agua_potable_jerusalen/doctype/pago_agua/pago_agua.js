// Copyright (c) 2023, Luis Pillaga and contributors
// For license information, please see license.txt

frappe.ui.form.on('Pago Agua', {
	// refresh: function(frm) {

	// }
});

frappe.ui.form.on("Pago Agua", "total_bill", function(frm) {
    let total = calculateTotal(frm);
    frm.set_value('total', total);
});

frappe.ui.form.on("Pago Agua", "total_excess", function(frm) {
    let total = calculateTotal(frm);
    frm.set_value('total', total);
});

function calculateTotal(frm) {
    // Calculate and set consume
    return  frm.doc.total_bill + frm.doc.total_excess;
}