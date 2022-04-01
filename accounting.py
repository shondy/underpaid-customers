def print_payment_status(payment_data_filename):
    """Calculate cost of melons and determine who has underpaid."""

    melon_cost = 1.00
    the_file = open(payment_data_filename)

    # Iterate over lines in file
    for line in the_file:
        # remove spaces to the right
        line = line.rstrip()

        # Split line by '|' to get a list of strings
        order = line.split('|')

        full_name = order[1]

        # split full_name and take first element to get first name
        first_name = full_name.split(" ")[0]

        # Get number of melons and amount customer paid
        melons_qty = int(order[2])
        amount_paid = float(order[3])

        # Calculate expected price of customer's order
        customer_expected = melons_qty * melon_cost

        print(f"{first_name} paid ${amount_paid:.2f},",
            f"expected ${customer_expected:.2f}"
            )

        # Print payment status
        #
        # If customer overpaid, print that they've overpaid for their melons. If
        # customer underpaid, print that they've underpaid for their melons.
        if customer_expected < amount_paid:
            print(f"{first_name} has overpaid for their melons.")

        elif customer_expected > amount_paid:
            print(f"{first_name} has underpaid for their melons.")


# Call the function
print_payment_status("customer-orders.txt")