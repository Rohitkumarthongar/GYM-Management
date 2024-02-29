# Copyright (c) 2024, Rohit and contributors
# For license information, please see license.txt
import frappe
from frappe.model.document import Document
from datetime import datetime


class Revenue(Document):
    @frappe.whitelist()
    def before_insert(self):
        frappe.print("YEs it's Working")
        console.log("Yes It's Working")      
        equipment_cost = frappe.db.get_single_value("Gym Settings", "equipment_cost")
        trainer_cost = frappe.db.get_single_value("Gym Settings", "trainer_cost")
        building_rent = frappe.db.get_single_value("Gym Settings", "building_cost")
        extra_cost = frappe.db.get_single_value("Gym Settings", "extra_cost")
        electricity_bill = frappe.db.get_single_value("Gym Settings", "electricity_bill")
        water_bill = frappe.db.get_single_value("Gym Settings", "water_bill")

       
        trainer_count = frappe.db.count("Gym Trainer")
        self.no_of_trainer = trainer_count

        
        current_month = datetime.now().strftime("%B")  
        current_year = datetime.now().year

        
        subscription_status = "Active"
        membership_count = frappe.db.sql("""
            SELECT COUNT(*) FROM `tabGym Membership`
            WHERE docstatus = 1  # Submitted documents
            AND YEAR(creation) = %s
            AND MONTH(creation) = %s
            AND subscription_status = %s
        """, (current_year, current_month, subscription_status))[0][0]
        self.total_number_of_members = membership_count

        
        payable_amount = frappe.db.sql("""
            SELECT SUM(payable_amount) FROM `tabGym Membership`
            WHERE docstatus = 1  # Submitted documents
            AND YEAR(creation) = %s
            AND MONTH(creation) = %s
        """, (current_year, current_month))[0][0]

        
        total_trainer_cost = trainer_cost * trainer_count

       
        total_costs = equipment_cost + total_trainer_cost + building_rent + extra_cost + electricity_bill + water_bill

       
        self.total_revenue = payable_amount - total_costs

       
        self.name = f"{current_month} {current_year} Revenue: {self.total_revenue}"
