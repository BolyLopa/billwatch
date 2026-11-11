# === Stage 76: Add graceful keyboard interrupt handling in the CLI entry point ===
# Project: BillWatch
def main():
    bills = load_bills()
    try:
        while True:
            show_menu()
            choice = input("Command: ").strip().lower()
            if choice in ("quit", "exit", "q"):
                break
            elif choice in ("list", "show"):
                list_bills(bills)
            elif choice in ("add"):
                add_bill(bills)
            elif choice in ("pay", "mark_paid"):
                mark_paid(bills)
            elif choice in ("summary"):
                monthly_summary(bills)
            elif choice == "help":
                show_help()
            else:
                print("Unknown command. Type 'help' for options.")
    except (KeyboardInterrupt, EOFError):
        print()
        print("Goodbye!")
