# Copyright (c) 2022, Luis Pillaga and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


@frappe.whitelist()
def get_mingas():
	return frappe.get_all('Minga', fields=['*'])


class Minga(Document):
	pass
