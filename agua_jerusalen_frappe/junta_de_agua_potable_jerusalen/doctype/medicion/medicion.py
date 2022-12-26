# Copyright (c) 2022, Luis Pillaga and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe import _
from frappe.utils import now


class Medicion(Document):

	def before_submit(self):
		"""Create water bill"""
		import pdb
		pdb.set_trace()
		customer = frappe.get_value("Medidor", self.customer.name, 'customer')
		print(self)
		print(customer)
		print(self.water_meter)
		frappe.throw(_('En desarrollo'))

	# water_bill = frappe.new_doc('Planilla')
		# water_bill.customer = self.customer
		# water_bill.issue_date = now()
		# water_bill.start_date =
		# water_bill.days_billed =
		# water_bill.paid = False
		# water_bill.base_price =
		# water_bill.amount =
		# water_bill.water_meter = self.water_meter
		# water_bill.expiration_date =
		# water_bill.end_date =
		# water_bill.rate =
		# water_bill.billed = False
		# water_bill.penalty_price =
		# water_bill.excess_amount =
		# water_bill.total =
		# water_bill.save()


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
