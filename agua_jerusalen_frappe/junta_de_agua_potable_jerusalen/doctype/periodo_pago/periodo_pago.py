# Copyright (c) 2022, Luis Pillaga and contributors
# For license information, please see license.txt

# import frappe
import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import now
from datetime import datetime, date


class PeriodoPago(Document):

    def before_save(self):
        """Set days billed"""
        start_date = datetime.strptime(self.start_date, '%Y-%m-%d')
        end_date = datetime.strptime(self.end_date, '%Y-%m-%d')

        self.days_billed = (end_date - start_date).days + 1

    def after_insert(self):
        """Create new reading for each water meter"""
        default_uom = frappe.db.get_single_value(
            'Configuracion Junta', 'uom')

        if not default_uom:
            frappe.throw(_('Por favor selecccione una UOM en Configuracion Junta'))

        water_meters = frappe.get_all("Medidor", filters={
            'is_active': 1
        }, fields=['name', 'actual_reading'])

        for water_meter in water_meters:
            actual_reading = water_meter.actual_reading
            customer = frappe.get_value("Medidor", water_meter.name, 'customer')

            if not actual_reading:
                actual_reading = 0

            new_measurement = frappe.new_doc('Medicion')
            new_measurement.water_meter = water_meter.name
            new_measurement.customer = customer
            new_measurement.previous_reading = actual_reading
            new_measurement.actual_reading = actual_reading
            new_measurement.uom = default_uom
            new_measurement.operator = frappe.session.user
            new_measurement.period = self.name
            new_measurement.total_consume = 0
            new_measurement.read_at = now()

            new_measurement.insert()
