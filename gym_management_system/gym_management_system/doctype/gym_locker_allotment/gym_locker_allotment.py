# Copyright (c) 2024, Rohit and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class GymLockerAllotment(Document):
	pass
@frappe.whitelist()
def update_locker_status(locker_number):
    frappe.msgprint("Yes IT's Working")
    console.log("Yes Working")
    try:
        # Update locker status in Gym Locker Booking DocType
        frappe.db.set_value("Gym Locker Booking", {"locker_number": locker_number}, "locker_status", "occupied")

        # Update locker status in Locker DocType (assuming the locker number is the name of the Locker DocType)
        frappe.db.set_value("Locker", locker_number, "status", "occupied")

        return True, f"Locker {locker_number} status updated to 'occupied' successfully"
    except Exception as e:
        return False, str(e)
