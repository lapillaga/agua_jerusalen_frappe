# Copyright (c) 2022, Luis Pillaga and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe import _


class Medicion(Document):
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
