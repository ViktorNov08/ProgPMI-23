def validate_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Enter a positive number.")
            else:
                return value
        except ValueError:
            print("Invalid input format. Enter an integer.")


def calculate_minimum_time(N, M):
    
    total_time_minutes = (N + 1) * M + N * (M + 1)

    return total_time_minutes


if __name__ == "__main__":
   
    
    N = validate_input("Enter the number of blocks in the south-north direction (N): ")
    M = validate_input("Enter the number of blocks in the west-east direction (M): ")

    minutes_required = calculate_minimum_time(N, M)
    print(f"The minimum number of minutes required to walk the site: {minutes_required} minutes.")
