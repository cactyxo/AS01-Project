while True:
    print ( "=============================================== " )
    print ( "     BruPass ID Validator - Staff terminal     " ) 
    print ( "=============================================== " )
    print ( "1. Validate a BruPass ID" )
    print ( "2. View Session Summary" )    
    print ( "3. Exit" )
    print ( "----------------------------------------------- " ) 
    
    choice = input("Enter your choice (1-3): ")
    if choice == "1":
        raw_id = input("Enter BruPass ID: (or press enter to cancel) ")
        if raw_id == "":
            print("BruPass ID validation cancelled.")
        else:
            print(f"  >> Validating BruPass ID: {raw_id} <<  ")
            cleaned = raw_id.replace("-", "").upper()
            if not cleaned.startswith("BP"):
                print("INVALID BruPass ID. It must start with 'BP'.")
            else: 
                category = cleaned[2:4]
                year_text = cleaned[4:8]
                sequence = cleaned[8:14] 
                
                if category not in ["CT", "PR", "WK", "ST"]:
                    print("INVALID BruPass ID. Category code is not recognized.")
                elif not year_text.isdigit():
                    print("INVALID BruPass ID. Year must be a 4-digit number.")
                elif int(year_text) < 2000 or int(year_text) > 2026:
                    print("INVALID BruPass ID. Year is out of valid range (2000-2026).")
                elif not sequence.isdigit():
                    print("INVALID BruPass ID. Sequence must be a 6-digit number.")
                else: 
                    print("BruPass ID is VALID.")
                    print(f"  >> Category: {category} <<  ")
                    print(f"  >> Year: {year_text} <<  ")
                    print(f"  >> Sequence: {sequence} <<  ")
                
            input("Press Enter to return to the main menu.")
    
    elif choice == "2":
        print("Session Summary:")   
        
    elif choice == "3":
        print("Exiting. Thank you for using the BruPass ID Validator.")
        break   

    else:
        print("Invalid choice. Please enter a number between 1 and 3.")
        print ()
