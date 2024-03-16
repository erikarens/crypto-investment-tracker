def print_investment_table(investments):
    """
    Print investments in a tabular format.

    Args:
        investments (list of dict): List of investment records.
    """
    if not investments:
        print("No investments to display.")
        return

    header = "ID", "Coin Name", "Price", "Amount", "Timestamp"
    # Determine the maximum width for each column
    col_widths = [max(len(str(row[col])) for row in investments) for col in header]

    # Print the header
    header_row = " | ".join(f"{title:{width}}" for title, width in zip(header, col_widths))
    print(header_row)
    print("-" * len(header_row))

    # Print each investment row
    for inv in investments:
        row = inv['ID'], inv['Coin Name'], inv['Price'], inv['Amount'], inv['Timestamp']
        print(" | ".join(f"{value:{width}}" for value, width in zip(row, col_widths)))