from __future__ import unicode_literals
from frappe.model.document import Document
import frappe
import json
import secrets
from datetime import datetime

@frappe.whitelist(allow_guest=True)
def create_user():
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
    user.role_profile_name = "Gym Member"
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


@frappe.whitelist()
def update_locker_status(locker_number):
    if locker_number:
        try:
            locker_booking = frappe.get_doc("Gym Locker Booking", locker_number)
        except frappe.DoesNotExistError:
            return {"error": "Locker not found."}

        if locker_booking.locker_status == "Vacant":
            locker_booking.locker_status = "Occupied"
            locker_booking.save()

            try:
                # Update locker status in Gym Locker Booking DocType
                frappe.db.set_value("Gym Locker Booking", locker_number, "locker_status", "Occupied")

                # Update locker status in Gym Locker Allotment DocType
                frappe.db.set_value("Gym Locker Allotment", locker_number, "locker_status", "Occupied")

                return {"message": ("Locker status updated to Occupied successfully.")}
            except Exception as e:
                frappe.log_error(frappe.get_traceback(), "Error Updating Locker Status")
                return {"error": ("Failed to update locker status: {0}".format(str(e)))}
        else:
            return {"message": ("Locker is already occupied.")}
    else:
        return {"error": "Locker number is required."}



