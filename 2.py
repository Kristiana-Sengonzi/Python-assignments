


users_db = {
    "admin_user": ["admin123", "Admin"],
    "cashier_jane": ["cash456", "Cashier"],
    "customer_sam": ["cust789", "Customer"]
}


coupon_rules = {
    "WELCOME10": 0.10,  
    "SUPER20": 0.20,    
    "SAVE5": 0.05       
}


tax_rules = {
    "NY": 0.08,    
    "CA": 0.09,    
    "TX": 0.0625,  
    "FL": 0.06    
}


print("--- WELCOME TO THE E-COMMERCE PLATFORM ---")
input_username = input("Enter Username: ")
input_password = input("Enter Password: ")




if input_username in users_db and users_db[input_username][0] == input_password:
    user_role = users_db[input_username][1]
    print(f"\nLogin Successful! Welcome, {input_username}.")
    
   
    if user_role == "Admin":
        print("Access Level: [ADMIN] - Full System Access Granted.")
        print("Features: Manage Users, View Financial Reports, Run Checkout.")
        
        run_checkout = True 
        
    elif user_role == "Cashier":
        print("Access Level: [CASHIER] - Register Access Granted.")
        print("Features: Process Sales, Apply Discounts.")
        run_checkout = True
        
    elif user_role == "Customer":
        print("Access Level: [CUSTOMER] - Storefront Access Granted.")
        print("Features: Browse Products, Personal Checkout.")
        run_checkout = True
        
    
    if run_checkout:
        print("\n--- Processing Checkout Cart ---")
        try:
            subtotal = float(input("Enter Cart Subtotal Amount ($): "))
        except ValueError:
            print("Invalid amount entered. System defaulting to $0.00")
            subtotal = 0.0
            
        user_coupon = input("Enter Coupon Code (Leave blank if none): ").strip().upper()
        user_location = input("Enter Shipping Location/State (e.g., NY, TX): ").strip().upper()
        
        
        base_discount_rate = 0.0
        coupon_discount_rate = 0.0
        tax_rate = 0.0
        
        
        if subtotal >= 100.0:
            base_discount_rate = 0.15  
            print("Subtotal qualifies for the Premium 15% Tier.")
            
           
            if user_coupon in coupon_rules:
                coupon_discount_rate = coupon_rules[user_coupon]
                print(f"Valid coupon '{user_coupon}' applied! Adding extra discount.")
            elif user_coupon != "":
                print(f"Coupon '{user_coupon}' is invalid or expired.")
                
        elif subtotal >= 50.0:
            base_discount_rate = 0.10  
            print("Subtotal qualifies for the Standard 10% Tier.")
            
            
            if user_coupon in coupon_rules:
                coupon_discount_rate = coupon_rules[user_coupon]
                print(f"Valid coupon '{user_coupon}' applied! Adding extra discount.")
            elif user_coupon != "":
                print(f"Coupon '{user_coupon}' is invalid or expired.")
                
        else:
            base_discount_rate = 0.0
            print("Subtotal under $50. No baseline tier discounts apply.")
            
            
            if user_coupon in coupon_rules:
                coupon_discount_rate = coupon_rules[user_coupon]
                print(f"Valid coupon '{user_coupon}' applied!")
            elif user_coupon != "":
                print(f"Coupon '{user_coupon}' is invalid or expired.")

        
        if user_location in tax_rules:
            tax_rate = tax_rules[user_location]
            print(f"Tax rate for {user_location} identified as {tax_rate * 100}%.")
        else:
            tax_rate = 0.05  
            print(f"Location unknown. Applying standard fallback tax rate of 5%.")

        
        total_discount_rate = base_discount_rate + coupon_discount_rate
        discount_amount = subtotal * total_discount_rate
        discounted_subtotal = subtotal - discount_amount
        
        
        tax_amount = discounted_subtotal * tax_rate
        final_price = discounted_subtotal + tax_amount
        
        
        print("\n================================")
        print("        FINAL RECEIPT           ")
        print("================================")
        print(f"Original Subtotal:  ${subtotal:.2f}")
        print(f"Total Discount:   - ${discount_amount:.2f} ({total_discount_rate * 100:.1f}%)")
        print(f"Tax Amount:       + ${tax_amount:.2f} ({tax_rate * 100:.2f}%)")
        print("--------------------------------")
        print(f"FINAL PRICE:        ${final_price:.2f}")
        print("================================")

else:
    print("\n[ACCESS DENIED]: Invalid username or password configuration.")