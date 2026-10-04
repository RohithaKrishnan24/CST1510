"""
RECORD CHECK  -  my version
===========================

Name  : Rohitha Biju Krishnan
Lane  :  IT
Date  : 10/2/2026


Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""
# ================================================================== PROCESS

label = input("Enter the server name: ")
first = float(input("Enter used space: "))
second = float(input("Enter total space: "))

difference = second - first    # to find the free space by subtracting used space from total space
percent = (first / second) * 100     # to find the percentage of used space

# =================================================================== OUTPUT
print()
print("=" * 31)
print(f"    RECORD CHECK  -  {label}")                                # NAME
print("=" * 31)

# ===================================================================== REPORT
print(f"Used  Space: {first:>14.2f} GB")                              # USED SPACE
print(f"Total Space: {second:>14.2f} GB")                             # TOTAL SPACE
print(f"Free  Space: {difference:>+14.2f} GB")                        # FREE SPACE
print(f"Percentage Used: {percent:>9.2f} %")                          # PERCENTAGE USED
print("=" * 31)
print(f"{first:.2f} GB of {second:.2f} GB used")                     # SUMMARY
print("=" * 31)
