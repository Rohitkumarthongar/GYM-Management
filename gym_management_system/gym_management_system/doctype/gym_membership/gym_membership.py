# Copyright (c) 2024, Rohit and contributors
# For license information, please see license.txt

import frappe
# from __future__ import unicode_literals
from frappe.model.document import Document
import json
from datetime import datetime
from frappe.model.docstatus import DocStatus


class GymMembership(Document):
    def after_save(self):
        # Call the create_user method after the document is saved
        self.create_user()

    @frappe.whitelist(allow_guest=True)
    def create_user(self):
        data = json.loads(frappe.request.data)
        name = frappe.db.get_value("Gym Membership", {"name": data.get("membership_name")}, "name")

        if not name:
            return {"error": "Gym Membership not found."}

        password = 1827  

        email = data.get("email")
        existing_user = frappe.db.get_value("User", {"email": email})
        if existing_user:
            frappe.throw(_("A user with the same email already exists."))

        full_name = data.get("member_name")
        if not full_name:
            return {"error": "Full name is required."}

        first_name, *last_name = full_name.split(maxsplit=1)

        try:
            birth_date = datetime.strptime(data.get("date_of_birth"), "%d-%m-%Y").strftime("%Y-%m-%d")
        except ValueError:
            return {"error": "Invalid date format for date_of_birth. Please provide the date in DD-MM-YYYY format."}

        user = frappe.new_doc("User")
        user.email = email.lower()
        user.first_name = first_name
        user.last_name = last_name[0] if last_name else ""
        user.gender = data.get("gender")
        user.mobile_no = data.get("mobile_number")
        user.birth_date = birth_date
        user.update(data)  

        user.password = password

        try:
            user.save(ignore_permissions=True)
            frappe.db.commit()
            return {"message": "User created successfully."}
        except Exception as e:
            frappe.log_error(frappe.get_traceback(), "User Creation Failed")
            return {"error": f"Failed to create user: {str(e)}"}
