// Copyright (c) 2022, Luis Pillaga and contributors
// For license information, please see license.txt

frappe.ui.form.on('Medicion', {
    measurements_add(frm, cdt, cdn) {
        frappe.msgprint('A row has been added to the links table 🎉 ');
    }
});

// frappe.ui.form.on('Periodo Pago', {
//     before_load(frm) {
//         console.log("before_load");
//         console.log(frm);
//         // write setup code
//     }
// });

frappe.ui.form.on("Medicion", "actual_reading", function(frm, cdt, cdn) {
    let row = locals[cdt][cdn];
    let total_consumption = row.actual_reading - row.previous_reading;

    if (row.actual_reading < row.previous_reading) {
        frappe.msgprint("El valor actual no puede ser menor que el valor anterior");
        row.actual_reading = row.previous_reading;
        return;
    }

    frappe.model.set_value(
        cdt,
        cdn,
        'total_consume',
        total_consumption
    );
});

// frappe.ui.form.on("Medicion", "water_meter", function(frm, cdt, cdn) {
//     console.log('water_meter');
//     // frm.call('get_last_reading', { throw_if_missing: true })
//     //     .then(r => {
//     //         console.log(r);
//     //         // do something with r
//     //     }
//     // );
// });