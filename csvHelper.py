import csv
import os
from datetime import datetime

# Define the CSV file name
csv_file_name = 'crypto_investments.csv'

def write_investment(coin_name, price, amount):
    """
    Write a new investment to the CSV file.

    Args:
        coin_name (str): Name of the cryptocurrency.
        price (float): Price at which the coin was bought.
        amount (float): Amount of the coin bought.
    """
    try:
        # Input validation
        if price <= 0 or amount <= 0:
            raise ValueError("Price and amount should be positive numbers.")
        
        # Check if the file exists to determine if headers should be written
        file_exists = os.path.isfile(csv_file_name)

        # Create or append to the CSV file
        with open(csv_file_name, mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['ID', 'Coin Name', 'Price', 'Amount', 'Timestamp'])

            # Write the header if the file is new
            if not file_exists:
                writer.writeheader()

            # Write the data row
            writer.writerow({
                'ID': datetime.now().strftime("%Y%m%d%H%M%S"),  # Unique ID based on timestamp
                'Coin Name': coin_name,
                'Price': price,
                'Amount': amount,
                'Timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })

    except Exception as e:
        print(f"Error adding investment: {e}")

def read_investments():
    """
    Read investments from the CSV file.

    Returns:
        list of dict: List of investment records.
    """
    investments = []

    # Check if the file exists
    if os.path.isfile(csv_file_name):
        with open(csv_file_name, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                investments.append(row)
    
    return investments

def delete_investment(investment_id):
    """
    Delete an investment by its ID.

    Args:
        investment_id (str): The unique ID of the investment to be deleted.
    """
    try:
        investments = read_investments()
        if investment_id not in [inv['ID'] for inv in investments]:
            raise ValueError("Investment ID not found.")
        
        investments = read_investments()
        investments = [inv for inv in investments if inv['ID'] != investment_id]

        with open(csv_file_name, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['ID', 'Coin Name', 'Price', 'Amount', 'Timestamp'])
            writer.writeheader()
            writer.writerows(investments)

        print(f"Investment with ID {investment_id} has been deleted.")

    except Exception as e:
        print(f"Error deleting investment: {e}")


def calculate_total(coin_name=None):
    """
    Calculate the total amount and money invested.

    Args:
        coin_name (str, optional): Name of the coin to calculate totals for. Defaults to None.
    """
    try:
        investments = read_investments()
        total_amount, total_invested = 0, 0

        for inv in investments:
            if coin_name is None or inv['Coin Name'] == coin_name:
                total_amount += float(inv['Amount'])
                total_invested += float(inv['Amount']) * float(inv['Price'])

        print(f"Total amount of {'all coins' if coin_name is None else coin_name}: {total_amount}")
        print(f"Total invested in {'all coins' if coin_name is None else coin_name}: ${total_invested}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
