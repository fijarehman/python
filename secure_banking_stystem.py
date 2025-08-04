#  a list to store all the transaction records.
#  each record itself will be an immutable tuble.
transaction_logs = []
print("__recording transactions__")
# transaction 1
account_number_1 = "account_number_01"
amount_1 = 150.75
transaction_type_1 = "deposit"
timestamp_1 = "2025-10-01 10:00:00"
transaction_1 = (account_number_1, amount_1, transaction_type_1, timestamp_1)
transaction_logs.append(transaction_1)
print(f"recorded: {transaction_1}")
# transaction 2
account_number_2 = "account_number_02"
amount_2 = 75.00
transaction_type_2 = "withdrawal"
timestamp_2 = "2025-10-01 11:00:00"
transaction_2 = (account_number_2, amount_2, transaction_type_2, timestamp_2)
transaction_logs.append(transaction_2)
print(f"recorded: {transaction_2}")
# transaction 3
account_number_3 = "account_number_03"
#  represnting moeny outgoing from the account
amount_3 = 25.00
transaction_type_3 = "withdrawal"
timestamp_3 = "2025-10-01 12:00:00"
transaction_3 = (account_number_3, amount_3, transaction_type_3, timestamp_3)
transaction_logs.append(transaction_3)
print(f"recorded: {transaction_3}")
print("recorded: {transaction_3}")
print("\n---attempting to modify a stored record (demostrating immutability)---")
try:
    #  this line attempts to change the amount of the first transaction.
    # becouse transaction_logos[0] is a tuple, this operation will fail.
    transaction_logs[0][1] = 200.00
except TypeError as e:
    print(f"Error: {e}")
    print("this  confirms that individual transaction records {tuples} cannot be modified after creation.")
    print("\n---displaying all recorded transactions---")
    if not transaction_logs:
        print("no transactions recorded yet .")
    else:
        for i in range(len(transaction_logs)):
            tranaction = transaction_logs[i]
            print(f"record {i+1}: Account: {tranaction[0]}, Amount: {tranaction[1]}, Type: {tranaction[2]}, Timestamp: {tranaction[3]}")