def validate_account(session, acc):
    """Helper function to check if an account is valid, active, and owned by the user."""
    if acc not in session.accounts:
        print("Error: Account does not exist.")
        return False
    if session.accounts[acc]['status'] == 'D':
        print("Error: Account is disabled.")
        return False
    if session.mode == "standard" and session.accounts[acc]['name'] != session.current_user:
        print("Error: Not authorized for this account.")
        return False
    return True

def handle_withdrawal(session):
    acc = input("Account number: ").strip()
    if not validate_account(session, acc): return

    try:
        amount = float(input("Amount: ").strip())
    except ValueError:
        print("Error: Invalid amount.")
        return

    if session.mode == "standard" and amount > 500:
        print("Error: Maximum withdrawal is $500.00.")
        return
    if amount < 0:
        print("Error: Amount must be positive.")
        return
    if session.accounts[acc]['balance'] - amount < 0:
        print("Error: Insufficient funds.")
        return

    session.accounts[acc]['balance'] -= amount
    session.log_transaction("01", session.current_user, acc, amount)
    print("Withdrawal logged successfully.")

def handle_transfer(session):
    from_acc = input("From account: ").strip()
    if not validate_account(session, from_acc): return

    to_acc = input("To account: ").strip()
    if to_acc not in session.accounts:
        print("Error: Destination account does not exist.")
        return
    if session.accounts[to_acc]['status'] == 'D':
        print("Error: Destination account is disabled.")
        return

    try:
        amount = float(input("Amount: ").strip())
    except ValueError:
        print("Error: Invalid amount.")
        return

    if session.mode == "standard" and amount > 1000:
        print("Error: Maximum transfer is $1000.00.")
        return
    if amount < 0:
        print("Error: Amount must be positive.")
        return
    if session.accounts[from_acc]['balance'] - amount < 0:
        print("Error: Insufficient funds.")
        return

    session.accounts[from_acc]['balance'] -= amount
    session.accounts[to_acc]['balance'] += amount
    session.log_transaction("02", session.current_user, from_acc, amount)
    print("Transfer logged successfully.")

def handle_paybill(session):
    acc = input("Account number: ").strip()
    if not validate_account(session, acc): return

    company = input("Company (EC, CQ, or FI): ").strip().upper()
    if company not in ["EC", "CQ", "FI"]:
        print("Error: Invalid company.")
        return

    try:
        amount = float(input("Amount: ").strip())
    except ValueError:
        print("Error: Invalid amount.")
        return

    if session.mode == "standard" and amount > 2000:
        print("Error: Maximum bill payment is $2000.00.")
        return
    if amount < 0:
        print("Error: Amount must be positive.")
        return
    if session.accounts[acc]['balance'] - amount < 0:
        print("Error: Insufficient funds.")
        return

    session.accounts[acc]['balance'] -= amount
    session.log_transaction("03", session.current_user, acc, amount, misc=company)
    print("Bill payment logged successfully.")

def handle_deposit(session):
    acc = input("Account number: ").strip()
    if not validate_account(session, acc): return

    try:
        amount = float(input("Amount: ").strip())
    except ValueError:
        print("Error: Invalid amount.")
        return

    if amount <= 0:
        print("Error: Deposit amount must be positive.")
        return

    session.accounts[acc]['balance'] += amount
    session.log_transaction("04", session.current_user, acc, amount)
    print("Deposit logged successfully.")