tracker = "EXPENSE_TRACKER.txt"



def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    amount = int(input("Enter amount numbers: "))
    description = input("Enter purpose of expenditure: ")

    # storage = [{"date":date,"amount":amount,"description":description},]
    data = f"{date},{amount},{description}\n"

    file_store = open(tracker,"a")
    file_store.write(data)
    file_store.close()
    print("Expense data saved!.")


def view_expenses():
    try:
        with open(tracker, "r") as f1:
            data = f1.readlines()
            if len(data) == 0:
                print("There is no expense..")
            else:
                for line in data:
                    print(line.strip())
    except FileNotFoundError:
        print("Error: File not Found..")
        

def calculate_total():
    total = 0
    try: 
        with open(tracker, "r") as f1:
            data = f1.readlines()
            if len(data) == 0:
                print("There is no expense..")
            else:
                for lines in data:
                    parts = lines.strip().split(",")
                    amount = int(parts[1])
                    date = parts[0]
                    # print(f"{date} : {amount}")
                    total += int(amount)
        print("Toatal Expense: ",total)
    except FileNotFoundError:
        print("Expense File Not found.")



def main():

    while True:
        print("Options: add | view | total | exit")
        user_input = input("choose....").strip().lower()
        if user_input == "add":
            add_expense()
        elif user_input == "view":
            view_expenses()
        elif user_input == "total":
            calculate_total()
        else:
            print("......?")
            break

main()