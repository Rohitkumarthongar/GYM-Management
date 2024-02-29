import frappe
from frappe.model.document import Document

class GymMemberRecords(Document):
    @frappe.whitelist()
    def bmi(weight_kg, height_m):
        return weight_kg / (height_m ** 2)
