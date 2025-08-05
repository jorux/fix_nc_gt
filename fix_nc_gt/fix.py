
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
		"custom logic here"
	else
	
@frappe.whitelist()
def contar_costo (doc, method):
	if doc.is_return == True:
		"custom logic here"
	else
