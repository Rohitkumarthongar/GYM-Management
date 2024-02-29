import frappe
from frappe.model.docstatus import DocStatus
from frappe.model.document import Document

class GymSubscription(Document):
    def before_submit(self):
        if self.subscription_status in ["Active", "Expired", "Pending"]:
            self.update_membership_status(self.subscription_status)

    def update_membership_status(self, status):
        self.validate_issue()
        membership = frappe.get_doc("Gym Member", self.member_name)
        membership.status = status
        membership.save()


    def validate_membership(self):
        valid_membership = frappe.db.exists(
            "Gym Membership",
            {
                "member_name": self.member_name,
                "docstatus": DocStatus.submitted,
                "joining_date": ("<", self.date),
                "exp_date": (">", self.date),
            },
        )
        if not valid_membership:
            frappe.throw("The member does not have a valid membership")
