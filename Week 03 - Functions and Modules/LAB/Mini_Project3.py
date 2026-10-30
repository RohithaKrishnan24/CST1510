"""
RECORD CHECK  -  my version
===========================

Name  : ROHITHA BIJU KRISHNAN
Lane  :  IT
Date  : 10/10/2026

"""


# function to understand status based on percentage calculated
def status_of(percent):
    """Return OVER LIMIT, WARNING, OK based on percentage"""
    if percent >= 100:                                        # to check if value is equal to or more than 100 which returns over limit
        return "OVER LIMIT"
    elif percent >= 90:                                       # to check if value is equal to or more than 90 which returns warning
        return "WARNING"
    else:                                                     # to check if value is lower than the limit which returns ok
        return "OK"

# function to perform calculation on given value and limit
def check(value , limit):
    """Return differnce and percentage between value and limit"""
    difference = value - limit
    percent = (value/limit)*100
    return difference, percent                                # to send both calculated numbers back so that to use again later

# to get initial input from the user
label = input("Enter label: ") 
value = float(input("Enter value: "))
limit = float(input("Enter limit:"))  

# function calls and processes
difference , percent = check(value, limit)                   # pass the user values to the function to get the difference and percent
status = status_of(percent)                                  # to get the calculated percentage to find which status it belongs to

# to print report
print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

# to print the final report
def print_report(value, limit, difference, percent, status):
    print(f"Used:       {value:>5.2f}")                       # to print the used value entered by the user
    print(f"Total:      {limit:>5.2f}")                       # to print the total entered by the user
    print(f"Free:       {difference:>5.2f}")                  # to print the difference of value and limit enetered by the user
    print(f"Percent:    {percent}%")                          # to print the percentage
    print(f"Status:     {status}")                            # to print the status based on percentage calculated
    
# to trigger the print function to form the whole report
print_report(label, value, limit, difference, percent, status)
print("=" * 34)