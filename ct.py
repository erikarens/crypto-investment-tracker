import argparse
from csvHelper import write_investment, read_investments, delete_investment, calculate_total
from visualizationHelper import print_investment_table

def main():
    parser = argparse.ArgumentParser(description='Crypto Investment Tracker')
    subparsers = parser.add_subparsers(dest='command')

    # Subparser for adding an investment
    add_parser = subparsers.add_parser('add', help='Add a new investment')
    add_parser.add_argument('coin_name', type=str, help='Name of the cryptocurrency')
    add_parser.add_argument('price', type=float, help='Price at which the coin was bought')
    add_parser.add_argument('amount', type=float, help='Amount of the coin bought')

    # Subparser for viewing investments
    view_parser = subparsers.add_parser('view', help='View investments')
    view_parser.add_argument('--coin', type=str, help='Filter by coin name')

    # Subparser for deleting an investment
    delete_parser = subparsers.add_parser('delete', help='Delete an investment')
    delete_parser.add_argument('id', type=str, help='ID of the investment to delete')

    # Subparser for calculating totals
    total_parser = subparsers.add_parser('total', help='Calculate total investments')
    total_parser.add_argument('--coin', type=str, help='Calculate total for a specific coin')

    args = parser.parse_args()
    handle_command(args)

def handle_command(args):
    """
    Handle the command based on the parsed arguments.

    Args:
        args (Namespace): Parsed arguments.
    """
    if args.command == 'add':
        write_investment(args.coin_name, args.price, args.amount)
        print(f'Investment in {args.coin_name} added successfully.')
    elif args.command == 'view':
        investments = read_investments()
        if args.coin:
            investments = [inv for inv in investments if inv['Coin Name'] == args.coin]
        print_investment_table(investments)
    elif args.command == 'delete':
        delete_investment(args.id)
    elif args.command == 'total':
        calculate_total(args.coin)
    else:
        print("Invalid command. Use 'add', 'view', 'delete', or 'total'.")

if __name__ == "__main__":
    main()
