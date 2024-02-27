import frappe
from frappe.model.document import Document

class GymMemberRecords(Document):
    pass

    @frappe.whitelist()
    def member(self):
        frappe.msgprint("Yes, You are ")
        print("************************Print Statement *******************************")
        if self.docfield_name:
            # Fetch the name based on the selected value
            name = frappe.db.get_value("Gym Membership", {"member": self.docfield_name}, "name")
            # Update the name field with the fetched name
            self.member_name = name
            self.save() 

    @staticmethod
    def bmi(weight_kg, height_m):
        """
        Calculate Body Mass Index (BMI) using weight (in kilograms) and height (in meters).
        """
        return weight_kg / (height_m ** 2)
