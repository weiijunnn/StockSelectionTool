from functions import(
    registration,
    authenticate,
    get_closing_prices,
    analyze_closing_prices,
    save_to_csv,
    read_from_csv,
)

def main():
    print("Welcome to the Stock Selection Tool")
    while True:
        choice = input("1. Register\n2. Login\n3. Quit\nEnter your choice: ")
        if choice == "1":
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            try:
                print(registration(email, password))
            except ValueError as e:
                print(e)
        elif choice == "2":
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            if authenticate(email, password):
                print("Login successful!")
                while True:
                    print("\nOptions:\n1. Retrieve Stock Data\n2. View Saved Data\n3. Logout")
                    sub_choice = input("Enter your choice: ")
                    if sub_choice == "1":
                        ticker = input("Enter stock ticker: ")
                        start_date = input("Enter start date (YYYY-MM-DD): ")
                        end_date = input("Enter end date (YYYY-MM-DD): ")
                        try:
                            data = get_closing_prices(ticker, start_date, end_date)
                            print("Closing Prices:")
                            print(data)
                            analysis = analyze_closing_prices(data)
                            print("Analysis:")
                            for key, value in analysis.items():
                                print(f"{key}: {value}")
                            save_to_csv(
                                {"email": email, "ticker": ticker, **analysis},
                                filename="users.csv",
                            )
                        except Exception as e:
                            print(f"Error: {e}")
                    elif sub_choice == "2":
                        try:
                            print(read_from_csv("users.csv"))
                        except FileNotFoundError as e:
                            print(e)
                    elif sub_choice == "3":
                        break
                    else:
                        print("Invalid choice. Try again.")
            else:
                print("Invalid credentials.")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

