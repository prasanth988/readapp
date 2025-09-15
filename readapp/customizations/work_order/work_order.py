import frappe

def notify_quality_inspector(doc, method=None):
    if doc.doctype == "Work Order" and doc.status == "Completed":
        try:
            # Get users with Quality Inspector role
            users = frappe.get_all(
                "Has Role",
                filters={"role": "Quality Inspector"},
                fields=["parent"]
            )

            recipients = []
            for u in users:
                email = frappe.db.get_value("User", u.parent, "email")
                enabled = frappe.db.get_value("User", u.parent, "enabled")
                if email and enabled:  # only active users with email
                    recipients.append(email)

            if recipients:
                subject = f"Quality Inspection Perfect – Work Order {doc.name}"
                message = f"""
                    Dear Quality Inspector,<br><br>
                    The Work Order <b>{doc.name}</b> has been marked as 
                    <b>Completed</b>.<br><br>
                    Please proceed with your quality inspection.<br><br>
                    Regards,<br>
                    ERPNext System
                """
                frappe.sendmail(
                    recipients=recipients,
                    subject=subject,
                    message=message
                )

                # ✅ Success log
                frappe.logger().info(
                    f"[Work Order {doc.name}] Email sent to Quality Inspectors: {', '.join(recipients)}"
                )
            else:
                # ⚠️ No recipients log
                frappe.logger().warning(
                    f"[Work Order {doc.name}] No active Quality Inspector with email found."
                )

        except Exception as e:
            # ❌ Error log
            frappe.log_error(
                title=f"Work Order Email Error [{doc.name}]",
                message=frappe.get_traceback()
            )

