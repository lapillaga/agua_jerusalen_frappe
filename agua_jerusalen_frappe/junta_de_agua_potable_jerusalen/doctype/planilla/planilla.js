// Copyright (c) 2022, Luis Pillaga and contributors
// For license information, please see license.txt

frappe.ui.form.on('Planilla', {
	// refresh: function(frm) {

	// }
});

frappe.ui.form.on('Planilla', {
    refresh: function(frm) {
        frm.add_custom_button(__('Pagar'), function() {
            frappe.confirm(
                __('¿Está seguro de que desea pagar esta planilla?'),
                function() {
                    validateIfPaymentExists(frm);
                }
            )
        }).addClass("btn-primary");
    }
});

function validateIfPaymentExists(frm) {
    frappe.db.get_value('Pago Agua', {
        bill: frm.doc.name
    }, 'name').then(response => {
        if (response.message.name) {
            frappe.msgprint('Ya existe un pago para esta planilla');
            frappe.set_route('Form', 'Pago Agua', response.message.name);
            throw 'Ya existe un pago para esta planilla';
        } else {
            create_payment(frm);
        }
    });
}

function create_payment(frm) {
    frappe.db.insert({
        doctype: 'Pago Agua',
        customer: frm.doc.customer,
        bill: frm.doc.name,
        water_meter: frm.doc.water_meter,
        address: frm.doc.address,
        user: frappe.session.user,
        total: frm.doc.base_price + frm.doc.excess_amount,
    }).then(doc => {
        if (doc) {
            frappe.set_route('Form', 'Pago Agua', doc.name);
        }
    });
}