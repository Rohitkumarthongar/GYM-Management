# Copyright (c) 2024, Rohit and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class GymMembership(Document):
    pass
    # @frappe.whitelist()
    # def calculate_base_tenure_charge(membership_tenure):
    #     base_tenure_charges = 0
    #     if membership_tenure == 'Monthly':
    #         base_tenure_charges = 2000
    #     elif membership_tenure == 'Yearly':
    #         base_tenure_charges = 20000
    #     elif membership_tenure == 'Quarterly':
    #         base_tenure_charges = 7500
    #     elif membership_tenure == 'Half Yearly':
    #         base_tenure_charges = 11000        
    #     return base_tenure_charges
