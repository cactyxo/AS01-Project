#AS02: KEDAI RUNCIT SALES TRACKER

FILENAME = "kedai_runcit_sales.csv"

#read the file, returns a list of clean rows and dirty rows
def load_file(filename):
    clean_rows = []
    dirty_rows = []

    try:
        file = open(filename, "r")
    except FileNotFoundError:
        print(f"Error: cannot find {filename}")
        return clean_rows, dirty_rows

    #Skips the header line
    lines = file.read().splitlines()[1:]
    file.close()

     # Check whether the row has 4 fields
    count = []
    rows = []
    for line in lines:
        fields = line.strip().split(",")
        count.append(len(fields))
        rows.append((fields + ["", "", "", ""])[:4])

    names = [row[0].strip() for row in rows]
    categories = [row[1].strip() for row in rows]
    qty = [row[2].strip() for row in rows]
    price = [row[3].strip() for row in rows]

    #Checks the validity of the data and whether its a valid number
    missing = [c < 4 for c in count]
    bad_qty = [not q.isdigit() for q in qty]
    negative_qty = [q.startswith("-") and q[1:].isdigit() for q in qty]
    bad_price = [not p.replace(".", "", 1).isdigit() for p in price]

    valid = []
    for i in range(len(rows)):
        valid.append(not missing[i] and not bad_qty[i] and not bad_price[i])

    # Dictionary for the clean row data (Latest Learnt Topic)
    for i in range(len(rows)):
        if valid[i]:
            clean_row = {
                "name": names[i],
                "category": categories[i],
                "quantity": int(qty[i]),
                "price": float(price[i])
            }
            clean_rows.append(clean_row)
        else:
            if missing[i]:
                reason = f"Missing field ({count[i]} columns found)"
            elif negative_qty[i]:
                reason = f"Negative quantity ({qty[i]})"
            elif bad_qty[i]:
                reason = f"Non-numeric quantity ({qty[i]})"
            else:
                reason = f"Non-numeric price ({price[i]})"

            dirty_row = {"row": i + 1, "product": names[i], "reason": reason}
            dirty_rows.append(dirty_row)

    return clean_rows, dirty_rows


#Loads the summary
def show_loading_summary(filename, clean_rows, dirty_rows):
    total_rows = len(clean_rows) + len(dirty_rows)
    print(f"=== Loading {filename} ===")
    print(f"Total rows read : {total_rows}")
    print(f"Clean rows      : {len(clean_rows)}")
    print(f"Dirty rows      : {len(dirty_rows)}")
    print()

    # Reads the file which returns a list of clean rows and a list of dirty rows (Summarises the data)
    print("--- Skipped Rows ---")
    for dirty in dirty_rows:
        print(f"Row {dirty['row']:>2} : {dirty['reason']:<32} - {dirty['product']}")
    print("-" * 60)
    print(f"{len(clean_rows)} rows ready for analysis.")


#Main program
def main():
    clean_rows, dirty_rows = load_file(FILENAME)
    if len(clean_rows) + len(dirty_rows) == 0:
        return
    show_loading_summary(FILENAME, clean_rows, dirty_rows)

main()