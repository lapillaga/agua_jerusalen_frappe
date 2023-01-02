# Copyright (c) 2022, Luis Pillaga and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe import _
from frappe.utils import now
from frappe.utils import add_days


class Medicion(Document):

    def before_submit(self):
        """Create water bill and also update water meter reading"""
        water_meter = frappe.get_doc('Medidor', self.water_meter)
        water_meter.actual_reading = self.actual_reading
        water_meter.save()

        water_bill = frappe.new_doc('Planilla')
        customer = frappe.get_doc('Customer', self.customer)
        water_bill.customer = customer.name

        period = frappe.get_doc('Periodo Pago', self.period)
        water_bill.issue_date = now()
        water_bill.start_date = period.start_date
        water_bill.days_billed = period.days_billed
        water_bill.paid = False

        rate = frappe.get_doc('Tarifa', water_meter.rate)
        water_bill.base_price = rate.amount
        water_bill.water_meter = water_meter.name

        expiration_date = add_days(now(), rate.grace_days)
        water_bill.expiration_date = expiration_date
        water_bill.end_date = period.end_date
        water_bill.rate = rate.name
        water_bill.billed = False
        water_bill.penalty_price = rate.penalty

        excess_amount = self.excess_consume * rate.penalty
        water_bill.excess_amount = excess_amount

        total = excess_amount + rate.amount
        water_bill.total = total

        barrio = frappe.get_doc('Barrio', water_meter.neighborhood)
        default_address = frappe.db.get_single_value(
            'Configuracion Junta', 'default_address')
        water_bill.address = default_address + ', ' + barrio.description

        water_bill.measurement = self.name
        water_bill.save()

        self.completed_at = now()

    @frappe.whitelist()
    def get_excess_consume(self, throw_if_missing=False, **kwargs):
        """Calculate the excess consume"""
        water_meter_name: str = kwargs.get('water_meter_name')
        total_consume: int = kwargs.get('total_consume')

        rate_name = frappe.get_value("Medidor", water_meter_name, 'rate')
        rate = frappe.get_doc('Tarifa', rate_name)

        if not rate and throw_if_missing:
            frappe.throw(_('El medidor seleccionado no tiene una tarifa asignada'))

        excess_consume = 0
        if total_consume > rate.max:
            excess_consume = total_consume - rate.max

        return excess_consume
