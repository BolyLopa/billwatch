# === Stage 53: Add command help text and usage examples ===
# Project: BillWatch
def print_help():
    """Print usage information and examples for BillWatch."""
    help_text = (
        "BillWatch - Household Bill Tracker\n"
        "Usage: python billwatch.py <command> [options]\n\n"
        "Commands:\n"
        "  add <name> <amount> [category] [due_date]  - Add a new bill\n"
        "  list [status]                                - List bills (optionally by status)\n"
        "  pay <id>                                     - Mark a bill as paid\n"
        "  summary [month]                              - Show monthly summary\n"
        "  help                                         - Show this help message\n\n"
        "Examples:\n"
        "  python billwatch.py add 'Electric' 150.00 'Utilities' '2024-03-15'\n"
        "  python billwatch.py list\n"
        "  python billwatch.py list paid\n"
        "  python billwatch.py pay 1\n"
        "  python billwatch.py summary 2024-03\n"
    )
    print(help_text)
