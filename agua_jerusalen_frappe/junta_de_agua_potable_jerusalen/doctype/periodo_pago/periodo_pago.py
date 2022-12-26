# Copyright (c) 2022, Luis Pillaga and contributors
# For license information, please see license.txt

# import frappe
import frappe
from frappe.model.document import Document
from frappe.utils import now

from frappe import _


class PeriodoPago(Document):

	def before_insert(self):
		"""Create new reading for each water meter"""
		default_uom = frappe.db.get_single_value(
			'Configuracion Junta', 'uom')

		water_meters = frappe.get_all("Medidor", filters={
			'is_active': 1
		})

		for water_meter in water_meters:
			actual_reading = water_meter.actual_reading

			if not actual_reading:
				actual_reading = 0

			self.append('measurements', {
				'read_at': now(),
				'water_meter': water_meter.name,
				'previous_reading': actual_reading,
				'actual_reading': actual_reading,
				'total_consume': 0,
				'operator': frappe.session.user,
				'uom': default_uom
			})

	def on_update(self):
		"""Update payment period status"""
		pass
		# for measurement in self.measurements:
		# 	try:
		# 		water_bill = frappe.get_doc('Planilla', {
		# 			'periodo_pago': self.name,
		# 			'medidor': measurement.water_meter
		# 		})
		# 		water_bill.status = self.status
		# 		water_bill.save()
		# 	except frappe.DoesNotExistError:
		# 		pass
		#
		#
		# 	already_exists = frappe.db.exists('Planilla', {
		# 		'periodo_pago': self.name,
		# 		'medidor': measurement.water_meter
		# 	})
		#
		# 	if already_exists:
		# 		water_bill = frappe.get_doc('Planilla', already_exists)
		#
		#
		# 	frappe.get_doc({
		# 		'doctype': 'Planilla',
		# 		'periodo_pago': self.name,
		# 		'medidor': measurement.water_meter,
		# 		'previous_reading': measurement.previous_reading,
		# 		'actual_reading': measurement.actual_reading,
		# 		'total_consume': measurement.total_consume,
		# 		'operator': measurement.operator,
		# 		'uom': measurement.uom
		# 	}).insert()
		# 	frappe.db.exists("User", "jane@example.org", cache=True)
		#
		# 	if measurement.is_completed:
		# 		measurement.completed_at = now()
		#
		#
		#




	# @frappe.whitelist()
	# def get_last_reading(self, throw_if_missing=False):
	# 	"""Get last measurement for this water meter"""
	# 	print(self)
	# 	last_measurement = frappe.db.get_value(
	# 		'Medidor', self.water_meter, 'actual_reading'
	# 	)
	#
	# 	if not last_measurement:
	# 		if throw_if_missing:
	# 			frappe.throw(_("No hay mediciones para este cliente"))
	# 		return None
	#
	# 	return last_measurement[0]