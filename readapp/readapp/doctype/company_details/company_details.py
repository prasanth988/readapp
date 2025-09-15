# Copyright (c) 2025, prasanth and contributors
# For license information, please see license.txt

# import frappe
# from frappe.model.document import Document


# class CompanyDetails(Document):
# 	def validate(self):
# 		frappe.msgprint("this is validate function")

# import frappe
# from frappe.model.document import Document

# class CompanyDetails(Document):
#     def validate(self):
#         full_name = self.first_name + " " + self.last_name
#         frappe.msgprint(full_name)

import frappe
from frappe.model.document import Document

class CompanyDetails(Document):

    def crete_user(self):
        pass
    # def validate(self):
    #     self.get_document()
        
