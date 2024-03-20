import datetime

# Constants for ticket prices
ONE_DAY_TICKET_PRICES = {
    'adult': 20.00,
    'child': 12.00,
    'senior': 16.00,
    'family': 60.00,
    'group': 15.00
}

TWO_DAY_TICKET_PRICES = {
    'adult': 30.00,
    'child': 18.00,
    'senior': 24.00,
    'family': 90.00,
    'group': 22.50
}

EXTRA_ATTRACTIONS_PRICES = {
    'lion feeding': 2.50,
    'penguin feeding': 2.00,
    'evening barbecue': 5.00
}

# Function to display ticket options and attractions
def display_options():
    print("Ticket Options for One-Day Visit:")
    for ticket_type, price in ONE_DAY_TICKET_PRICES.items():
        print(f"{ticket_type.capitalize()}: ${price:.2f}")

    print("\nTicket Options for Two-Day Visit:")
    for ticket_type, price in TWO_DAY_TICKET_PRICES.items():
        print(f"{ticket_type.capitalize()}: ${price:.2f}")

    print("\nExtra Attractions:")
    for attraction, price in EXTRA_ATTRACTIONS_PRICES.items():
        print(f"{attraction.capitalize()}: ${price:.2f}")

# Function to process a booking
def process_booking():
    # Input data
    ticket_type = input("Enter ticket type (adult/child/senior/family/group): ").lower()
    while ticket_type not in ONE_DAY_TICKET_PRICES.keys():
        ticket_type = input("Invalid ticket type. Please enter a valid ticket type: ").lower()

    num_tickets = int(input("Enter number of tickets: "))
    while num_tickets <= 0:
        num_tickets = int(input("Invalid number of tickets. Please enter a positive integer: "))

    days_visit = int(input("Enter number of days for visit (1 or 2): "))
    while days_visit not in [1, 2]:
        days_visit = int(input("Invalid number of days. Please enter 1 or 2: "))

    attractions = input("Enter extra attractions separated by commas (leave blank for none): ").lower().split(',')
    attractions_cost = sum([EXTRA_ATTRACTIONS_PRICES.get(attraction.strip(), 0) for attraction in attractions])

    # Calculate total cost
    if days_visit == 1:
        total_cost = num_tickets * ONE_DAY_TICKET_PRICES[ticket_type] + attractions_cost
    else:
        total_cost = num_tickets * TWO_DAY_TICKET_PRICES[ticket_type] + attractions_cost

    # Generate booking number
    booking_number = f"B{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"

    # Display booking details
    print("\nBooking Details:")
    print(f"Ticket Type: {ticket_type.capitalize()}")
    print(f"Number of Tickets: {num_tickets}")
    print(f"Days for Visit: {days_visit}")
    if attractions:
        print(f"Extra Attractions: {', '.join(attractions)}")
    print(f"Total Cost: ${total_cost:.2f}")
    print(f"Booking Number: {booking_number}")

# Main program loop
def main():
    while True:
        print("\nWelcome to the Wildlife Park Ticketing System")
        print("1. Display Ticket Options and Attractions")
        print("2. Process a Booking")
        print("3. Exit")

        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':
            display_options()
        elif choice == '2':
            process_booking()
        elif choice == '3':
            print("Thank you for using the Wildlife Park Ticketing System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
