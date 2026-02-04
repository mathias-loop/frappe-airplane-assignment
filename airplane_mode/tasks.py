import frappe

def send_rent_reminders():
    # Debug: Confirm function started
    print("--- REMINDERS STARTED ---")

    # 1. Check Settings
    enable_reminders = frappe.db.get_single_value('Shop Settings', 'enable_check_reminders')
    print(f"Debug: Enable Reminders is set to: {enable_reminders}")

    if not enable_reminders:
        print("--- REMINDERS STOPPED: Settings are disabled ---")
        return

    # 2. Find Shops
    shops = frappe.get_all(
        "Airport Shop",
        filters={
            "status": "Occupied",
            "tenant_email": ["is", "set"]
        },
        fields=["shop_name", "tenant_name", "tenant_email", "rent_amount"]
    )
    
    print(f"Debug: Found {len(shops)} shops to email.")

    # 3. Send Emails
    for shop in shops:
        print(f"Debug: Sending email to {shop.tenant_email} for {shop.shop_name}")
        frappe.sendmail(
            recipients=[shop.tenant_email],
            subject=f"Rent Reminder for {shop.shop_name}",
            message=f"""
            Dear {shop.tenant_name},
            
            This is a friendly reminder that your monthly rent of {shop.rent_amount} 
            for {shop.shop_name} is due.
            
            Regards,
            Airport Management
            """
        )
    
    print("--- REMINDERS FINISHED ---")