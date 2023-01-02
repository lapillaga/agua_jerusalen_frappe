# Copyright (c) 2023, Luis Pillaga and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class PagoAgua(Document):
	def before_submit(self):
		"""Set the status of the associated Bill to Submited"""
		bill = frappe.get_doc("Planilla", self.bill)
		bill.paid = True
		bill.save()
		bill.submit()
