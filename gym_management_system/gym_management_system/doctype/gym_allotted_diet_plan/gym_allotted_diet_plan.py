# Copyright (c) 2024, Rohit and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class GymAllottedDietPlan(Document):
    pass


@frappe.whitelist()
def fetch_diet_plan_server(diet_goal):
    # Fetch data from the Diet List DocType based on the provided diet_goal
    diet_plan_data = frappe.get_all("Diet List", filters={"diet_goal": diet_goal}, fields=["name", "diet_meal", "protein", "fat", "carbs"])

    return diet_plan_data



# @frappe.whitelist()
# def fetch_diet_plan(frm):
#     diet_goal = frm.doc.diet_goal

#     try:
#         data = frappe.get_all('Gym Diet Plan List', filters={'name': diet_goal})

#         if not data:
#             frappe.msgprint('No diet plan found for the selected goal.')
#             return

#         # Clear existing rows in the Diet Plan child table
#         frm.clear_table('diet_plan')

#         # Add fetched data to the Diet Plan child table
#         for row in data:
#             frm.append('diet_plan', {
#                 'diet_meal': row.diet_meal,
#                 'protein': row.protein,
#                 'fat': row.fat,
#                 'carbs': row.carbs
#             })

#     except Exception as e:
#         frappe.throw(f"Error fetching diet plan: {e}")
