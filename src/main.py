import sys
from session import Session
from standard import handle_withdrawal, handle_transfer, handle_paybill, handle_deposit
from admin import handle_create, handle_delete, handle_disable, handle_changeplan

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <currentaccounts.txt> <output_transactions.atf>")
        sys.exit(1)

    accounts_file = sys.argv[1]
    output_file = sys.argv[2]
    
    session = Session(accounts_file, output_file)
    print("Banking System Front End Loaded.")

    while True:
        try:
            cmd = input("Enter transaction: ").strip().lower()

            if cmd == "login":
                if session.is_logged_in:
                    print("Error: Already logged in.")
                    continue

                mode = input("Session type (standard/admin): ").strip().lower()
                if mode not in ["standard", "admin"]:
                    print("Error: Invalid session type.")
                    continue

                if mode == "standard":
                    name_input = input("Account holder name: ").strip()
                    valid_names = [data['name'] for data in session.accounts.values()]
                    
                    if name_input not in valid_names:
                        print("Error: Invalid account holder name.")
                        continue
                    session.current_user = name_input
                else:
                    session.current_user = "admin"

                session.mode = mode
                session.is_logged_in = True
                print(f"Logged in successfully as {session.mode}.")

            elif not session.is_logged_in:
                print("Error: Must login first.")

            elif cmd == "logout":
                session.log_transaction("00", session.current_user, "00000", 0.0)
                print("Session terminated.")
                session.is_logged_in = False
                session.mode = None
                session.current_user = ""

            elif cmd in ["withdraw", "withdrawal"]:
                handle_withdrawal(session)
            elif cmd == "transfer":
                handle_transfer(session)
            elif cmd == "paybill":
                handle_paybill(session)
            elif cmd == "deposit":
                handle_deposit(session)
            elif cmd == "create":
                handle_create(session)
            elif cmd == "delete":
                handle_delete(session)
            elif cmd == "disable":
                handle_disable(session)
            elif cmd == "changeplan":
                handle_changeplan(session)
            else:
                print("Error: Transaction not recognized.")
                
        except EOFError:
            break
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main()