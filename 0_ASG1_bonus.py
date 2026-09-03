# GROUP CODE : DCSY 01

# GROUP MEMBERS :
# MUHAMMAD AIMAN BIN RAMLI - 25FTT1747
# FAREES ZIKRY BIN JASNI - 25FTT1760
# MUHAMMAD HAKIM AMSYAR IRSYADUDDIN BIN HAJI SHAHIROL DINI - 25FTT1758

# SESSION VARIABLES : THIS IS WHERE TO KEEP TRACK OF THE IDS DURING THE SESSION.

total_id_checked = 0
valid_id_count = 0
invalid_id_count = 0
valid_ids = []

# MENU DISPLAY : DISPLAY THE MAIN MENU TO THE USER ( STAFF )

def menu():
    print("============================================")
    print("   BruPass ID Validator - Staff terminal    ")
    print("============================================")
    print("[1] Validate a BruPass ID")
    print("[2] View Session Summary")
    print("[3] Exit")
    print("--------------------------------------------")

# VALIDATION OF BRUPASS ID ( CHECKS EVERY REQUIRED RULES IN THE CORRECT ORDER )

def validate_brupass_id(raw_id):

    cleaned_id = raw_id.replace("-","").upper()

    if not cleaned_id.startswith("BP"):
        print("INVALID BruPass ID.")
        print("BruPass ID must starts with 'BP'.")
        return False

    if len(cleaned_id) !=16:
        print("INVALID BruPass ID.")
        print("BruPass ID must be 16 characters long.")
        return False

    category_code = cleaned_id[2:4]

    if category_code not in ["CT", "PR", "WK", "ST"]:
            print("INVALID BruPass ID.")
            print("BruPass ID must be either in CT, PR, WK or ST.")
            return False

    year_text = cleaned_id[4:8]

    if not year_text.isdigit():
            print("INVALID BruPass ID.")
            print("BruPass ID must contain 4 characters")
            return False

    year = int(year_text)

    if year < 2000 or year > 2026:
            print("INVALID BruPass ID.")
            print("BruPass ID year must be between 2000 and 2026 to be valid.")
            return False
    
    sequence_numbers = cleaned_id[8:14]

    if not sequence_numbers.isdigit():
            print("INVALID BruPass ID.")
            print("BruPass Sequence number must be exactly 6 digtis ")
            return False

    check_digit = cleaned_id[15]

    if not check_digit.isdigit():
            print("INVALID Check Digit.")
            print("Check Digit must be a single digit")
            return False

    # CALCULATING THE CHECK DATA:

    digit_character = cleaned_id[2:14]

    digit_sum = 0

    for character in digit_character:
         if character.isdigit():
              digit_character = digit_sum + int(character)

    calculated_check_digit = digit_sum % 10

    if int(check_digit) != calculated_check_digit:
         print("Invalid Check Digit.")
         print("Expected check digit:", calculated_check_digit)
         return False

    return True

# INFORMATION EXTRACTION : THIS IS WHERE THE EXTRACTS AND INFORMATION ARE BEING DISPLAYED ( FOR VALID BRUPASS ID ).

def information_extracted(raw_id):

    cleaned_id = raw_id.replace("-","").upper()
    category_code = cleaned_id[2:4]
    year = int(cleaned_id[4:8])
    sequence_number = cleaned_id[8:14]

# DETERMINING CATEGORY CODE

    if category_code == 'CT':
         category_code = ("Citizen (CT)")
        
    elif category_code == 'PR':
         category_code = ("Permanent Citizen")
        
    elif category_code == 'WK':
         category_code = ("Work Permit Holder (WK)")
        
    elif category_code == 'ST':
         category_code = ("Student Pass Holder (ST)")
        
    else:
        print("No Validated BruPass.")

# DETERMINING ID STATUS

    current_year = 2026

    if current_year - year > 5:
        status = "May require renewal (issued more than 5 years ago)"
    else:
        status = "Active"

    print("----------------------------------------------")
    print("BruPass Status: Valid")
    print("----------------------------------------------")
    print("========== BruPass Session Summary ===========")
    print("  Registration category  : ", category_code)
    print("  Year of issued         : ", year)
    print("  Sequence number        : ", sequence_number)
    print("  Status                 : ", status)
    print("==============================================")

# SESSION SUMMARY SECTION : DISPLAY EVERYTHING CHECKED DURING THE SESSION.

def summary_session():

    print("==============================================")
    print("               SESSION SUMMARY                ")
    print("==============================================")

    if total_id_checked == 0:
         print("Session is empty. No ID has been checked yet.")
         print("==============================================")
         return
    
    print(f"Total checked  :{total_id_checked}")
    print(f"Valid ID       :{valid_id_count}")
    print(f"Invalid        :{invalid_id_count}")
    print("")
    print("Valid BruPass IDs this session:")

    if len(valid_ids) == 0:
        print("No valid IDs were entered.")
    else:
        number = 1

        for id in valid_ids:
             print(str(number) + ". " + id.upper())
             number = number + 1
    print("==============================================")

# MAIN MENU LOOP : THIS IS TO KEEP THE PROGRAM TO CONTINUE RUNNING UNTIL THE USER SELECTS TO EXIT.

while True:

    menu()

    choice = input("Enter your option (1-3): ")

    if choice == "1":

         raw_id = input("Enter BruPass ID ( or press enter to cancel): ")

         print(f">> Checking : {raw_id}...")

         if raw_id == "":
              print("INVALID INPUT. Please enter a BruPass ID.")
              continue

         total_id_checked = total_id_checked + 1

         is_valid = validate_brupass_id(raw_id)

         if is_valid:
              valid_id_count = valid_id_count + 1

              valid_ids.append(raw_id)

              information_extracted(raw_id)

         else:
              invalid_id_count = invalid_id_count + 1

         input("Press Enter to return to the main menu.")

    elif choice == "2":

         summary_session()

         input("Press Enter to return to the main menu.")

    elif choice == "3":

         print("==============================================")
         print("                 Thank you!                   ")
         print("==============================================")
         break

    else:
         print("Invalid Option. Please Enter 1, 2 or 3.")
         