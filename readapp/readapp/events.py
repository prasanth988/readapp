# import frappe

# def demo(doc,method=None):
#     doc=frappe.get_doc("College Details","jthj6u1nbk")
#     doc.full_name="raju kumar"
#     doc.save()
#     print(doc)

import frappe

def demo(doc=None, method=None):
    # Fetch the document by doctype and name
    college_doc = frappe.get_doc("College Details", "jthj6u1nbk")
    
    # Update the field
    college_doc.full_name = "Raju Kumar"
    
    # Save the document wertyu   
    college_doc.save()
    
    # Optional: print to console for debugging
    print(f"Updated document: {college_doc.name} with full_name: {college_doc.full_name}")
