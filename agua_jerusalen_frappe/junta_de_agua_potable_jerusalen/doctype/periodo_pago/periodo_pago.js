// Copyright (c) 2022, Luis Pillaga and contributors
// For license information, please see license.txt

frappe.ui.form.on('Medicion', {
    measurements_add(frm, cdt, cdn) {
        frappe.msgprint('A row has been added to the links table 🎉 ');
    }
});

frappe.ui.form.on('Periodo Pago', {
    before_load(frm) {
        console.log("before_load");
        console.log(frm);
        // write setup code
    }
});

frappe.ui.form.on("Medicion", "water_meter", function(frm, cdt, cdn) { // notice the presence of cdt and cdn
    console.log('water_meter');
});