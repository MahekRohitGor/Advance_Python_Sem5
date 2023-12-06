import csv

# Function to load train data from CSV file
def load_train_data(file_name):
    trains = {}
    with open(file_name, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            train_id, train_name, source, dest, total_seats, fare_per_seat = row
            trains[train_id] = {
                'train_name': train_name,
                'source': source,
                'destination': dest,
                'total_seats': int(total_seats),
                'fare_per_seat': float(fare_per_seat)
            }
    return trains

# Function to load passenger data from CSV file
def load_passenger_data(file_name):
    passengers = []
    with open(file_name, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header
        for row in reader:
            passenger_name, train_id, num_tickets = row
            passengers.append({
                'passenger_name': passenger_name,
                'train_id': train_id,
                'num_tickets': int(num_tickets)
            })
    return passengers

# Function to check seat availability and book tickets
def book_tickets(train_data, passengers):
    reports = {
        'train_details': [],
        'revenue_per_train': {}
    }

    for passenger in passengers:
        passenger_name = passenger['passenger_name']
        train_id = passenger['train_id']
        num_tickets = passenger['num_tickets']

        if train_id not in train_data:
            print(f"Error: Train with ID {train_id} not found.")
            continue

        train = train_data[train_id]
        available_seats = train['total_seats']

        if num_tickets <= available_seats:
            # Calculate fare
            total_fare = num_tickets * train['fare_per_seat']
            # Update seat availability
            train_data[train_id]['total_seats'] -= num_tickets
            # Update revenue
            if train_id not in reports['revenue_per_train']:
                reports['revenue_per_train'][train_id] = total_fare
            else:
                reports['revenue_per_train'][train_id] += total_fare

            # Add to train details report
            reports['train_details'].append({
                'passenger_name': passenger_name,
                'train_name': train['train_name'],
                'source': train['source'],
                'destination': train['destination'],
                'num_tickets': num_tickets,
                'total_fare': total_fare
            })

        else:
            print(f"Error: Insufficient seats on train {train_id} for passenger {passenger_name}.")

    return reports

# Function to generate reports
def generate_reports(train_data, reports):
    print("Train Details Report:")
    print("{:<15} {:<20} {:<15} {:<15} {:<15}".format('Train ID', 'Train Name', 'Source', 'Destination', 'Total Seats'))
    for train_id, train in train_data.items():
        print("{:<15} {:<20} {:<15} {:<15} {:<15}".format(
            train_id, train['train_name'], train['source'], train['destination'], train['total_seats']))

    print("\nRevenue Report:")
    print("{:<15} {:<20} {:<15}".format('Train ID', 'Train Name', 'Total Revenue'))
    for train_id, total_revenue in reports['revenue_per_train'].items():
        print("{:<15} {:<20} {:<15}".format(train_id, train_data[train_id]['train_name'], total_revenue))

# Main program
def main():
    try:
        # Load train data
        train_data = load_train_data('trains.csv')
        # Load passenger data
        passengers = load_passenger_data('passengers.csv')
        # Book tickets and generate reports
        reports = book_tickets(train_data, passengers)
        generate_reports(train_data, reports)
    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    main()
