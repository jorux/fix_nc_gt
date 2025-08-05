
from __future__ import unicode_literals

import json
from datetime import date, datetime

import frappe
import requests
import xmltodict
from frappe import _
from frappe.utils import get_site_name


@frappe.whitelist()
def descontar_costo (doc, method):
	if doc.is_return == True:
		        frappe.db.set_value("Sales Invoice",{"name":doc.return_against},{"outstanding_amount":"outstanding_amount" + doc.grand_total})
	else:
		pass 
	
@frappe.whitelist()
def contar_costo (doc, method):
	if doc.is_return == True:
		frappe.db.set_value("Sales Invoice",{"name":doc.return_against},{"outstanding_amount":"outstanding_amount" - doc.grand_total})
	else:
		pass 
