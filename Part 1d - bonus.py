#1d
#BP-CT2019-000142-7

BruPass = input("Enter BruPass ID: ")
clean_id = BruPass.replace("-", "")
cat_code = clean_id[2:4]      # Gets 'CT'
year_str = clean_id[4:8]      # Gets '2019'
seq_num = clean_id[8:14]      # Gets '000142'

if len(BruPass) == 12 and cat_code in ["CT", "PR", "WK", "ST"]: 
    status = "result:valid"
else: 
    status = "result:invalid"

if status == "result:valid":
    print("The ID is valid and active.")
    
elif status == "result:invalid":
    print("The ID is invalid or may require renewal.")
    

if cat_code == "CT":
    category_name = "Citizen"
elif cat_code == "PR":
    category_name = "Permanent Resident"
elif cat_code == "WK":
    category_name = "Work Permit Holder"
elif cat_code == "ST":
    category_name = "Student Pass Holder"
    
current_year = 2026
year_of_issue = int(year_str)
years_elapsed = current_year - year_of_issue

if years_elapsed > 5:
    status = "May require renewal (issued more than 5 years ago)"
else:
    status = "Active" 

print("\n--- Information Extraction ---")
print(f"Result          : VALID")
print(f"Category        : {category_name} ({cat_code})")
print(f"Year of Issue   : {year_of_issue}")
print(f"Sequence Number : {seq_num}")
print(f"Status          : {status}\n")

#1e

def display_session_summary(total_checked, valid_count, invalid_count, valid_ids_list):
   
    print("="*45)
    print("             SESSION SUMMARY              ")
    print("="*45)
    
    # Check if any IDs have been validated during the session
    
    if total_checked == 0:
        print("No IDs have been checked yet in this session.")
    else:
        print(f"Total checked : {total_checked}")
        print(f"Valid         : {valid_count}")
        print(f"Invalid       : {invalid_count}")
        print()
        
        # Display valid IDs if any exist
        if valid_count > 0:
            print("Valid BruPass IDs (raw user input):")
            for index, raw_id in enumerate(valid_ids_list, start=1):
                print(f"  {index}.  {raw_id}")
        else:
            print("No valid BruPass IDs were entered during this session.")
            
    print("==========================================")

# bonus

def validate_check_digit(clean_id):
    """
    Validates Rule 6: Check Digit (Z) for BruPass ID.
    clean_id must be a hyphen-stripped string of 16 characters.
    """
    # 1. Extract the check digit Z (16th character, index 15)
    provided_check_digit = clean_id[15]
    
    # Ensure provided check digit is numeric
    if not provided_check_digit.isdigit():
        return False, "Rule #6 Failed: Check digit must be a single numeric digit."

    # 2. Extract the CC + YYYY + NNNNNN (indices 2 through 13)
    middle_section = clean_id[2:14]
    
    # 3. Sum only digit characters from middle_section
    digit_sum = sum(int(char) for char in middle_section if char.isdigit())
            
    # 4. Calculate Z = mod 10
    calculated_check_digit = digit_sum % 10
    
    # 5. Verify match
    if calculated_check_digit == int(provided_check_digit):
        return True, "Check digit is valid."
    else:
        return False, f"Rule #6 Failed: Check digit mismatch (Expected {calculated_check_digit}, got {provided_check_digit})."
