import frappe
def company_name:
    frappe.db.set_value('System Settings', None, 'Login to Jupiter')