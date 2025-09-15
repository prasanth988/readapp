# Copyright (c) 2025, prasanth and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class ArchitectPointsLedger(Document):
	pass



# import frappe
# from frappe.utils import getdate, nowdate
# from datetime import datetime

# def expire_old_points():
#     today = getdate(nowdate())
#     if today.month == 4 and today.day == 1:
#         # Expire all points earned before April 1 of current year
#         expiry_cutoff = datetime(today.year - 1, 3, 31)

#         # Fetch records before expiry date
#         records = frappe.get_all("Points Ledger", 
#             filters={"posting_date": ["<=", expiry_cutoff], "status": "Active"},
#             fields=["name", "architect"]
#         )

#         for record in records:
#             frappe.db.set_value("Points Ledger", record.name, "status", "Expired")
#             frappe.db.set_value("Points Ledger", record.name, "expired_on", today)
        
#         frappe.db.commit()
        



# @frappe.whitelist()
# def calculate_architect_points(doc, method):
#     if doc.architect:
#         points = compute_points(doc)  # మీరు నిర్ణయించే లాజిక్
#         frappe.get_doc({
#             'doctype': 'Architect Points Ledger',
#             'architect': doc.architect,
#             'points': points,
#             'date_earned': frappe.utils.nowdate(),
#             'sales_order': doc.name
#         }).insert()

# import frappe
# from frappe.utils import nowdate

# def calculate_architect_points(doc, method):
#     if not doc.architect:
#         return

#     # Custom logic to compute points
#     # For example: 1 point per ₹10,000 in net total
#     points = doc.net_total // 10000

#     # Update Sales Order custom field
#     frappe.db.set_value("Sales Order", doc.name, "scheme_points", points)

#     # Insert entry in Architect Points Ledger
#     frappe.get_doc({
#         'doctype': 'Architect Points Ledger',
#         'architect': doc.architect,
#         'points': points,
#         'date_earned': nowdate(),
#         'sales_order': doc.name,
#         'status': 'Active'
    # }).insert()
import frappe
from frappe.utils import nowdate

def after_sales_order_submit(doc, method):
    if doc.architect:
        # Logic: 1 point per ₹1000
        points = float(doc.grand_total) / 1000

        ledger = frappe.get_doc({
            "doctype": "Architect Points Ledger",
            "architect": doc.architect,
            "points": points,
            "date_earned": nowdate(),
            "status": "Active",
            "sales_order": doc.name
        })
        ledger.insert(ignore_permissions=True)
        frappe.msgprint(f"🎉 {points} points awarded to Architect {doc.architect}")

# import frappe

# def on_submit(doc, method):
#     if doc.architect:
#         frappe.get_doc({
#             "doctype": "Architect Points Ledger",
#             "architect": doc.architect,
#             "sales_order": doc.name,
#             "points": 10  # or any calculation based on your business logic
#         }).insert(ignore_permissions=True)