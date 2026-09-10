# === Stage 16: Add argparse support for the most common commands ===
# Project: BillWatch
import argparse
from datetime import datetime

def parse_arguments():
    parser = argparse.ArgumentParser(
        description="BillWatch - Track household bills with due dates, payment status, and monthly summaries."
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands:")

    add_parser = subparsers.add_parser("add", help="Add a new bill")
    add_parser.add_argument("name", help="Bill name")
    add_parser.add_argument("due_date", help="Due date (YYYY-MM-DD)")
    add_parser.add_argument("--category", default="Other", help="Bill category (default: Other)")
    add_parser.add_argument("--amount", type=float, help="Bill amount")
    add_parser.add_argument("--status", default="pending", help="Payment status (pending, paid, overdue)")

    list_parser = subparsers.add_parser("list", help="List all bills")
    list_parser.add_argument("--status", choices=["pending", "paid", "overdue"], help="Filter by status")
    list_parser.add_argument("--category", help="Filter by category")

    summary_parser = subparsers.add_parser("summary", help="Show monthly bill summary")
    summary_parser.add_argument("--month", help="Month to summarize (YYYY-MM)")
    summary_parser.add_argument("--status", choices=["pending", "paid", "overdue"], help="Filter by status")

    return parser.parse_args()

def main():
    args = parse_arguments()
    if args.command == "add":
        print(f"Added bill: {args.name} | Due: {args.due_date} | Amount: {args.amount or 'N/A'} | Status: {args.status}")
    elif args.command == "list":
        print("Listing bills...")
    elif args.command == "summary":
        print(f"Monthly summary for {args.month or 'current'}...")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
