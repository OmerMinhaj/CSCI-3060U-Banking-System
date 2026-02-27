class Session:
    def __init__(self, accounts_path, output_path):
        self.accounts_path = accounts_path
        self.output_path = output_path
        self.is_logged_in = False
        self.mode = None 
        self.current_user = ""
        self.accounts = {}
        self.load_accounts()

    def load_accounts(self):
        """Loads account data from the text file into a dictionary for validation."""
        try:
            with open(self.accounts_path, "r") as f:
                for line in f:
                    acc_num = line[0:5]
                    if acc_num == "00000": 
                        continue # Skip END_OF_FILE marker
                    name = line[6:26].strip()
                    status = line[27]
                    balance = float(line[29:37])
                    self.accounts[acc_num] = {'name': name, 'status': status, 'balance': balance}
        except FileNotFoundError:
            print(f"Error: Could not find {self.accounts_path}")

    def log_transaction(self, code, name, acc_num, amount, misc="  "):
        """Writes a fixed-length 41-character line to the transaction file."""
        # CC_AAAAAAAAAAAAAAAAAAAA_NNNNN_PPPPPPPP_MM
        line = f"{code} {name:<20} {acc_num:>05} {amount:08.2f} {misc}"
        with open(self.output_path, "a") as f:
            f.write(line + "\n")