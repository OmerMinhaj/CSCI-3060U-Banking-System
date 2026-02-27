def handle_create(session):
    if session.mode != "admin":
        print("Error: Privileged transaction.")
        return
        
    acc = input("New account number: ").strip()
    if acc in session.accounts:
        print("Error: Account number already exists.")
        return

    name = input("Account name: ").strip()
    if len(name) > 20:
        print("Error: Name exceeds 20 characters.")
        return

    try:
        amount = float(input("Initial balance: ").strip())
    except ValueError:
        print("Error: Invalid amount.")
        return

    if amount < 0 or amount > 99999.99:
        print("Error: Invalid initial balance.")
        return

    session.accounts[acc] = {'name': name, 'status': 'A', 'balance': amount}
    session.log_transaction("05", name, acc, amount)
    print("Create logged successfully.")

def handle_delete(session):
    if session.mode != "admin":
        print("Error: Privileged transaction.")
        return
        
    acc = input("Account number to delete: ").strip()
    if acc not in session.accounts:
        print("Error: Account does not exist.")
        return

    name = input("Account name: ").strip()
    if session.accounts[acc]['name'] != name:
        print("Error: Account name mismatch.")
        return

    del session.accounts[acc]
    session.log_transaction("06", name, acc, 0.0)
    print("Delete logged successfully.")

def handle_disable(session):
    if session.mode != "admin":
        print("Error: Privileged transaction.")
        return
        
    acc = input("Account number to disable: ").strip()
    if acc not in session.accounts:
        print("Error: Account does not exist.")
        return

    name = input("Account name: ").strip()
    if session.accounts[acc]['name'] != name:
        print("Error: Account name mismatch.")
        return

    session.accounts[acc]['status'] = 'D'
    session.log_transaction("07", name, acc, 0.0)
    print("Disable logged successfully.")

def handle_changeplan(session):
    if session.mode != "admin":
        print("Error: Privileged transaction.")
        return
        
    acc = input("Account number for plan change: ").strip()
    if acc not in session.accounts:
        print("Error: Account does not exist.")
        return

    name = input("Account name: ").strip()
    if session.accounts[acc]['name'] != name:
        print("Error: Account name mismatch.")
        return

    session.log_transaction("08", name, acc, 0.0)
    print("Change plan logged successfully.")