"""
RECORD CHECK  -  my version
===========================

Name  : Rohitha Biju Krishnan
Lane  : IT
Date  : 10/18/2026

"""


def status_of(percent):                                              # to determine the status of the devices with over limit, warning, ok
    """Return OVER LIMIT, WARNING, OK based on percentage"""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"

def check(value , limit):                                            
    """Reture differnce and percentage between value and limit"""
    difference = limit - value                                       # to calculate the free space available 
    percent = (value/limit)*100 
    return difference, percent                                       # to return both difference and percent back to the loop

def print_report(label, value, limit, difference, percent, status): 
    print(f"Used    :   {value:>5.2f}")
    print(f"Total   :   {limit:>5.2f}")
    print(f"Free    :   {difference:>5.2f}")
    print(f"Percent :   {percent:.2f}%")
    print(f"Status  :   {status}")

# =================================================================================== STORE
# records is a list which contain multiple dictionaries
records = [{"label" : "Computer" , "value" : "900" , "limit" : "1000"},
           {"label" : "Laptop" , "value" : "190" , "limit" : "120"},
           {"label" : "Phone" , "value" : "60" , "limit" : "100"},]   

# =================================================================================== PROCESS AND OUTPUT
over_limit_count = 0                                                 # a counter variable 

with open("Records4.txt" , "w") as f:                                # to create a new text file in overwrite mode
    """Extract data from dictionary"""
    for record in records:
        label_ = record["label"]                                     # to take values from dictionary and convert text strings to normal text
        value_ = float(record["value"])                              # to take values from dictionary and convert text strings to decimals
        limit_ = float(record["limit"])                              # to take values from dictionary and convert text strings to decimals

        difference, percent = check(value_, limit_)                  # by using the values and calculate the difference and percent
        status = status_of(percent)                                  # get the status of the device after calculating the percent

        print()
        print("=" * 34)
        print(f"  RECORD CHECK  -  {label_}")
        print("=" * 34)
        print_report(label_, value_, limit_, difference, percent, status) # to print the report below

        if status == "OVER LIMIT":                                   # if the status is equal to the over limit then it adds one to the counter variable 
            over_limit_count += 1
            
        f.write(f"{label_}, {status}\n")                             # a summary line to the records4 file
print(f"Number of records that are over limit: {over_limit_count}")
