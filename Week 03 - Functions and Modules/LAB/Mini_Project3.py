"""
RECORD CHECK  -  my version
===========================

Name  : ROHITHA BIJU KRISHNAN
Lane  :  IT
Date  : 10/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""



def status_of(percent):
    """Return OVER LIMIT, WARNING, OK based on percentage"""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"

def check(value , limit):
    """Reture differnce and percentage between value and limit"""
    difference = value - limit
    percent = (value/limit)*100
    return difference, percent


label = input("Enter label: ") 
value = float(input("Enter value: "))
limit = float(input("Enter limit:"))  

difference , percent = check(value, limit) 
status = status_of(percent)   

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

def print_report(label, value, limit, difference, percent, status):
    print(f"Used:       {value:>5.2f}")
    print(f"Total:      {limit:>5.2f}")
    print(f"Free:       {difference:>5.2f}")
    print(f"Percent:    {percent}%")
    print(f"Status:     {status}")
print_report(label, value, limit, difference, percent, status)
print("=" * 34)

