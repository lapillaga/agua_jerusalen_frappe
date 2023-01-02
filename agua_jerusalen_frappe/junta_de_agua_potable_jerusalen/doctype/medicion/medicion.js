// Copyright (c) 2022, Luis Pillaga and contributors
// For license information, please see license.txt

frappe.ui.form.on("Medicion", {
	// refresh: function(frm) {

	// }
});

frappe.ui.form.on("Medicion", "actual_reading", function(frm) {
    let total_consumption = calculateTotalConsume(frm);
    frm.set_value('total_consume', total_consumption);
    setExcessConsume(frm, total_consumption);
});

frappe.ui.form.on("Medicion", "previous_reading", function(frm) {
    let total_consumption = calculateTotalConsume(frm);
    frm.set_value('total_consume', total_consumption);
    setExcessConsume(frm, total_consumption);
});

function calculateTotalConsume(frm) {
    // Calculate and set consume
    let total_consumption = frm.doc.actual_reading - frm.doc.previous_reading;

    if (frm.doc.actual_reading < frm.doc.previous_reading) {
        frappe.msgprint("El valor actual no puede ser menor que el valor anterior");
        frm.doc.actual_reading = frm.doc.previous_reading;
        return;
    }

    return total_consumption;
}

function setExcessConsume(frm, total_consumption) {
    frm.call('get_excess_consume', {
        water_meter_name: frm.doc.water_meter,
        total_consume: total_consumption,
        throw_if_missing: true
    }).then(r => {
        let excess_consume = r.message;
        frm.set_value('excess_consume', excess_consume);
    });
}